# Telly Bot

Telly Bot is a customizable Telegram bot that can respond to specific messages with predefined responses, set up in a virtual environment with easy setup and management.

## Features

- Responds to greetings and other commands using a custom response list.
- Configurable environment setup that remembers settings for future runs.
- Simple shutdown and uninstall commands for full environment management.
- Runs indefinitely in polling mode or can be set to non-infinite polling.

## Setup Instructions

1. **Clone or Download the Project**
   
   Ensure all files are in the `bot_project/` directory structure as shown.

2. **Configuration**

   - `.env`: Holds sensitive bot information. Enter your bot token:
     ```plaintext
     BOT_TOKEN=your_bot_token_here
     ```
   - `responses.json`: Customize bot responses by editing this file with message-response pairs.
   - `bot_config.json`: Generated automatically on first run. Stores environment name and polling preferences.

3. **Install Dependencies**

   The `init_env.py` script will handle dependency installation. Alternatively, you can install manually:
   ```bash
   pip install -r requirements.txt
Run the Bot
Run init_env.py to initialize the bot for the first time. This script will create a virtual environment, install dependencies, prompt for environment name, and run the bot.
```
python init_env.py
```
Additional Commands
```
Shutdown: Stop the bot if it’s running.
python init_env.py shutdown
```
```
Uninstall: Completely remove the environment, config, and .env files.
python init_env.py uninstall
```
Bot Usage

Start the bot with /start or /hello.
Any other messages will be matched against responses.json and replied to with the corresponding response. If no match is found, the bot will simply echo the message.
Customization

Modify Responses: Edit responses.json to add or change responses.

Change Polling Settings(diable bot): Open bot_config.json and modify "infinity_polling" as needed.
Notes

Ensure .env, bot_config.json, and responses.json are present in the project directory for proper functionality.
Use shutdown and uninstall commands for controlled environment management.
Happy botting!


---

### Summary

With all files in place, you now have:
1. An environment initialization script (`init_env.py`) for setting up, running, shutting down, and uninstalling the bot.
2. A `.env` file to store sensitive tokens securely.
3. Configurable response and settings files (`responses.json` and `bot_config.json`).
4. Detailed usage instructions in `Telly.md`.

