# Ai-Chatbot
A Telegram bot powered by Groq's Llama model with memory for personal questions.
# Khode Ai Telegram Bot 🤖

A Telegram bot powered by Groq's Llama model with memory for personal questions.

## ✨ Features
- **Intelligent Responses**: Uses Groq's Llama 3.3 70B model for smart conversations
- **Memory System**: Personalized responses for questions about the bot
- **Randomized Answers**: Multiple variations for common questions
- **Simple Interface**: Easy-to-use Telegram bot commands
- **Error Handling**: Graceful error recovery and user-friendly messages

## 🚀 Quick Setup

### 1. Get API Keys
- **Telegram Bot Token**: Get from [@BotFather](https://t.me/botfather) on Telegram
- **Groq API Key**: Get from [Groq Cloud](https://console.groq.com)

### 2. Install Dependencies

pip install pyTelegramBotAPI groq


### 3. Configure the Bot
Open `bot.py` and replace:

TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # ← Replace this
GROQ_API_KEY = "YOUR_GROQ_API_KEY"  # ← Replace this


### 4. Run the Bot
```bash
python bot.py
```

## 🎯 Available Commands

| Command | Description |
|---------|-------------|
| `/start` | Welcome message and bot introduction |
| `/help` | Show help information and capabilities |
| `/quit` | End the conversation |

## 💬 Memory System

The bot has pre-programmed responses for personal questions:

| Category | Sample Questions | Example Responses |
|----------|-----------------|-------------------|
| **Name** | 
| **Age** | 
| **Location** | 
| **Creator** | 
| **Purpose** |
| **Mood** | 

## 🛠️ Project Structure

```
khode-ai-bot/
├── bot.py              # Main bot script
├── requirements.txt    # Dependencies (create with: pip freeze > requirements.txt)
└── README.md          # This file
```

## 📋 Dependencies
- `pyTelegramBotAPI` - Telegram bot framework
- `groq` - Groq API client
- `random` - Python standard library for random responses

## 🤖 How It Works

1. **Message Processing**: 
   - User sends a message to the bot
   - Bot checks if question matches memory categories
   - Returns random response from memory if match found
   - Otherwise, queries Groq's LLM for intelligent response

2. **Memory Matching**:
   - Converts user input to lowercase
   - Checks against keywords for each category
   - Returns random answer from the matched category

3. **LLM Fallback**:
   - If no memory match, uses Groq's Llama model
   - Processes through chat completion API
   - Returns generated response

## ⚠️ Error Handling
- API connection failures
- Invalid tokens
- Network issues
- Unexpected errors

## 🔧 Customization

### Add More Memory Categories
```python
MEMORY = {
    "new_category": [
        "Response 1",
        "Response 2",
        # Add more variations
    ]
}

KEYWORDS = {
    "new_category": ["keyword1", "keyword2", "keyword3"],
    # Add to existing categories
}
```

### Modify Responses
Edit the `MEMORY` dictionary to change:
- Response variations
- Add new categories
- Update existing answers

## 📝 License
MIT License - Feel free to modify and distribute

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📞 Support
For issues or questions:
1. Check the setup instructions
2. Verify your API keys are correct
3. Ensure all dependencies are installed
4. Check your internet connection

---

**Note**: Keep your API keys secure. Never commit them to public repositories. Use environment variables or configuration files in production.

---
*Made with ❤️ by Khode*
