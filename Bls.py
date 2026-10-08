import requests

print("Checking BLS Oran...")

url = "https://algeria.blsspainglobal.com/Global/blsAppointment"

headers = {"User-Agent": "Mozilla/5.0"}

try:
    r = requests.get(url, headers=headers, timeout=20)
    print(f"Status: {r.status_code}")
    if "No appointment" in r.text or "not available" in r.text.lower():
        print("مازال مغلوق - وهران")
    else:
        print("!!! كاين حاجة جديدة، شوف الموقع بسرعة !!!")
    # تقدر تخلي 300 سطر هنا ما يبلوكيش
    print(r.text[:500])
except Exception as e:
    print(f"Error: {e}")
