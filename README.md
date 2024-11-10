---

# 📱 Telly the Telegram Bot 📱

*The friendliest bot to ever live in a virtual environment!* 🐍🤖

**[📖 Documentation](Telly.md)**

---

### 🛠️ Project Overview 🛠️

**Telly** is your customizable Telegram companion bot, always ready to respond with witty replies and do your bidding on command. Built to live in its own virtual bubble (environment), Telly can:

- 🎉 Reply to greetings like “/start” and “/hello” with a charming message.
- 🧠 Echo back anything you say (almost like a very polite parrot).
- 📬 Deliver custom responses based on keywords set in `responses.json`.
- 📲 Run indefinitely, or on a short leash, depending on your `infinity_polling` settings.

**Made with:**  
Python 🐍 + Telegram’s `telebot` API 🤖 + a sprinkle of humor 😄

---

## 🎩 Magic Setup Instructions 🎩

1. **🎬 Clone or Download the Project**

   Get the files into a cozy folder, `bot_project/`. Like this:

   ```
   bot_project/
   ├── .env
   ├── bot.py
   ├── bot_config.json
   ├── init_env.py
   ├── responses.json
   ├── requirements.txt
   └── Telly.md
   ```

2. **🛠️ Configure with Love**

   - **🔑 .env** — Securely stores your bot token. Fill it out like so:
     ```
     BOT_TOKEN=your_bot_token_here
     ```

   - **💬 responses.json** — Customize Telly’s wit! Add your responses here with keywords and corresponding replies. Perfect for those who want a sassy or helpful bot 🗣️.

   - **⚙️ bot_config.json** — *Automatically created* on your first run. Stores environment settings like `environment_name` and `infinity_polling`. You can adjust `infinity_polling` here if you like your bot more chill.

3. **📥 Install Dependencies Like a Pro**

   Run the `init_env.py` script, and it’ll handle everything. Or, if you’re a fan of DIY:

   ```bash
   pip install -r requirements.txt
   ```

4. **🚀 Launch Telly**

   Fire up `init_env.py` to initialize and start the bot! Telly will set up the virtual environment, install the goods, ask for an environment name, and jump into action:

   ```bash
   python init_env.py
   ```

5. **📴 Additional Commands**

   - **🛑 Shutdown Telly:**  
     Stop Telly in its tracks (if it’s being a bit *too* chatty):

     ```bash
     python init_env.py shutdown
     ```

   - **💥 Uninstall Everything:**  
     Remove Telly’s environment, configs, and token – *poof!* It’s like Telly was never there:

     ```bash
     python init_env.py uninstall
     ```

---

## 💻 Using Telly – A Joyful Experience 💻

- Type `/start` or `/hello` to see Telly’s cheerful welcome!  
- Send any other messages, and Telly will look up its response list to see if it has anything clever to say. If not, Telly’s polite enough to just echo what you said (no awkward silence here!).
  
Want more attitude? Just edit `responses.json` to add custom replies, jokes, or wisdom from Telly. 🧩

---

## ⚙️ Extra Customization

- **🗃️ Update `responses.json`** for more custom replies.
- **🔄 Change Polling Settings:** Modify `bot_config.json` to toggle `"infinity_polling"`. Infinite mode = Telly’s always on. Toggle it off if Telly needs some downtime.

---

## 📄 Notes and Handy Hints

- Telly can’t live without `.env`, `bot_config.json`, and `responses.json` – make sure they’re safe and sound in the project directory.
- Use the **`shutdown`** and **`uninstall`** commands for ultimate control over Telly’s environment. *Because a bot needs to know who’s boss.*

---

### 🌟 Special Thanks to You, Human

Without you, Telly would just be lines of code waiting to come alive. Thanks for letting Telly become the life of the virtual party! 🎉
