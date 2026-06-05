#!/bin/bash

echo "🤖 Setting up Simple Telegram Bot..."

# Check Python version
python3 --version

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "✅ Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Copy environment file
echo "⚙️ Setting up .env file..."
cp .env.example .env
echo "⚠️ Please edit .env and add your TELEGRAM_BOT_TOKEN"

echo ""
echo "✅ Setup complete!"
echo "👉 Edit .env with your bot token, then run: python bot.py"
