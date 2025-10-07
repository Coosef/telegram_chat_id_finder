🔍 Telegram Chat ID Finder

📬 Telegram Chat ID Finder, herhangi bir Telegram botunun eklendiği grup, kanal veya özel sohbetin chat_id bilgisini kolayca öğrenmek için tasarlanmış hafif bir Python aracıdır.
Webhook, bot yetkisi veya modül eksikliği gibi yaygın hataları otomatik algılar ve sana en doğru yönlendirmeyi yapar.

🚀 Özellikler

getUpdates API'si ile güvenli şekilde chat ID yakalar

Webhook aktifse algılar ve kaldırma seçeneği sunar

message, channel_post, my_chat_member gibi tüm update tiplerini destekler

Komut satırında kolay kullanım – ekstra modül gerekmez (requests dışında)

Grup, kanal ve özel sohbetleri ayırt eder

Anlık olarak birden fazla chat ID yakalayabilir

📦 Kurulum

Python 3.10+ önerilir.
Öncelikle requests modülünü kur:

pip install requests

⚙️ Kullanım

Bot’unu oluştur ve token’ı al: @BotFather

Botu hedef grup / kanal / kullanıcıya ekle

Grupta bir mesaj gönder (/start olabilir)

Script’i çalıştır:

pip install requests

python chat_id_finder.py

Terminalde istendiğinde bot token’ını gir ve Enter’a bas

Ekranda aşağıdakine benzer bir sonuç göreceksin:

[✓] Bulundu → Chat: Systrack Bildirim Grubu | Chat ID: -1001945632871

🛠️ Örnek Çıktı

=== Telegram Chat ID Finder ===
[i] Bot kullanıcı adı: @MyAlertBot | id: 1234567890
[i] Webhook AYARLI DEĞİL (getUpdates kullanılabilir).

[✓] Bulundu → Chat: Systrack Bildirim Grubu | Chat ID: -1001945632871

🧠 Sık Karşılaşılan Sorunlar

KeyError: 'result'
→ Büyük olasılıkla webhook aktif. Script seni zaten uyarır, deleteWebhook ile kaldırabilirsin.

401 Unauthorized
→ Token yanlış. getMe isteği başarısız olur. BotFather’dan yeni token oluştur.

ModuleNotFoundError: No module named 'telegram'
→ Bu script python-telegram-bot kullanmaz. Sadece requests yeterlidir.

📜 Lisans

MIT License © 2025 Coosef 🛡️

💡 İpucu: Chat ID’nin başında -100 varsa bu bir supergroup veya kanal’dır.
Pozitif sayı ise özel sohbet (private chat) anlamına gelir.
