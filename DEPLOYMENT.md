# Deployment Guide for Simple Telegram Bot

## 🚀 Deployment Options

### Option 1: Local Machine (Development)

```bash
# Clone
git clone https://github.com/nyxnoe/simple-telegram-bot.git
cd simple-telegram-bot

# Setup
pip install -r requirements.txt
cp .env.example .env

# Edit .env with your bot token
# Then run
python bot.py
```

### Option 2: Railway.app (Recommended - Free & Easy)

#### Setup Steps:

1. Go to [Railway.app](https://railway.app)
2. Sign up with GitHub
3. Click **"New Project"** → **"Deploy from GitHub repo"**
4. Select `simple-telegram-bot` repository
5. Add environment variable:
   - Key: `TELEGRAM_BOT_TOKEN`
   - Value: Your bot token from @BotFather
6. Click **"Deploy"** ✅

**Cost:** Free tier includes 5GB/month

**Pro Tips:**
- Railway will auto-redeploy on git push
- View logs in Railway dashboard
- Set up custom domain (optional)

### Option 3: Render (Free)

#### Setup Steps:

1. Go to [Render.com](https://render.com)
2. Sign up with GitHub
3. Click **"New"** → **"Background Worker"**
4. Connect your GitHub repo
5. Select branch `main`
6. Add environment variable:
   - Key: `TELEGRAM_BOT_TOKEN`
   - Value: Your bot token
7. Click **"Create Web Service"** ✅

**Cost:** Free tier with limitations (limited build time)

### Option 4: Heroku (Paid - $5/month)

#### Setup Steps:

1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Login: `heroku login`
3. Create app: `heroku create your-app-name`
4. Set environment variable:
   ```bash
   heroku config:set TELEGRAM_BOT_TOKEN=your_token_here
   ```
5. Deploy:
   ```bash
   git push heroku main
   ```

### Option 5: AWS Lambda (Free tier eligible)

More complex - requires webhook setup instead of polling.

## 📋 Environment Variables

```
TELEGRAM_BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
```

**How to get:**
1. Open Telegram
2. Search [@BotFather](https://t.me/botfather)
3. Send `/newbot`
4. Copy the token provided

## ✅ Verify Deployment

After deployment:

1. Open Telegram
2. Search for your bot (by username)
3. Send `/start`
4. Bot should respond with welcome message ✅

If bot doesn't respond:
- Check if `TELEGRAM_BOT_TOKEN` is set correctly
- Check application logs for errors
- Verify token is active in BotFather

## 🔍 Monitoring

### Railway Dashboard
- View logs: Project → Deployments → Logs
- Monitor resources: Project → Metrics
- Auto-redeploy: Push to GitHub

### Render Dashboard
- View logs: Service → Logs
- Monitor: Service → Metrics
- Manual redeploy: Click "Manual Deploy"

## 💰 Cost Comparison

| Platform | Free Tier | Cost After |
|----------|-----------|------------|
| Railway | 5GB/month | $5/month |
| Render | Limited | $7/month |
| Heroku | None | $5/month |
| AWS Lambda | 1M requests/month | Pay per use |

**Recommendation:** Use **Railway** for best free tier value and ease of deployment.

## 🐛 Troubleshooting

### Bot not responding
- Check `TELEGRAM_BOT_TOKEN` in platform dashboard
- Verify bot token is correct from @BotFather
- Check application logs for Python errors
- Ensure network connectivity (bot can reach Telegram API)

### Deployment fails
- Ensure `requirements.txt` is present
- Check Python version (3.8+)
- Review deployment logs for specific errors
- Try redeploying

### Bot crashes
- Check logs for error messages
- Ensure environment variables are set
- Verify bot token hasn't expired

## 📈 Next Steps

After successful deployment:

1. **Test all commands** - Send `/help` to see commands
2. **Monitor logs** - Check dashboard logs for issues
3. **Add more features** - Edit `bot.py` and push to GitHub
4. **Share with friends** - Search for your bot on Telegram!

---

**Made with ❤️ for easy bot deployment**
