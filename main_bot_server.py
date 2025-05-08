from flask import Flask, request
import telegram
import os

app = Flask(__name__)

# Telegram bot tokens
MONIQUE_TOKEN = '8067661887:AAF16gmBxzmUqlxqams4dVwlUScou2ncgVQ'
COORDINATOR_TOKEN = '7719709224:AAEDjFDCUY6E8zLl8IXZlImulDEpdND-UiQ'

# Bot instances
monique_bot = telegram.Bot(token=MONIQUE_TOKEN)
coordinator_bot = telegram.Bot(token=COORDINATOR_TOKEN)

# Shared routes for Monique and Coordinator AI
@app.route('/vote', methods=['POST'])
def vote_handler():
    data = request.json
    decision = data.get("decision", "undecided")
    proposal = data.get("proposal", "Unnamed Proposal")
    monique_bot.send_message(chat_id=1194534732, text=f"Vote Received: {proposal} — {decision}")
    coordinator_bot.send_message(chat_id="@COORDINATOR_AI_BOT", text=f"Vote Recorded: {proposal} — {decision}")
    return {"status": "vote recorded"}, 200

@app.route('/report', methods=['POST'])
def report_handler():
    report = data.get("summary", "No summary provided")
    monique_bot.send_message(chat_id="@MONIQUEADMINISTOR_BOT", text=f"CFO Report: {report}")
    coordinator_bot.send_message(chat_id="@COORDINATOR_AI_BOT", text=f"CFO Report Sent: {report}")
    return {"status": "report sent"}, 200

@app.route('/audit', methods=['GET'])
def audit_trigger():
    monique_bot.send_message(chat_id="@MONIQUEADMINISTOR_BOT", text="System audit triggered.")
    return {"status": "audit notification sent"}, 200

@app.route('/')
def index():
    return "Telegram bot server for Monique and Coordinator AI is running.", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
