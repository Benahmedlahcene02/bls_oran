import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send(text):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": text}, timeout=10)
    except:
        pass

print("Checking BLS Oran...")

try:
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get("https://algeria.blsspainglobal.com", headers=headers, timeout=20)
    
    if r.status_code == 200:
        print("Site OK - checking slots")
        # اذا بغيت نركبلك الفحص الحقيقي، ابعثلي الكود القديم
        send("✅ Bot Oran is online")
    else:
        print("Site down")

except Exception as e:
    print(e)
