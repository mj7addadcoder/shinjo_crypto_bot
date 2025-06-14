from datetime import datetime
import requests
import telegram
import os
import time

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
bot = telegram.Bot(token=TOKEN)

# الإعدادات العامة
PAIR = "bitcoin"
SYMBOL = "BTCUSD"
RISK_MODE = "سكالبينج"
TP1_OFFSET = 50    # بالدولار
TP2_OFFSET = 90
SL_OFFSET = 70

def get_price():
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={PAIR}&vs_currencies=usd"
    data = requests.get(url).json()
    return data[PAIR]['usd']

while True:
    try:
        current_price = get_price()
        tp1 = round(current_price + TP1_OFFSET, 2)
        tp2 = round(current_price + TP2_OFFSET, 2)
        sl = round(current_price - SL_OFFSET, 2)
        now = datetime.now().strftime('%Y-%m-%d %H:%M')

        message = f"""🚨 توصية سكالب لحظية – Shinjo Signals
🕰 التوقيت: {now}
💱 الزوج: {SYMBOL}
💰 السعر الحالي: ${current_price}
🎯 الهدف 1: ${tp1}
🎯 الهدف 2: ${tp2}
🛑 وقف الخسارة: ${sl}
📊 نوع الصفقة: شراء ({RISK_MODE})
⚙️ Shinjo Crypto V2 Bot – بث مباشر
"""

        bot.send_message(chat_id=CHAT_ID, text=message)
        time.sleep(3600)  # كل ساعة توصية جديدة
    except Exception as e:
        print("❌ Error:", e)
        time.sleep(120)
