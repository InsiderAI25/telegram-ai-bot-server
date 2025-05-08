from flask import Flask, request
import telegram
import asyncio

app = Flask(__name__)

# Updated Tokens and Chat IDs
MONIQUE_TOKEN = '8067661887:AAGL4vcZBI6E7avI72VPCGI2WLwJYsxJzlE'
COORDINATOR_TOKEN = '7719709224:AAHF5h3We8e8WdVHc6rh-MdtmWwlLhIgDH0'
MONIQUE_CHAT_ID = 1194534732
COORDINATOR_CHAT_ID = 1194534732

monique_bot = telegram.Bot(token=MONIQUE_TOKEN)
coordinator_bot = telegram.Bot(token=COORDINATOR_TOKEN)

@app.route('/vote', methods=['POST'])
def vote_handler():
    print("==== VOTE ROUTE STARTED ====")
    data = request.json
    decision = data.get("decision", "undecided")
    proposal = data.get("proposal", "Unnamed Proposal")
    print(f"Received proposal: {proposal}, decision: {decision}")

    try:
        asyncio.run(monique_bot.send_message(chat_id=MONIQUE_CHAT_ID, text=f"✅ Vote Received: {proposal} — {decision}"))
        print("✅ Monique message sent.")
    except Exception as e:
        print("❌ Monique failed:", e)

    try:
        asyncio.run(coordinator_bot.send_message(chat_id=COORDINATOR_CHAT_ID, text=f"📩 Vote Recorded: {proposal} — {decision}"))
        print("✅ Coordinator message sent.")
    except Exception as e:
        print("❌ Coordinator failed:", e)

    print("==== VOTE ROUTE ENDED ====")
    return {"status": "vote recorded"}, 200

@app.route('/')
def index():
    return "Telegram bot server (asyncio patched) is running.", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
