🔍 Telegram Chat ID Finder

📬 Telegram Chat ID Finder, herhangi bir Telegram botunun eklendiği grup, kanal veya özel sohbetin chat_id bilgisini kolayca öğrenmek için tasarlanmış hafif ve pratik bir Python aracıdır.
Webhook, yetki veya modül eksikliği gibi yaygın hataları otomatik algılar ve seni en doğru çözüme yönlendirir.

🚀 Özellikler

✅ getUpdates API'si ile güvenli ve hızlı chat ID tespiti

✅ Webhook aktifse otomatik algılama ve kaldırma önerisi

✅ message, channel_post, my_chat_member gibi tüm update tiplerini destekler

✅ Sadece requests modülü ile çalışır – ekstra bağımlılık yok

✅ Grup, kanal ve özel sohbet türlerini ayırt edebilir

✅ Aynı anda birden fazla chat ID yakalayabilir

📦 Kurulum

💻 Python 3.10+ önerilir.
İlk olarak gerekli paketi kur:

pip install requests

⚙️ Kullanım Adımları

1️⃣ Bot’unu oluştur ve token’ı al: @BotFather

2️⃣ Botu hedef grup, kanal veya kullanıcıya ekle
3️⃣ Grupta bir mesaj gönder (örneğin /start)
4️⃣ Script’i çalıştır:

python chat_id_finder.py

5️⃣ Terminalde istendiğinde bot token’ını gir ve Enter’a bas
6️⃣ Aşağıdakine benzer bir sonuç göreceksin:

[✓] Bulundu → Chat: Systrack Bildirim Grubu | Chat ID: -1001945632871

🛠️ Örnek Çıktı

=== Telegram Chat ID Finder ===
[i] Bot kullanıcı adı: @MyAlertBot | id: 1234567890
[i] Webhook AYARLI DEĞİL (getUpdates kullanılabilir).

[✓] Bulundu → Chat: Systrack Bildirim Grubu | Chat ID: -1001945632871

🧠 Sık Karşılaşılan Sorunlar ve Çözümleri

🔁 KeyError: 'result'
➡️ Büyük olasılıkla webhook aktif. Script seni uyarır, deleteWebhook ile kaldırabilirsin.

🔑 401 Unauthorized
➡️ Token yanlış. getMe isteği başarısız olur. BotFather’dan yeni bir token oluştur.

📦 ModuleNotFoundError: No module named 'telegram'
➡️ Bu script python-telegram-bot kullanmaz. Sadece requests yeterlidir.

📜 Lisans

MIT License © 2025 Coosef 🛡️

💡 İpucu:

Chat ID’nin başında -100 varsa bu bir supergroup veya kanal’dır.

Pozitif sayı ise özel sohbet (private chat) anlamına gelir.
