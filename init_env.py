import os
import sys
import json
import subprocess
from dotenv import load_dotenv

ENV_DIR = "bot_env"  # Environment directory name
CONFIG_FILE = "bot_config.json"
REQUIREMENTS_FILE = "requirements.txt"

def create_environment():
    """Create a virtual environment and install requirements."""
    if not os.path.exists(ENV_DIR):
        subprocess.run([sys.executable, "-m", "venv", ENV_DIR])
        print(f"Environment '{ENV_DIR}' created.")
    install_requirements()

def install_requirements():
    """Install required packages in the virtual environment."""
    subprocess.run([f"{ENV_DIR}/bin/pip", "install", "-r", REQUIREMENTS_FILE])
    print("Requirements installed.")

def load_or_create_config():
    """Load config if exists or prompt for environment name and create config."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE) as config_file:
            config = json.load(config_file)
    else:
        environment_name = input("Enter environment name: ")
        config = {
            "environment_name": environment_name,
            "infinity_polling": True
        }
        with open(CONFIG_FILE, "w") as config_file:
            json.dump(config, config_file, indent=4)
        print(f"Configuration saved with environment name: {environment_name}")
    return config

def run_bot():
    """Run the bot inside the virtual environment."""
    print("Starting bot...")
    subprocess.run([f"{ENV_DIR}/bin/python", "bot.py"])

def shutdown_bot():
    """Stop the bot if it's running."""
    print("Shutting down bot (if running).")

def uninstall_environment():
    """Delete the virtual environment and configuration files."""
    if os.path.exists(ENV_DIR):
        subprocess.run(["rm", "-rf", ENV_DIR])
        print(f"Environment '{ENV_DIR}' uninstalled.")
    if os.path.exists(CONFIG_FILE):
        os.remove(CONFIG_FILE)
        print("Configuration file removed.")
    if os.path.exists(".env"):
        os.remove(".env")
        print(".env file removed.")

def main():
    load_dotenv()  # Load .env variables
    
    if "uninstall" in sys.argv:
        uninstall_environment()
    elif "shutdown" in sys.argv:
        shutdown_bot()
    else:
        create_environment()
        config = load_or_create_config()
        run_bot()

if __name__ == "__main__":
    main()
