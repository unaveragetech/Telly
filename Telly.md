# 📖 Telly Bot Documentation 📖

Welcome to the documentation for **Telly**, your friendly Telegram bot. This document will guide you through the setup, configuration, usage, and customization of Telly. Let's dive in!

---

## 📋 Table of Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Setup and Installation](#setup-and-installation)
4. [Configuration Files](#configuration-files)
   - [.env](#env)
   - [bot_config.json](#bot_configjson)
   - [responses.json](#responsesjson)
5. [Running the Bot](#running-the-bot)
6. [Available Commands](#available-commands)
7. [Customizing Responses](#customizing-responses)
8. [Managing the Environment](#managing-the-environment)
   - [Shutdown](#shutdown)
   - [Uninstall](#uninstall)
9. [Troubleshooting](#troubleshooting)
10. [FAQs](#faqs)
11. [Advanced Tips](#advanced-tips)

---

## 📢 Introduction

**Telly** is a customizable Telegram bot built using Python and the `telebot` library. Telly lives in a dedicated virtual environment, allowing you to run it independently of your system Python installation. Telly can respond to greetings, echo messages, and offer custom replies based on keywords. It also features optional infinite polling, allowing it to stay active 24/7.

---

## 🗂️ Project Structure

Upon downloading or cloning the repository, your directory should look like this:

```plaintext
bot_project/
├── .env                 # Environment variables for sensitive data like the bot token
├── bot.py               # Main bot script
├── bot_config.json      # Configuration file storing environment details and settings
├── init_env.py          # Script for environment setup and bot launch
├── responses.json       # JSON file for customizable responses
├── requirements.txt     # Python package requirements
└── Telly.md             # This documentation file
```

Each file plays an essential role in Telly’s operation, so be sure to keep the structure intact.

---

## 🚀 Setup and Installation

1. **Clone or Download the Project**

   First, get the files into a directory called `bot_project` or any other directory of your choice. Ensure the project structure is as shown above.

2. **Set Up Environment Variables**

   In the `.env` file, add your Telegram bot token (replace `your_bot_token_here` with your actual bot token):

   ```plaintext
   BOT_TOKEN=your_bot_token_here
   ```

3. **Install Dependencies**

   The script `init_env.py` will automatically set up a virtual environment and install dependencies. Simply run:

   ```bash
   python init_env.py
   ```

   This command:
   - Creates a virtual environment (if not already existing).
   - Installs required packages from `requirements.txt`.
   - Saves the environment’s name to `bot_config.json` for subsequent use.

---

## 🛠️ Configuration Files

### `.env`

The `.env` file holds sensitive environment variables such as the bot token. This file should look like:

```plaintext
BOT_TOKEN=your_bot_token_here
```

Replace `your_bot_token_here` with your actual Telegram bot token, available from the [BotFather](https://core.telegram.org/bots#botfather) on Telegram.

### `bot_config.json`

This configuration file, created on first run, holds environment settings. The file will look like this:

```json
{
  "environment_name": "telly_env",  // Virtual environment name
  "infinity_polling": true          // Set to true for continuous polling, false to disable
}
```

- **environment_name**: The name of Telly’s virtual environment.
- **infinity_polling**: Set to `true` if Telly should run indefinitely; set to `false` for single-session runs.

### `responses.json`

This file holds custom keywords and responses in a JSON format:

```json
{
  "greeting": "Hello! How can I assist you today?",
  "help": "I'm here to assist you with anything you need.",
  "weather": "Looks like a sunny day! But you might want to double-check."
}
```

In `responses.json`, define custom responses with keywords as keys and messages as values. When a message matches a keyword, Telly will reply with the corresponding response.

---

## ▶️ Running the Bot

To start Telly, simply run the following command in your terminal:

```bash
python init_env.py
```

- **First Run**: The script will prompt you to enter a name for the virtual environment. This name will be saved in `bot_config.json` for future runs.
- **Subsequent Runs**: Telly will automatically start within the same environment specified in `bot_config.json`.

---

## 📜 Available Commands

- **/start** and **/hello**: Telly will greet you with a welcome message.
- **Custom Keywords**: Any keyword specified in `responses.json` will trigger a custom response.
- **Echo Mode**: If no keyword is matched, Telly will echo the message back to you.

---

## 🎨 Customizing Responses

To add your own responses, edit `responses.json`:

1. Open `responses.json`.
2. Add new key-value pairs, where:
   - The **key** is the keyword Telly will recognize.
   - The **value** is the response Telly will send.

For example:

```json
{
  "joke": "Why did the bot cross the road? To send you this message!",
  "quote": "The only limit to our realization of tomorrow is our doubts of today."
}
```

---

## 🧹 Managing the Environment

### Shutdown

To gracefully stop Telly, use:

```bash
python init_env.py shutdown
```

This will terminate the bot without deleting any files or configurations.

### Uninstall

To fully remove the environment and reset Telly, run:

```bash
python init_env.py uninstall
```

This command:
- Deletes the virtual environment.
- Removes `bot_config.json`.
- Deletes the `.env` file to remove your bot token.

---

## 🛠️ Troubleshooting

### Common Issues

1. **Bot Not Responding**  
   Ensure your bot token is correct in the `.env` file, and that `BOT_TOKEN` matches exactly.

2. **Alias Parsing Errors in YAML**  
   This error may arise on GitHub if the README contains symbols that conflict with YAML. Try avoiding special characters or referring to the GitHub docs for alias parsing details.

3. **Environment Issues**  
   If Telly doesn’t recognize the virtual environment, run `init_env.py uninstall` and start fresh by re-running `init_env.py`.

---

## ❓ FAQs

**Q: How can I add multiple responses for the same keyword?**  
A: You can only add one response per keyword in `responses.json`. For variety, create similar keywords like “hello,” “hi,” and “hey,” each with a different response.

**Q: How do I switch Telly from infinite polling to one-time polling?**  
A: Open `bot_config.json` and set `"infinity_polling": false`. Telly will then respond once and stop.

**Q: What if I accidentally delete `bot_config.json`?**  
A: Just re-run `init_env.py`. A new `bot_config.json` will be created automatically.

---

## 🔧 Advanced Tips

- **Testing with Polling Off**  
   Set `"infinity_polling": false` in `bot_config.json` to make it easier to test single responses without Telly running continuously.

- **Environment Reset**  
   Use `python init_env.py uninstall` to quickly clean up and reset Telly’s environment if you run into issues.

- **Logging for Debugging**  
   Consider adding logging for debugging responses by using Python’s `logging` library in `bot.py`.

---

### 🎉 Thank You for Using Telly!

With these steps, Telly should be all set to bring some life to your Telegram chat. For additional help, feel free to consult this documentation or add comments in the code for your future self! Happy botting!
