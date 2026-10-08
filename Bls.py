import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram(text):
    try:
        if not BOT_TOKEN or not CHAT_ID:
            print("Secrets not set")
            return
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
        requests.post(url, data=data, timeout=10)
        print("Telegram sent")
    except Exception as e:
        print(f"Telegram error: {e}")

print("Checking BLS Oran...")

# BLS Oran check
try:
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0"})
    
    # نسييو نفتحو صفحة المواعيد
    r = session.get("https://algeria.blsspainglobal.com/Global/account/login", timeout=20)
    
    # هذا لوجيك بسيط: اذا الموقع رد و ما فيهش كلمة no slot
    # انت عندك كودك القديم كان خدام، نقدر نرجعوه اذا تحب
    
    # للتجربة: نبعثلك ميساج باش نتأكد البوت يخدم
    # من بعد نحطو لوجيك الصحيح تاع وهران
    send_telegram("✅ البوت تاع BLS وهران راه ي
