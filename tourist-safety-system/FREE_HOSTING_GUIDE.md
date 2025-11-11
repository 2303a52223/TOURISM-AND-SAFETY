# Free Hosting Setup Guide

## 🌐 Best FREE Hosting Options for Your App

### 1. 🚂 Railway.app (RECOMMENDED - Easiest)
**Free Tier:** 500 hours/month + $5 credit

**Deploy Steps:**
1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select `2303a52223/TOURISM-AND-SAFETY`
5. Railway auto-detects Python and deploys!
6. Add environment variables in Settings:
   - `MONGO_URI` = your MongoDB connection
   - `SECRET_KEY` = your secret key
7. Get URL: `https://your-app.up.railway.app`

**Why Best:** Zero configuration needed, auto-scales, includes free PostgreSQL/Redis if needed

---

### 2. 🎨 Render.com (Best for Production)
**Free Tier:** 750 hours/month (always on)

**Deploy Steps:**
1. Go to https://render.com
2. Sign up with GitHub
3. New → Web Service
4. Connect `2303a52223/TOURISM-AND-SAFETY`
5. Settings:
   - Root Directory: `tourist-safety-system`
   - Build Command: `./build.sh`
   - Start Command: `gunicorn --chdir backend --bind 0.0.0.0:$PORT app:app`
6. Add Environment Variables
7. Deploy!

**Why Good:** No sleep, custom domains, auto-deploy on push

---

### 3. 🟣 Heroku (Classic Choice)
**Free Tier:** DISCONTINUED (Now $5/month minimum)

**If you want to pay $5/month:**
1. Go to https://heroku.com
2. Create new app
3. Connect GitHub repo
4. Enable automatic deploys
5. Add Config Vars (environment variables)
6. Uses `Procfile` automatically

---

### 4. 🐍 PythonAnywhere (Python Specific)
**Free Tier:** 1 web app, always on

**Deploy Steps:**
1. Go to https://www.pythonanywhere.com
2. Sign up (free account)
3. Open Bash console
4. Clone repo: `git clone https://github.com/2303a52223/TOURISM-AND-SAFETY.git`
5. Create virtual environment: `mkvirtualenv --python=/usr/bin/python3.10 myenv`
6. Install deps: `pip install -r TOURISM-AND-SAFETY/tourist-safety-system/backend/requirements.txt`
7. Go to Web tab → Add new web app
8. Manual configuration → Python 3.10 → Flask
9. Set WSGI file path: `/home/yourusername/TOURISM-AND-SAFETY/tourist-safety-system/backend/wsgi.py`
10. Reload web app

**Why Good:** Always on, no sleep, perfect for Flask

---

### 5. 🔵 Glitch.com (Quickest Deploy)
**Free Tier:** Unlimited projects, sleeps after 5 min inactive

**Deploy Steps:**
1. Go to https://glitch.com
2. New Project → Import from GitHub
3. Enter: `https://github.com/2303a52223/TOURISM-AND-SAFETY`
4. Add `.env` file with variables
5. Glitch auto-starts!

**Why Good:** Instant preview, collaborative editing

---

### 6. ⚡ Vercel (Serverless - LIMITED)
**Free Tier:** Unlimited bandwidth

**Note:** Vercel works but has limitations:
- 10 second timeout per request
- Serverless (not ideal for Flask)
- No WebSockets

Already configured with `vercel.json` in your repo.

---

## 🗄️ Free MongoDB Hosting

Your app needs MongoDB. Use:

### MongoDB Atlas (FREE Forever)
1. Go to https://www.mongodb.com/cloud/atlas
2. Sign up free
3. Create free cluster (512MB storage)
4. Create database user
5. Get connection string
6. Add to environment variables as `MONGO_URI`

**Connection String Format:**
```
mongodb+srv://username:password@cluster.mongodb.net/tourist_safety?retryWrites=true&w=majority
```

---

## 📝 Quick Start Recommendation

**For Beginners:** Use **Railway.app**
- Easiest setup
- Auto-detects everything
- No configuration needed
- Just connect GitHub and deploy!

**For Production:** Use **Render.com**
- Always on (no sleep)
- Free SSL certificates
- Custom domains
- Auto-deploy on git push

**For Python Focus:** Use **PythonAnywhere**
- Made for Python/Flask
- Always on
- SSH access
- Best for learning

---

## 🚀 Environment Variables Needed

Add these to your hosting platform:

```
MONGO_URI=mongodb+srv://user:pass@cluster.mongodb.net/tourist_safety
SECRET_KEY=your-super-secret-key-here-change-this
FLASK_ENV=production
PORT=5000
```

---

## ✅ All Configuration Files Ready

Your repo now has:
- ✅ `Procfile` (Heroku/Railway)
- ✅ `render.yaml` (Render.com)
- ✅ `railway.json` (Railway.app)
- ✅ `vercel.json` (Vercel)
- ✅ `build.sh` (Build script)
- ✅ `requirements.txt` (Dependencies)

**Just pick a platform and deploy!** 🎉
