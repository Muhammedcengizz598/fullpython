# 🐍 Full Python - Kapsamlı Python Öğrenme Platformu

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-5.2-darkgreen?style=flat-square&logo=django)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

**Python programlama dilinin tüm konularını kapsamlı bir şekilde öğrenebileceğiniz interaktif web platformu**

[Özellikleri](#-özellikler) • [Kurulum](#-kurulum) • [Kullanım](#-kullanım) • [Konular](#-konular) • [Katkıda Bulunun](#-katkıda-bulunun)

</div>

---

## 📋 İçindekiler

- [Proje Hakkında](#-proje-hakkında)
- [Özellikler](#-özellikler)
- [Teknoloji Stack](#-teknoloji-stack)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Proje Yapısı](#-proje-yapısı)
- [Konular](#-konular)
- [Ekran Görüntüleri](#-ekran-görüntüleri)
- [Katkıda Bulunun](#-katkıda-bulunun)
- [Lisans](#-lisans)
- [İletişim](#-iletişim)

---

##  Proje Hakkında

**Full Python**, Python programlama dilini sıfırdan başlayarak ileri seviyelere kadar öğrenebileceğiniz kapsamlı bir web platformudur. Django framework'ü kullanılarak geliştirilmiş bu proje, 25+ farklı Python konusunu detaylı açıklamalar ve örneklerle sunmaktadır.

Proje, hem başlangıç seviyesi öğrenenler hem de ileri seviye geliştiriciler için uygun içerik barındırmaktadır.

---

## ✨ Özellikler

- ✅ **25+ Kapsamlı Konu** - Python'un temel ve ileri konuları
- ✅ **Türkçe İçerik** - Tüm açıklamalar Türkçe olarak sunulmuştur
- ✅ **Responsive Tasarım** - Tüm cihazlarda uyumlu arayüz
- ✅ **Kolay Navigasyon** - Konular arasında hızlı geçiş
- ✅ **Pratik Örnekler** - Her konu için gerçek dünya örnekleri
- ✅ **Hızlı Yükleme** - Optimize edilmiş performans
- ✅ **Modern UI** - Kullanıcı dostu arayüz tasarımı

---

## 🛠️ Teknoloji Stack

| Teknoloji | Versiyon | Kullanım |
|-----------|---------|---------|
| **Python** | 3.x | Backend programlama dili |
| **Django** | 5.2 | Web framework |
| **SQLite** | 3.x | Veritabanı |
| **HTML5** | - | Markup |
| **CSS3** | - | Styling |
| **JavaScript** | ES6+ | Frontend interaktivitesi |

---

## 📦 Kurulum

### Ön Gereksinimler

- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)
- Git

### Adım Adım Kurulum

1. **Depoyu Klonlayın**
```bash
git clone https://github.com/Muhammedcengizz598/fullpython.git
cd fullpython
```

2. **Sanal Ortam Oluşturun (Önerilir)**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Gerekli Paketleri Yükleyin**
```bash
pip install -r requirements.txt
```

4. **Veritabanı Migrasyonlarını Uygulayın**
```bash
python manage.py migrate
```

5. **Geliştirme Sunucusunu Başlatın**
```bash
python manage.py runserver
```

6. **Tarayıcıda Açın**
```
http://localhost:8000
```

---

## 🚀 Kullanım

### Temel Komutlar

```bash
# Sunucuyu başlat
python manage.py runserver

# Sunucuyu belirli port'ta başlat
python manage.py runserver 8080

# Admin paneline erişim (superuser oluştur)
python manage.py createsuperuser

# Admin paneli
http://localhost:8000/admin

# Statik dosyaları topla (production için)
python manage.py collectstatic
```

### Navigasyon

- **Ana Sayfa**: `/` - Tüm konuların listesi
- **Konular**: `/python/[konu-adı]` - Belirli bir konunun detayları

---

## 📁 Proje Yapısı

```
fullpython/
├── fullpython/                 # Proje konfigürasyonu
│   ├── settings.py            # Django ayarları
│   ├── urls.py                # Ana URL yönlendirmesi
│   ├── wsgi.py                # WSGI konfigürasyonu
│   └── asgi.py                # ASGI konfigürasyonu
│
├── python_app/                # Ana uygulama
│   ├── migrations/            # Veritabanı migrasyonları
│   ├── templates/             # HTML şablonları (25+ sayfa)
│   ├── static/                # Statik dosyalar (CSS, JS, resimler)
│   ├── views.py               # View fonksiyonları
│   ├── urls.py                # Uygulama URL'leri
│   ├── models.py              # Veritabanı modelleri
│   ├── admin.py               # Admin konfigürasyonu
│   └── apps.py                # Uygulama konfigürasyonu
│
├── templates/                 # Genel şablonlar
├── static/                    # Genel statik dosyalar
├── db.sqlite3                 # SQLite veritabanı
├── manage.py                  # Django yönetim aracı
├── requirements.txt           # Proje bağımlılıkları
└── README.md                  # Bu dosya
```

---

## 📚 Konular

Platform aşağıdaki Python konularını kapsamaktadır:

### Temel Konular
- 🔹 **Giriş** - Python'a başlangıç
- 🔹 **Değişkenler** - Veri türleri ve değişken tanımlama
- 🔹 **Operatörler** - Aritmetik, karşılaştırma ve mantıksal operatörler
- 🔹 **If-Else** - Koşullu ifadeler
- 🔹 **Döngüler** - For ve While döngüleri
- 🔹 **Girdi İşlemleri** - Kullanıcı girdisi alma

### Veri Yapıları
- 🔹 **String** - Metin işlemleri
- 🔹 **Listeler** - Liste veri yapısı
- 🔹 **Tüpleler** - Tuple veri yapısı
- 🔹 **Sözlükler** - Dictionary veri yapısı
- 🔹 **Türeçler** - Set veri yapısı

### Fonksiyonlar ve İleri Konular
- 🔹 **Fonksiyonlar** - Fonksiyon tanımlama ve kullanma
- 🔹 **Args/Kwargs** - Değişken sayıda argümanlar
- 🔹 **Decorators** - Dekoratörler
- 🔹 **Jeneratörler** - Generator fonksiyonları

### Nesne Yönelimli Programlama
- 🔹 **OOP** - Sınıflar ve nesneler
- 🔹 **Metaclass** - Metaclass'lar
- 🔹 **Context Managers** - Context yöneticileri

### Dosya ve Hata Yönetimi
- 🔹 **Dosya İşlemleri** - Dosya okuma/yazma
- 🔹 **Hata Yakalama** - Exception handling
- 🔹 **Yorum Satırları** - Kod yorumları

### İleri Konular
- 🔹 **Time** - Zaman işlemleri
- 🔹 **Eşzamanlılık** - Threading ve Async
- 🔹 **Sanal Ortamlar** - Virtual environments
- 🔹 **Düzenli İfadeler** - Regex
- 🔹 **Web Scraping** - Web verisi çekme
- 🔹 **API** - API geliştirme
- 🔹 **Testing** - Unit testing

---

## 🎨 Ekran Görüntüleri

### Ana Sayfa
Tüm Python konularının listelendiği ana sayfa, kullanıcı dostu bir arayüz sunmaktadır.

### Konu Sayfaları
Her konu sayfası detaylı açıklamalar, kod örnekleri ve pratik bilgiler içermektedir.

---

## 🤝 Katkıda Bulunun

Bu projeyi geliştirmek için katkılarınızı bekliyoruz! Aşağıdaki adımları izleyerek katkıda bulunabilirsiniz:

### Katkı Adımları

1. **Depoyu Fork Edin**
```bash
git clone https://github.com/Muhammedcengizz598/fullpython.git
```

2. **Feature Branch Oluşturun**
```bash
git checkout -b feature/YeniOzellik
```

3. **Değişiklikleri Commit Edin**
```bash
git commit -m "Yeni özellik: Açıklama"
```

4. **Branch'i Push Edin**
```bash
git push origin feature/YeniOzellik
```

5. **Pull Request Açın**
   - GitHub'da Pull Request oluşturun
   - Değişikliklerinizi açıklayın
   - Onay bekleyin

### Katkı Kuralları

- Kod stil tutarlılığını sağlayın
- Yorum satırları ekleyin
- Türkçe içerik kullanın
- Responsive tasarım sağlayın

---

## 📝 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakınız.

```
MIT License

Copyright (c) 2024 Muhammet Cengiz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 📧 İletişim

**Muhammet Cengiz**

- 🔗 GitHub: [@Muhammedcengizz598](https://github.com/Muhammedcengizz598)
- 📧 Email: [E-posta adresiniz]
- 💼 LinkedIn: [LinkedIn profiliniz]

---

## 🙏 Teşekkürler

Bu projeyi destekleyen ve katkıda bulunan herkese teşekkür ederiz!

---

<div align="center">

**⭐ Eğer bu proje size yardımcı olduysa, lütfen bir yıldız verin!**

Made with ❤️ by [Muhammet Cengiz](https://github.com/Muhammedcengizz598)

</div>
