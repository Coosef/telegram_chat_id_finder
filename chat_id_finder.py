# chat_id_finder.py
import requests
import sys
import time

API_BASE = "https://api.telegram.org"

def api_call(token: str, method: str, params: dict | None = None):
    url = f"{API_BASE}/bot{token}/{method}"
    try:
        r = requests.get(url, params=params, timeout=20)
        data = r.json()
    except Exception as e:
        print(f"[!] HTTP/JSON hata: {e}")
        sys.exit(1)

    # Hata yakalama (ok:false ise)
    if not isinstance(data, dict) or not data.get("ok", False):
        print(f"[!] API Hatası: {data}")
        return None
    return data

def get_me(token: str):
    data = api_call(token, "getMe")
    if not data:
        print("[!] Token doğrulanamadı. Lütfen BOT TOKEN’ını kontrol et.")
        sys.exit(1)
    me = data.get("result", {})
    print(f"[i] Bot kullanıcı adı: @{me.get('username')} | id: {me.get('id')}")
    return me

def get_webhook_info(token: str):
    data = api_call(token, "getWebhookInfo")
    if not data:
        return None
    info = data.get("result", {})
    if info.get("url"):
        print(f"[i] Webhook aktif: {info.get('url')}")
        print("    getUpdates kullanmak için webhook’u kapatmak gerekir (Conflict 409 hatası alırsın).")
    else:
        print("[i] Webhook AYARLI DEĞİL (getUpdates kullanılabilir).")
    return info

def delete_webhook(token: str):
    data = api_call(token, "deleteWebhook", params={"drop_pending_updates": False})
    if data:
        print("[✓] Webhook kapatıldı.")
    else:
        print("[!] Webhook kapatılamadı.")

def get_updates(token: str, offset: int | None = None):
    params = {"timeout": 2}
    if offset is not None:
        params["offset"] = offset
    # Burada ok:false durumunda None döner, üstte kontrol var
    resp = api_call(token, "getUpdates", params=params)
    if not resp:
        return []
    return resp.get("result", [])

def extract_chat_from_update(update: dict) -> tuple[int | None, str | None]:
    """
    update tipine göre chat bilgisi çıkarır.
    Dönen: (chat_id, chat_title_or_username)
    """
    # message
    msg = update.get("message")
    if msg and "chat" in msg:
        c = msg["chat"]
        return c.get("id"), c.get("title") or c.get("username")

    # edited_message
    em = update.get("edited_message")
    if em and "chat" in em:
        c = em["chat"]
        return c.get("id"), c.get("title") or c.get("username")

    # channel_post
    cp = update.get("channel_post")
    if cp and "chat" in cp:
        c = cp["chat"]
        return c.get("id"), c.get("title") or c.get("username")

    # edited_channel_post
    ecp = update.get("edited_channel_post")
    if ecp and "chat" in ecp:
        c = ecp["chat"]
        return c.get("id"), c.get("title") or c.get("username")

    # my_chat_member / chat_member / message_reaction vb.
    for key in ("my_chat_member", "chat_member", "message_reaction", "message_reaction_count"):
        section = update.get(key)
        if section and isinstance(section, dict):
            c = section.get("chat")
            if c:
                return c.get("id"), c.get("title") or c.get("username")

    return None, None

def main():
    print("=== Telegram Chat ID Finder ===")
    token = input("Bot token’ını gir: ").strip()
    if not token or ":" not in token:
        print("[!] Geçersiz token.")
        sys.exit(1)

    # 1) Token doğrula
    get_me(token)

    # 2) Webhook durumu kontrol et
    info = get_webhook_info(token)
    if info and info.get("url"):
        yn = input("Webhook aktif. Kapatılsın mı? (y/N): ").strip().lower()
        if yn == "y":
            delete_webhook(token)
            time.sleep(1)

    print("\n[?] Şimdi botu hedef gruba/kanala ekle ve grupta bir mesaj yaz (/start gibi).")
    input("[Enter] yaptıktan sonra getUpdates ile çekiyorum...")

    # 3) Updates al, chat id’leri topla
    seen_ids = set()
    last_update_id = None
    attempts = 3
    for i in range(attempts):
        updates = get_updates(token, offset=last_update_id + 1 if last_update_id else None)
        if not updates:
            print(f"[i] Deneme {i+1}/{attempts}: yeni update yok. 2 saniye bekleniyor...")
            time.sleep(2)
            continue

        for u in updates:
            last_update_id = max(last_update_id or 0, u.get("update_id", 0))
            chat_id, title = extract_chat_from_update(u)
            if chat_id is not None and chat_id not in seen_ids:
                seen_ids.add(chat_id)
                label = title or "Private/Unknown"
                print(f"[✓] Bulundu → Chat: {label} | Chat ID: {chat_id}")

        # yeni update gelebilir, kısa bir bekleme
        time.sleep(1)

    if not seen_ids:
        print("\n[!] Hiç chat bulunamadı.")
        print("   • Botu gruba/kanala eklediğinden ve grupta yeni bir mesaj oluştuğundan emin ol.")
        print("   • Token doğru mu? (401 Unauthorized olabilir)")
        print("   • Webhook kapalı mı? (409 Conflict olursa getUpdates çalışmaz)")

if __name__ == "__main__":
    main()
