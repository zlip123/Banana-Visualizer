# 🚀 Quick Deployment Guide

## Deploy to Render in 5 Minutes

### 1️⃣ Push to GitHub

```bash
# Create new repo on GitHub: basecamp-kanban-dashboard

# In your terminal:
cd basecamp-dashboard
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/basecamp-kanban-dashboard.git
git push -u origin main
```

### 2️⃣ Deploy on Render

1. Go to [render.com](https://render.com) → Sign up/Login
2. Click **"New +"** → **"Web Service"**
3. **Connect GitHub** → Select `basecamp-kanban-dashboard`
4. **Configure:**
   - Name: `basecamp-kanban`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Plan: **Free**

5. **Add Environment Variables** (click "Advanced"):

```
BASECAMP_ACCOUNT_ID = 5835116
BASECAMP_ACCESS_TOKEN = BAhbB0kiAbB7ImNsaWVudF9pZCI6ImVkY2NiMjcyYmRlZjU3MDQ5N2QzNzc0MjNhMGM3MTU0NzkwZGMwZjEiLCJleHBpcmVzX2F0IjoiMjAyNi0wMS0yN1QwMToyMToxNloiLCJ1c2VyX2lkcyI6WzUxNjYzMTk1XSwidmVyc2lvbiI6MSwiYXBpX2RlYWRib2x0IjoiMjA5ZTJmNGU1N2RjOWNiMjc4NDU3MmQxODJiNTFjZGUifQY6BkVUSXU6CVRpbWUNYYMfwHhoCVUJOg1uYW5vX251bWkBsDoNbmFub19kZW5pBjoNc3VibWljcm8iBxdgOgl6b25lSSIIVVRDBjsARg==--e2386dcdb7a4541672db13449d48a25cda5421f1
PROJECT_ID = 38747490
CARD_TABLE_ID = 7720422504
USER_AGENT = Basecamp Dashboard (zelda.greenwald@gatech.edu)
AGE_THRESHOLD_YELLOW = 7
AGE_THRESHOLD_RED = 14
```

6. Click **"Create Web Service"**

### 3️⃣ Done! 🎉

Your dashboard will be live at:
```
https://basecamp-kanban.onrender.com
```
(or whatever name you chose)

Wait 2-3 minutes for first deployment.

---

## 🔄 Auto-Refresh Features

- ✅ Updates every **60 seconds** automatically
- ✅ Shows live status indicator
- ✅ Pauses when tab is hidden (saves bandwidth)
- ✅ No manual refresh needed!

## 💰 Cost

**$0/month** on Render's free tier!

**Limitations:**
- Sleeps after 15 min of inactivity (wakes in ~30 seconds)
- 750 hours/month free (enough for normal use)

**Want always-on?** Upgrade to paid tier ($7/month)

---

## 📺 Office Display Setup

Perfect for displaying on:
- Office TV/monitor
- Second monitor during meetings
- Shared team dashboard

Just open the URL and let it auto-refresh! 🍌
