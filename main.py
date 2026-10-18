
from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
from openai import OpenAI
import sys

import openai

# Load environment variables
load_dotenv()

# OpenRouter API configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Validate API keys
if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY is missing from .env")

if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is missing from .env")

# Initialize OpenRouter client
client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


class Reference:
    """
    A class to store the previous response
    from the OpenRouter API.
    """

    def __init__(self) -> None:
        self.response = ""


reference = Reference()

# Select an available OpenRouter model
model_name = "openai/gpt-4o-mini"



# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dispatcher = Dispatcher(bot)



def clear_past():
    """A function to clear the previous conversation and context.
    """
    reference.response = ""



@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    A handler to clear the previous conversation and context.
    """
    clear_past()
    await message.reply("I've cleared the past conversation and context.")



@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """
    This handler receives messages with `/start` or  `/help `command
    """
    await message.reply("Hi\nI am Tele Bot!\Created by Ebratul. How can i assist you?")


@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    """
    A handler to display the help menu.
    """
    help_command = """
    Hi There, I'm Telegram bot created by Ebratul! Please follow these commands - 
    /start - to start the conversation
    /clear - to clear the past conversation and context.
    /help - to get this help menu.
    I hope this helps. :)
    """
    await message.reply(help_command)






@dispatcher.message_handler()
async def chatgpt(message: types.Message):
    """Generate a response using OpenRouter."""
    if not message.text:
        return

    print(f">>> USER: {message.text}")

    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful AI assistant. "
                        "Answer the user's questions clearly."
                    ),
                },
                {
                    "role": "user",
                    "content": message.text,
                },
            ],
        )

        answer = response.choices[0].message.content

        if not answer:
            answer = "Sorry, the AI returned an empty response."

        reference.response = answer

        print(f">>> AI: {answer}")
        await message.reply(answer)

    except Exception as e:
        print(f"OpenRouter API error: {type(e).__name__}: {e}")
        await message.reply(
            "Sorry, I couldn't generate a response. "
            "Please check the terminal for the error."
        )


if __name__ == "__main__":
    print("Telegram bot is starting...")
    executor.start_polling(dispatcher, skip_updates=True)