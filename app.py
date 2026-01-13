#!/usr/bin/env python3
"""
Basecamp Card Table Dashboard - Flask Web App
Auto-refreshing kanban board with age-based coloring
"""

from flask import Flask, render_template, jsonify
import requests
from datetime import datetime, timezone
import os

app = Flask(__name__)

# ============================================================================
# CONFIGURATION - Set these as environment variables in Render
# ============================================================================

BASECAMP_ACCOUNT_ID = os.environ.get('BASECAMP_ACCOUNT_ID')
BASECAMP_ACCESS_TOKEN = os.environ.get('BASECAMP_ACCESS_TOKEN')
PROJECT_ID = os.environ.get('PROJECT_ID')
CARD_TABLE_ID = os.environ.get('CARD_TABLE_ID')
USER_AGENT = os.environ.get('USER_AGENT', 'Basecamp Dashboard (app)')

# Age thresholds
AGE_THRESHOLD_YELLOW = int(os.environ.get('AGE_THRESHOLD_YELLOW', 3))
AGE_THRESHOLD_RED = int(os.environ.get('AGE_THRESHOLD_RED', 14))

# ============================================================================
# BASECAMP API FUNCTIONS
# ============================================================================

def get_basecamp_headers():
    """Return headers for Basecamp API requests"""
    return {
        "Authorization": f"Bearer {BASECAMP_ACCESS_TOKEN}",
        "User-Agent": USER_AGENT
    }

def calculate_card_age(created_at):
    """Calculate how many days old a card is"""
    created_date = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
    now = datetime.now(timezone.utc)
    age_days = (now - created_date).days
    return age_days

def get_card_color(age_days):
    """Determine card color based on age"""
    if age_days >= AGE_THRESHOLD_RED:
        return "#fee2e2"  # Light red
    elif age_days >= AGE_THRESHOLD_YELLOW:
        return "#fef3c7"  # Light yellow
    else:
        return "#d1fae5"  # Light green

def fetch_card_table_data():
    """Fetch Card Table and all cards from Basecamp"""
    try:
        # Fetch Card Table structure
        url = f"https://3.basecampapi.com/{BASECAMP_ACCOUNT_ID}/buckets/{PROJECT_ID}/card_tables/{CARD_TABLE_ID}.json"
        response = requests.get(url, headers=get_basecamp_headers())
        
        if response.status_code != 200:
            return {"error": f"Failed to fetch Card Table: {response.status_code}"}
        
        card_table = response.json()
        
        # Get all lists (columns)
        all_lists = card_table.get('lists', [])
        
        # Filter to active columns only
        columns = [col for col in all_lists if col.get('type') in ['Kanban::Column', 'Kanban::Triage']]
        
        # Fetch cards for each column
        columns_data = []
        for column in columns:
            column_id = column['id']
            column_name = column['title']
            
            # Fetch cards
            cards_url = f"https://3.basecampapi.com/{BASECAMP_ACCOUNT_ID}/buckets/{PROJECT_ID}/card_tables/lists/{column_id}/cards.json"
            cards_response = requests.get(cards_url, headers=get_basecamp_headers())
            
            cards = []
            if cards_response.status_code == 200:
                raw_cards = cards_response.json()
                
                # Process each card
                for card in raw_cards:
                    age_days = calculate_card_age(card['created_at'])
                    color = get_card_color(age_days)
                    
                    # Get assignees
                    assignees = [person.get('name', 'Unassigned') for person in card.get('assignees', [])]
                    if not assignees:
                        assignees = ['Unassigned']
                    
                    cards.append({
                        'title': card['title'],
                        'age_days': age_days,
                        'color': color,
                        'assignees': assignees,
                        'created_at': card['created_at']
                    })
            
            columns_data.append({
                'name': column_name,
                'cards': cards
            })
        
        return {
            'title': card_table.get('title', 'Card Table'),
            'columns': columns_data,
            'thresholds': {
                'yellow': AGE_THRESHOLD_YELLOW,
                'red': AGE_THRESHOLD_RED
            },
            'updated_at': datetime.now().isoformat()
        }
    
    except Exception as e:
        return {"error": str(e)}

# ============================================================================
# ROUTES
# ============================================================================

@app.route('/')
def index():
    """Serve the main dashboard page"""
    return render_template('dashboard.html')

@app.route('/api/cards')
def get_cards():
    """API endpoint that returns current card data as JSON"""
    data = fetch_card_table_data()
    return jsonify(data)

@app.route('/health')
def health():
    """Health check endpoint for Render"""
    return jsonify({"status": "healthy"})

# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
