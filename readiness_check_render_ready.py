# readiness_check.py
import os
import time
import telegram
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load from environment
MONIQUE_TOKEN = os.getenv("MONIQUE_TOKEN")
COORDINATOR_TOKEN = os.getenv("COORDINATOR_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_check(bot, name):
    try:
        bot.send_message(chat_id=CHAT_ID, text=f"🔄 {name}, status check: Are you READY?")
        print(f"✅ {name} ping sent.")
    except Exception as e:
        print(f"❌ {name} failed: {e}")

def main():
    if not all([MONIQUE_TOKEN, COORDINATOR_TOKEN, CHAT_ID]):
        print("⚠️ One or more environment variables are missing. Please check .env or Render Environment Group.")
        return

    print("🚀 Running readiness check...")
    monique_bot = telegram.Bot(token=MONIQUE_TOKEN)
    coordinator_bot = telegram.Bot(token=COORDINATOR_TOKEN)

    send_check(monique_bot, "Monique AI")
    time.sleep(2)
    send_check(coordinator_bot, "Coordinator AI")
    print("✅ Readiness check complete.")

if __name__ == "__main__":
    main()
