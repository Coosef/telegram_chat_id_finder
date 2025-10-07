*TR
🔍 Telegram Chat ID Finder

📬 Telegram Chat ID Finder, herhangi bir Telegram botunun eklendiği grup, kanal veya özel sohbetin chat_id bilgisini saniyeler içinde öğrenmeni sağlayan, tamamen açık kaynaklı ve hafif bir Python aracıdır.
Webhook çakışmaları, yetki hataları veya eksik modüller gibi yaygın problemleri otomatik olarak tespit eder ve çözüm önerileri sunar. Basit terminal arayüzü sayesinde teknik bilgin az olsa bile kolayca kullanabilirsin.

🚀 Temel Özellikler

✅ getUpdates API’si ile güvenli ve hızlı chat ID tespiti

✅ Webhook aktifse otomatik algılama ve tek tuşla kaldırma önerisi

✅ message, channel_post, my_chat_member gibi tüm update tiplerini destekler

✅ Ekstra bağımlılık gerekmez – yalnızca requests modülü yeterlidir

✅ Grup, kanal ve özel sohbet türlerini ayırt eder

✅ Aynı anda birden fazla chat ID yakalayabilir

📦 Kurulum

Python 3.10+ önerilir.
Öncelikle gerekli paketi yükle:

pip install requests

⚙️ Kullanım Adımları

Bot’unu oluştur ve token’ı al → @BotFather üzerinden yeni bir bot oluştur.

Botu hedef grup, kanal veya kullanıcıya ekle.

Grupta bir mesaj gönder (örneğin /start).

Script’i çalıştır:

python chat_id_finder.py

Terminalde istendiğinde bot token’ını gir ve Enter’a bas.

Aşağıdakine benzer bir sonuç görüntülenecektir:

[✓] Bulundu → Chat: Bildirim Kanalı | Chat ID: -1001945632871

🛠️ Örnek Çıktı

=== Telegram Chat ID Finder ===
[i] Bot kullanıcı adı: @MyBot | id: 1234567890
[i] Webhook AYARLI DEĞİL (getUpdates kullanılabilir).

[✓] Bulundu → Chat: Bildirim Kanalı | Chat ID: -1001945632871

🧠 Sık Karşılaşılan Sorunlar ve Çözümler

⚠️ KeyError: 'result'
Sebep: Büyük ihtimalle webhook aktif.
Çözüm: Script seni uyarır, deleteWebhook ile webhook’u kaldır.

🔑 401 Unauthorized
Sebep: Token yanlış.
Çözüm: BotFather’dan yeni bir token oluştur.

📦 ModuleNotFoundError: No module named 'telegram'
Sebep: python-telegram-bot kurulu değil.
Çözüm: Gerek yok, script sadece requests ile çalışır.

📜 Lisans

MIT License © 2025 Coosef
Bu proje tamamen açık kaynaklıdır. Dilediğin gibi kullanabilir, değiştirebilir ve geliştirebilirsin.

💡 İpuçları

Chat ID’nin başında “-100” varsa bu bir supergroup veya kanal’dır.

Pozitif sayı ise bu bir özel sohbet (private chat) anlamına gelir.

Webhook açıkken getUpdates kullanılamaz; script bunu otomatik algılar ve kaldırmanı ister.

*EN

🔍 Telegram Chat ID Finder

📬 Telegram Chat ID Finder is a lightweight and open-source Python tool designed to quickly retrieve the chat_id of any group, channel, or private chat where your Telegram bot is added.
It automatically detects common issues such as webhook conflicts, authorization errors, or missing modules and provides helpful guidance. With its simple terminal interface, even users with minimal technical experience can use it easily.

🚀 Key Features

✅ Secure and fast chat ID detection using the getUpdates API

✅ Automatically detects active webhooks and suggests removal

✅ Supports all update types including message, channel_post, and my_chat_member

✅ No extra dependencies required – only the requests module is needed

✅ Differentiates between group, channel, and private chats

✅ Can capture multiple chat IDs in a single run

📦 Installation

Python 3.10+ is recommended.
First, install the required package:

pip install requests

⚙️ Usage Guide

Create your bot and get its token via @BotFather
.

Add the bot to your target group, channel, or private chat.

Send a message in that chat (e.g., /start).

Run the script:

python chat_id_finder.py

Enter your bot token when prompted and press Enter.

You’ll see an output similar to this:

[✓] Found → Chat: Notification Channel | Chat ID: -1001945632871

🛠️ Example Output

=== Telegram Chat ID Finder ===
[i] Bot username: @MyBot | id: 1234567890
[i] Webhook is NOT set (getUpdates available).

[✓] Found → Chat: Notification Channel | Chat ID: -1001945632871

🧠 Common Issues and Solutions

⚠️ KeyError: 'result'
Cause: A webhook is likely still active.
Solution: The script will notify you — remove the webhook using deleteWebhook.

🔑 401 Unauthorized
Cause: Invalid bot token.
Solution: Generate a new token via BotFather.

📦 ModuleNotFoundError: No module named 'telegram'
Cause: python-telegram-bot is not installed.
Solution: Not required — this script works with only the requests module.

📜 License

MIT License © 2025 Coosef
This project is fully open-source. You are free to use, modify, and distribute it.

💡 Tips

If the chat ID starts with -100, it belongs to a supergroup or channel.

A positive number means it's a private chat.

If a webhook is active, getUpdates cannot be used. The script will detect this and guide you.


