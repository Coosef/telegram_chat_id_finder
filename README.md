🔍 Telegram Chat ID Finder

📬 Telegram Chat ID Finder, herhangi bir Telegram botunun eklendiği grup, kanal veya özel sohbetin chat_id bilgisini saniyeler içinde öğrenmeni sağlayan, tamamen açık kaynaklı ve hafif bir Python aracıdır.
Webhook çakışmaları, yetki hataları veya eksik modüller gibi yaygın problemleri otomatik olarak tespit eder ve çözüm önerileri sunar. Basit terminal arayüzü sayesinde teknik bilgin az olsa bile rahatlıkla kullanabilirsin.

✨ Temel Özellikler

✅ getUpdates API’si ile güvenli ve hızlı chat ID tespiti
✅ Webhook aktifse otomatik algılama ve tek tuşla kaldırma önerisi
✅ message, channel_post, my_chat_member gibi tüm Telegram update tiplerini destekler
✅ Ekstra bağımlılık gerekmez – yalnızca requests modülü yeterlidir
✅ Grup, kanal ve özel sohbet türlerini ayırt eder
✅ Aynı anda birden fazla chat ID yakalayabilir

📦 Kurulum

📌 Python 3.10+ önerilir.
İlk olarak gerekli paketi yükle:

pip install requests

⚙️ Kullanım Adımları

1️⃣ Bot’unu oluştur ve token’ı al → @BotFather üzerinden yeni bir bot oluştur.
2️⃣ Botu hedef grup, kanal veya kullanıcıya ekle.
3️⃣ Grupta bir mesaj gönder (örneğin /start).
4️⃣ Script’i çalıştır:

python chat_id_finder.py

5️⃣ Terminalde istendiğinde bot token’ını gir ve Enter’a bas.
6️⃣ Aşağıdakine benzer bir sonuç görüntülenecektir:

[✓] Bulundu → Chat: Coosef Bildirim Grubu | Chat ID: -1001548632189

🛠️ Örnek Çıktı

=== Telegram Chat ID Finder ===
[i] Bot kullanıcı adı: @MyAlertBot | id: 1234567890
[i] Webhook AYARLI DEĞİL (getUpdates kullanılabilir).

[✓] Bulundu → Chat: Coosef Bildirim Grubu | Chat ID: -1001548632189

🧠 Sık Karşılaşılan Sorunlar ve Çözümler

⚠️ KeyError: 'result'
👉 Sebep: Büyük ihtimalle webhook aktif.
✅ Çözüm: Script seni uyarır, deleteWebhook ile webhook’u kaldır.

🔑 401 Unauthorized
👉 Sebep: Token yanlış.
✅ Çözüm: BotFather’dan yeni bir token oluştur.

📦 ModuleNotFoundError: No module named 'telegram'
👉 Sebep: python-telegram-bot kurulu değil.
✅ Çözüm: Gerek yok, bu script sadece requests ile çalışır.

📜 Lisans

MIT License © 2025 Coosef 🛡️
Bu proje tamamen açık kaynaklıdır. Dilediğin gibi kullanabilir, değiştirebilir ve geliştirebilirsin.

💡 İpuçları

Chat ID’nin başında -100 varsa bu bir supergroup veya kanal’dır.

Pozitif sayı ise bu bir özel sohbet (private chat) anlamına gelir.

Webhook açıkken getUpdates kullanılamaz; script bunu otomatik algılar ve kaldırmanı ister.

🤝 Katkıda Bulunma

Projeyi geliştirmek istersen, pull request açabilir veya önerilerini “Issues” sekmesinden paylaşabilirsin.
Yeni özellik fikirleri ve hata bildirimleri her zaman değerlidir 🚀

🌟 Neden Kullanmalı?

✔️ Telegram otomasyon projelerinde hızlı testler için idealdir
✔️ Bot entegrasyonu öncesinde chat ID tespiti zahmetsiz olur
✔️ API yanıtlarını manuel kontrol etmene gerek kalmaz
✔️ Geliştirici dostu sade terminal arayüzüyle vakit kazandırır
