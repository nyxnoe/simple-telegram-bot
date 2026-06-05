# Simple Telegram Bot 🤖

A lightweight, fast, and easy-to-use Telegram bot built with `python-telegram-bot`.

**Features:**
- ✅ Free and Open Source
- ✅ Minimal dependencies (only 2 packages)
- ✅ Fast deployment (5 minutes)
- ✅ Simple command handlers
- ✅ User statistics tracking
- ✅ No complex integration needed
- ✅ Ready to deploy on Railway/Render

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nyxnoe/simple-telegram-bot.git
   cd simple-telegram-bot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env and add your TELEGRAM_BOT_TOKEN
   ```

4. **Run the bot:**
   ```bash
   python bot.py
   ```

## 📝 Available Commands

| Command | Description |
|---------|-------------|
| `/start` | Initialize bot and see welcome message |
| `/help` | Show all available commands |
| `/echo <text>` | Repeat your message |
| `/stats` | View your usage statistics |
| `/time` | Get current date and time |
| `/flip` | Flip a coin (Heads/Tails) |
| `/hello` | Get a friendly greeting |
| `/count` | See total number of users |

## 📞 How to Get Your Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/botfather)
2. Send `/start` and follow the instructions
3. Send `/newbot` to create a new bot
4. Choose a name and username for your bot
5. Copy the token provided
6. Paste it in your `.env` file as `TELEGRAM_BOT_TOKEN`

## 🏗️ Project Structure

```
simple-telegram-bot/
├── bot.py              # Main bot script
├── requirements.txt    # Python dependencies
├── .env.example       # Environment variables template
├── .gitignore         # Git ignore rules
├── setup.sh           # Setup script
├── Procfile           # Cloud deployment config
├── DEPLOYMENT.md      # Deployment guide
└── README.md          # This file
```

## 🔧 How It Works

The bot uses the `python-telegram-bot` library with polling mode:

1. **Command Handlers** - Process `/start`, `/help`, `/echo`, etc.
2. **Message Handlers** - Respond to regular text messages
3. **User Tracking** - Store basic user data (name, message count, join time)
4. **Error Handler** - Gracefully handle errors

## 🚀 Deployment

### Local
```bash
python bot.py
```

### Cloud (Railway/Render)
See `DEPLOYMENT.md` for detailed instructions.

## 🔧 Customization

Easy to add more commands:

```python
async def my_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("My response")

application.add_handler(CommandHandler('mycommand', my_command))
```

## 📄 License

MIT License - Free to use and modify

## 🤝 Contributing

Feel free to fork, modify, and submit pull requests!

## 📞 Support

For issues or questions, open an issue in this repository.

---

**Made with ❤️ for quick and easy bot deployment**
