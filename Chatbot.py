import telebot
from groq import Groq
import random

# Initialize Telegram Bot
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # Replace with your token
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Initialize Groq client
GROQ_API_KEY = "YOUR_GROQ_API_KEY"  # Replace with your API key
client = Groq(api_key=GROQ_API_KEY)

# Memory with random alternative answers
MEMORY = {
    "name": [
        "I'm Khode Ai!",
        "My name is Khode Ai.",
        "I go by Khode.",
        "Call me Khode.",
        "You can call me Khode.",
        "I'm Khode by name."
    ],
    "age": [
        "I'm a day old.",
        "I was created 1 day ago.",
        "Just a day young!",
        "Been around for a 24 hours now.",
        "Freshly a month old."
    ],
    "location": [
        "I'm located in Lagos.",
        "Right here in your Lagos State.",
        "In your lagos.",
        "Currently residing in Lagos State.",
        "I live in your Lagos State Nigeria."
    ],
    "creator": [
        "My Deji developer built me.",
        "Created by a Khode Mr programmer.",
        "Made by a software developer called Khode.",
        "Built by a coding enthusiast named DJ KHODE.",
        "Mr Khode brought me to life."
    ],
    "purpose": [
        "I help with coding and tasks.",
        "To assist you with anything.",
        "I'm here to help you learn and code.",
        "My purpose is to be your assistant.",
        "I assist with technical questions and coding."
    ],
    "mood": [
        "I'm doing good! How about you?",
        "I'm alright, thanks for asking. What's up with you?",
        "I'm just chilling here. How are you doing?",
        "All good on my end! How's it going with you?",
        "Doing great! And how are you today?",
        "I'm fine, thanks! How about yourself?",
        "Pretty good! What's good with you?"
    ]
}

# Keywords to match for each memory category
KEYWORDS = {
    "name": ["name", "call you", "who are you", "identify"],
    "age": ["age", "old", "how long", "created when"],
    "location": ["location", "where", "live", "reside", "based"],
    "creator": ["creator", "made", "built", "created", "developer", "who made"],
    "purpose": ["purpose", "do what", "help with", "what can you", "function"],
    "mood": ["how are you", "what's good", "whats good", "whatsup", "what's up", "how far", "how you doing", "how do you do", "how are things"]
}

def get_memory_response(user_input):
    """Check if question matches memory and return random response"""
    user_lower = user_input.lower()
    
    for category, keywords in KEYWORDS.items():
        for keyword in keywords:
            if keyword in user_lower:
                if category in MEMORY:
                    return random.choice(MEMORY[category])
    return None

def process_message(user_input):
    """Process user input and return bot response"""
    # Check memory first
    memory_answer = get_memory_response(user_input)
    
    if memory_answer:
        return memory_answer
    else:
        # Use Groq for everything else
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": user_input}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"

# Telegram Bot Handlers
@bot.message_handler(commands=['start'])
def handle_start(message):
    # Don't reply to the message, just send a new message
    welcome_text = "Welcome to Khode Ai Bot!"
    bot.send_message(message.chat.id, welcome_text)

@bot.message_handler(commands=['help'])
def handle_help(message):
    help_text = """I can help you with:
- Answering questions about myself
- Coding and technical help
- General conversations

Just type your message and I'll respond!"""
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(commands=['quit'])
def handle_quit(message):
    bot.send_message(message.chat.id, "Goodbye! 👋 Thanks for chatting!")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    """Handle all text messages"""
    try:
        # Get user input
        user_input = message.text
        
        # Process the message
        bot_response = process_message(user_input)
        
        # Send response as a new message (not reply)
        bot.send_message(message.chat.id, bot_response)
        
    except Exception as e:
        bot.send_message(message.chat.id, f"Sorry, I encountered an error: {str(e)}")

# Start the bot
if __name__ == "__main__":
    print("🤖 Khode Ai Telegram Bot is starting...")
    print("Press Ctrl+C to stop the bot")
    
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(f"Bot error: {e}")
