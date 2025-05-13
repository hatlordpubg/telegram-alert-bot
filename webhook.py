from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("8142894136:AAFhHB9Su8C2qRnzGTBpXDzo3oAaPqctISs")
CHAT_ID = os.getenv("CHAT_ID")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data.get("message", "🚨 Yeni bir sinyal var!")
    
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    
    response = requests.post(telegram_url, json=payload)
    return {"status": "sent"}, response.status_code

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
