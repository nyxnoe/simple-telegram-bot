#!/usr/bin/env python3
"""
Simple Telegram Bot with basic commands
Free and Open Source - No heavy dependencies
"""

import logging
import os
import random
from datetime import datetime
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Store user data
user_data_store = {}

# ============ COMMAND HANDLERS ============

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    user_id = user.id
    
    if user_id not in user_data_store:
        user_data_store[user_id] = {
            'name': user.first_name,
            'messages': 0,
            'joined': datetime.now()
        }
    
    welcome_message = f"""
👋 Welcome {user.first_name}!

I'm a simple Telegram bot. Here are my commands:

/start - Welcome message
/help - Show all commands
/echo <text> - Echo your message
/stats - Your statistics
/time - Current time
/flip - Flip a coin
/hello - Get a greeting
/count - Total users

Type anything to chat!
    """
    
    await update.message.reply_text(welcome_message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send help message."""
    help_text = """
📚 Available Commands:

/start - Welcome message
/help - Show this message
/echo <text> - Repeat your message
/stats - Show your statistics
/time - Get current time
/flip - Coin flip
/hello - Friendly greeting
/count - Total users

Just chat with me too!
    """
    await update.message.reply_text(help_text)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo user's message."""
    if not context.args:
        await update.message.reply_text("Usage: /echo <your message>")
        return
    
    echo_text = ' '.join(context.args)
    await update.message.reply_text(f"🔊 Echo: {echo_text}")
    
    user_id = update.effective_user.id
    if user_id in user_data_store:
        user_data_store[user_id]['messages'] += 1

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show user statistics."""
    user_id = update.effective_user.id
    user = update.effective_user
    
    if user_id not in user_data_store:
        user_data_store[user_id] = {
            'name': user.first_name,
            'messages': 0,
            'joined': datetime.now()
        }
    
    data = user_data_store[user_id]
    stats_text = f"""
📊 Your Statistics:

Name: {data['name']}
Messages: {data['messages']}
Joined: {data['joined'].strftime('%Y-%m-%d %H:%M:%S')}
    """
    await update.message.reply_text(stats_text)

async def get_time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send current time."""
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    await update.message.reply_text(f"🕐 Current time: {current_time}")

async def flip_coin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Flip a coin."""
    result = random.choice(['Heads', 'Tails'])
    await update.message.reply_text(f"🪙 Coin flip: {result}")

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send greeting."""
    user_name = update.effective_user.first_name
    await update.message.reply_text(f"👋 Hello {user_name}! Nice to see you!")

async def count_users(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Count total users."""
    count = len(user_data_store)
    await update.message.reply_text(f"👥 Total users: {count}")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle regular messages."""
    user_id = update.effective_user.id
    user = update.effective_user
    
    if user_id not in user_data_store:
        user_data_store[user_id] = {
            'name': user.first_name,
            'messages': 0,
            'joined': datetime.now()
        }
    
    user_data_store[user_id]['messages'] += 1
    
    user_message = update.message.text
    
    responses = {
        'hello': '👋 Hello! How can I help?',
        'hi': '👋 Hey there!',
        'how are you': '😊 I\'m doing great!',
        'thanks': '😊 You\'re welcome!',
        'bye': '👋 Goodbye! See you!',
        'who are you': '🤖 I\'m a simple bot!',
    }
    
    message_lower = user_message.lower()
    
    for keyword, response in responses.items():
        if keyword in message_lower:
            await update.message.reply_text(response)
            return
    
    await update.message.reply_text(f"📝 You said: {user_message}\n\nType /help for commands!")

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log errors."""
    logger.error(f"Error: {context.error}")

def main() -> None:
    """Start the bot."""
    load_dotenv()
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not TOKEN:
        print("❌ Error: TELEGRAM_BOT_TOKEN not set in .env file")
        print("Get token from @BotFather on Telegram")
        return
    
    print("✅ Bot starting...")
    print(f"🤖 Token: {TOKEN[:10]}...")
    
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('echo', echo))
    application.add_handler(CommandHandler('stats', stats))
    application.add_handler(CommandHandler('time', get_time))
    application.add_handler(CommandHandler('flip', flip_coin))
    application.add_handler(CommandHandler('hello', hello))
    application.add_handler(CommandHandler('count', count_users))
    
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    application.add_error_handler(error_handler)
    
    print("🚀 Bot polling started...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
