# 🍌 Basecamp Kanban Dashboard

Auto-refreshing web dashboard that displays your Basecamp Card Table with age-based color coding.

![Dashboard Preview](https://img.shields.io/badge/Auto--Refresh-60s-green) ![Status](https://img.shields.io/badge/Status-Live-brightgreen)

## 🌟 Features

- ✅ **Auto-refreshing** - Updates every 60 seconds automatically
- 🎨 **Age-based coloring** - Cards change color based on age
  - 🟢 Green: 0-3 days old
  - 🟡 Yellow: 4-13 days old
  - 🔴 Red: 14+ days old
- 📱 **Responsive design** - Works on desktop, tablet, and mobile
- 🚀 **Free hosting** on Render
- 🔒 **Secure** - Credentials stored as environment variables

## 🚀 Deploy to Render (Free)

### Step 1: Push to GitHub

1. Create a new repository on GitHub (e.g., `basecamp-kanban-dashboard`)

2. Initialize git and push:
```bash
cd basecamp-dashboard
git init
git add .
git commit -m "Initial commit: Basecamp kanban dashboard"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/basecamp-kanban-dashboard.git
git push -u origin main
```

### Step 2: Deploy on Render

1. **Sign up/Login** to [Render](https://render.com)

2. **Click "New +"** → **"Web Service"**

3. **Connect your GitHub repository**
   - Select `basecamp-kanban-dashboard`

4. **Configure the service:**
   - **Name:** `basecamp-kanban` (or your choice)
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Plan:** `Free`

5. **Add Environment Variables** (click "Advanced" → "Add Environment Variable"):
   
   ```
   BASECAMP_ACCOUNT_ID=5835116
   BASECAMP_ACCESS_TOKEN=YOUR_ACCESS_TOKEN_HERE
   PROJECT_ID=38747490
   CARD_TABLE_ID=7720422504
   USER_AGENT=Basecamp Dashboard (zelda.greenwald@gatech.edu)
   AGE_THRESHOLD_YELLOW=7
   AGE_THRESHOLD_RED=14
   ```

6. **Click "Create Web Service"**

7. Wait 2-3 minutes for deployment ⏳

8. Your dashboard will be live at: `https://basecamp-kanban.onrender.com` 🎉

### Step 3: Access Your Dashboard

Visit your Render URL and you'll see:
- Live kanban board with colored cards
- Auto-refreshes every 60 seconds
- "Live • Auto-refreshing" indicator in header

## 🔧 Local Development

### Run Locally

1. **Set environment variables:**
```bash
export BASECAMP_ACCOUNT_ID="5835116"
export BASECAMP_ACCESS_TOKEN="YOUR_TOKEN"
export PROJECT_ID="38747490"
export CARD_TABLE_ID="7720422504"
export USER_AGENT="Basecamp Dashboard (your.email@example.com)"
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the app:**
```bash
python app.py
```

4. **Open browser:**
```
http://localhost:5000
```

## ⚙️ Customization

### Change Refresh Interval

Edit `templates/dashboard.html` line 246:
```javascript
const REFRESH_INTERVAL = 60000; // milliseconds (60 seconds)
```

### Change Age Thresholds

Set environment variables:
```
AGE_THRESHOLD_YELLOW=7   # Days until yellow
AGE_THRESHOLD_RED=14     # Days until red
```

### Change Colors

Edit `app.py` in `get_card_color()` function:
```python
def get_card_color(age_days):
    if age_days >= AGE_THRESHOLD_RED:
        return "#fee2e2"  # Change this hex color
    elif age_days >= AGE_THRESHOLD_YELLOW:
        return "#fef3c7"  # Change this hex color
    else:
        return "#d1fae5"  # Change this hex color
```

## 📋 API Endpoints

- `GET /` - Main dashboard page
- `GET /api/cards` - JSON API with card data
- `GET /health` - Health check endpoint

## 🐛 Troubleshooting

### Dashboard shows "Failed to fetch data"
- Check environment variables are set correctly in Render
- Verify Basecamp access token is valid
- Check Render logs: Dashboard → "Logs" tab

### Cards not showing
- Verify cards exist in your Basecamp Card Table
- Check that Card Table ID is correct
- Run `GET /api/cards` directly to see JSON response

### Free tier sleeping
- Render's free tier sleeps after 15 minutes of inactivity
- First visit after sleep takes ~30 seconds to wake up
- Consider upgrading to paid tier ($7/month) for always-on service

## 📊 Project Structure

```
basecamp-dashboard/
├── app.py                 # Flask application
├── templates/
│   └── dashboard.html     # Auto-refreshing dashboard
├── requirements.txt       # Python dependencies
├── Procfile              # Render start command
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🎯 Next Steps

- [ ] Deploy to Render
- [ ] Share URL with team
- [ ] Customize colors/thresholds
- [ ] Display on office TV/monitor during meetings
- [ ] Consider adding authentication for sensitive projects

## 📝 License

MIT License - Feel free to use and modify!

## 🙋 Support

If you have questions, check Render's [documentation](https://render.com/docs) or Basecamp's [API docs](https://github.com/basecamp/bc3-api).

---

**Made with 🍌 for efficient project management**
