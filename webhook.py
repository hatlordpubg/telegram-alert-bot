from flask import Flask, request
import requests

app = Flask(__name__)

# Telegram Bot ayarları
TELEGRAM_BOT_TOKEN = '8142894136:AAFhHB9Su8C2qRnzGTBpXDzo3oAaPqctISs'
TELEGRAM_CHAT_ID = '-4757109683'

def send_to_telegram(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    requests.post(url, json=payload)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        if request.content_type == 'application/json':
            data = request.get_json()
            message = data.get('message', 'TradingView JSON Webhook!')
        elif request.content_type == 'text/plain':
            message = request.data.decode('utf-8')
        else:
            message = '⚠️ Bilinmeyen veri formatı alındı.'

        print("Gelen mesaj:", message)
        send_to_telegram(message)
        return 'OK', 200
    except Exception as e:
        print("Hata oluştu:", e)
        return 'Error', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
