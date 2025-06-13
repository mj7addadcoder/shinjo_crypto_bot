import requests
import time
import os
import telegram

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

bot = telegram.Bot(token=TOKEN)

print("🚀 Shinjo Crypto Bot is now running...")  # ✅ رسالة ترحيبية في اللوق

def get_price(symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data[symbol]['usd']

last_btc_price = 0
last_eth_price = 0

while True:
    try:
        btc_price = get_price("bitcoin")
        eth_price = get_price("ethereum")

        if abs(btc_price - last_btc_price) > 20:
            bot.send_message(chat_id=CHAT_ID, text=f"📉 BTC Price Alert: ${btc_price}")
            last_btc_price = btc_price

        if abs(eth_price - last_eth_price) > 10:
            bot.send_message(chat_id=CHAT_ID, text=f"📉 ETH Price Alert: ${eth_price}")
            last_eth_price = eth_price

        time.sleep(60)
    except Exception as e:
        print(f"❌ Error: {e}")
        time.sleep(60)
