from flask import Flask, request
import telegram

app = Flask(__name__)

# Tokens and chat IDs
MONIQUE_TOKEN = '8067661887:AAF16gmBxzmUqlxams4dWvJlUsco2ncgVQ'
COORDINATOR_TOKEN = '7719709224:AAEDjFDCUY6E8zLl8IXZlImulDEpdND-UiQ'

MONIQUE_CHAT_ID = 1194534732
COORDINATOR_CHAT_ID = 1194534732

# Bot clients
monique_bot = telegram.Bot(token=MONIQUE_TOKEN)
coordinator_bot = telegram.Bot(token=COORDINATOR_TOKEN)

@app.route('/vote', methods=['POST'])
def vote_handler():
    data = request.json
    decision = data.get("decision", "undecided")
    proposal = data.get("proposal", "Unnamed Proposal")

    try:
        monique_bot.send_message(chat_id=MONIQUE_CHAT_ID, text=f"✅ Vote Received: {proposal} — {decision}")
        print("✅ Monique message sent.")
    except Exception as e:
        print("❌ Monique failed:", e)

    try:
        coordinator_bot.send_message(chat_id=COORDINATOR_CHAT_ID, text=f"📩 Vote Recorded: {proposal} — {decision}")
        print("✅ Coordinator message sent.")
    except Exception as e:
        print("❌ Coordinator failed:", e)

    return {"status": "vote recorded"}, 200

@app.route('/report', methods=['POST'])
def report_handler():
    data = request.json
    report = data.get("summary", "No summary provided")

    try:
        monique_bot.send_message(chat_id=MONIQUE_CHAT_ID, text=f"📊 CFO Report: {report}")
        print("✅ Monique report sent.")
    except Exception as e:
        print("❌ Monique report failed:", e)

    try:
        coordinator_bot.send_message(chat_id=COORDINATOR_CHAT_ID, text=f"📊 CFO Report Sent: {report}")
        print("✅ Coordinator report sent.")
    except Exception as e:
        print("❌ Coordinator report failed:", e)

    return {"status": "report sent"}, 200

@app.route('/audit', methods=['GET'])
def audit_trigger():
    try:
        monique_bot.send_message(chat_id=MONIQUE_CHAT_ID, text="🛡️ System audit triggered.")
        print("✅ Audit message sent.")
    except Exception as e:
        print("❌ Audit failed:", e)
    return {"status": "audit notification sent"}, 200

@app.route('/')
def index():
    return "Telegram bot server (synchronous version) is running.", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
