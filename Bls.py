import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram(text):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": text}, timeout=10)
        print("Telegram sent")
    except Exception as e:
        print(f"Telegram error: {e}")

print("Checking BLS Oran...")

# هنا لوجيك الفحص
try:
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get("https://algeria.blsspainglobal.com/Global/appointment", headers=headers, timeout=20)
    
    # كي يحل، البوت يبعث
    # بدل الشرط هذا بالفحص الحقيقي تاعك
    if r.status_code == 200 and "no appointment" not in r.text.lower():
        send_telegram("🔥 BLS ORAN حل! ادخل هنا: https://algeria.blsspainglobal.com")
    else:
        print("No slot")

    send_telegram("✅ Test: Bot Oran is working every 15min")

except Exception as e:
    print(e)
