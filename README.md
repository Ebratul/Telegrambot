# Telegram AI Bot 🤖

A Telegram chatbot powered by the OpenRouter API and Python. This bot allows users to interact with an AI model directly through Telegram.

## ✨ Features

- **AI-powered conversations:** Get AI-generated responses to text messages.
- **OpenRouter integration:** Connect to AI models through the OpenRouter API.
- **Start command:** Use `/start` to start interacting with the bot.
- **Help command:** Use `/help` to view available commands.
- **Clear command:** Use `/clear` to clear the stored conversation context.
- **Environment variables:** Store API keys and bot credentials securely in a `.env` file.
- **Error handling:** Display helpful feedback when an API request fails.

## 🛠️ Tech Stack

- **Language:** Python 3.11
- **Telegram Bot Framework:** aiogram 2.25.1
- **AI API Client:** OpenAI Python SDK
- **AI Provider:** OpenRouter
- **Configuration:** python-dotenv

## 📁 Project Structure

```text
Telegrambot/
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── research/
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Ebratul/Telegrambot.git
cd Telegrambot
```

### 2. Create a Conda environment

```bash
conda create -n telegrambot python=3.11 pip -y
conda activate telegrambot
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
OPENROUTER_API_KEY=your_openrouter_api_key
```

- Create a Telegram bot using [@BotFather](https://t.me/BotFather).
- Obtain an API key from [OpenRouter](https://openrouter.ai/keys).
- Ensure your selected model is available to your OpenRouter account.

**Security:** Never commit your `.env` file or expose your API keys publicly.

### 5. Run the bot

```bash
python main.py
```

Once the bot starts successfully, open your bot in Telegram and send a message.

## 💬 Available Commands

| Command | Description |
|---|---|
| `/start` | Start the bot and receive a welcome message |
| `/help` | Display available commands |
| `/clear` | Clear the stored conversation context |

## ⚙️ Configuration

The bot reads its credentials from environment variables:

| Variable | Purpose |
|---|---|
| `TELEGRAM_BOT_TOKEN` | Authenticates your Telegram bot |
| `OPENROUTER_API_KEY` | Authenticates API requests to OpenRouter |

The AI model is configured in `main.py`. Change `model_name` to another model supported by your OpenRouter account if needed.

## 🔒 Security

- Keep API keys and Telegram tokens private.
- Exclude `.env` from Git using `.gitignore`.
- Use `.env.example` to document required environment variables without including real credentials.
- Rotate any credentials accidentally exposed in a public repository.

## 🧪 Troubleshooting

**Missing environment variable**

Check that `.env` exists in the project root and contains both required variables.

**Telegram polling conflict**

The same bot token should not be used by multiple simultaneous `getUpdates` polling processes. Stop duplicate bot instances before restarting.

**OpenRouter API error**

Verify your API key, model availability, account credits, and API access.

**Missing Python dependencies**

Activate the correct Conda environment and run:

```bash
python -m pip install -r requirements.txt
```

## 👨‍💻 Author

**Ebratul Shaharier**

- GitHub: [@Ebratul](https://github.com/Ebratul)

## 📄 License

No license has been specified yet. Add a `LICENSE` file if you want to distribute this project under an open-source license.
