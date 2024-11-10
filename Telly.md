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
