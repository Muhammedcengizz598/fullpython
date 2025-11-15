# 🤝 Katkıda Bulunma Rehberi

Öncelikle, Full Python projesine katkıda bulunmak istediğiniz için teşekkür ederiz! Bu rehber, projeye nasıl katkıda bulunabileceğinizi açıklamaktadır.

## 📋 İçindekiler

- [Davranış Kuralları](#davranış-kuralları)
- [Başlamadan Önce](#başlamadan-önce)
- [Katkı Türleri](#katkı-türleri)
- [Geliştirme Süreci](#geliştirme-süreci)
- [Kod Standartları](#kod-standartları)
- [Commit Mesajları](#commit-mesajları)
- [Pull Request Süreci](#pull-request-süreci)

---

## 😊 Davranış Kuralları

Bu proje ve katılımcıları aşağıdaki davranış kurallarına uymaktadır:

- **Saygılı olun** - Tüm katılımcılara saygı gösterin
- **Yapıcı olun** - Eleştiriler yapıcı ve yardımcı olmalıdır
- **Kapsayıcı olun** - Farklı görüşleri ve deneyimleri değerlendirin
- **Profesyonel olun** - Profesyonel bir ortam sağlayın

---

## 🚀 Başlamadan Önce

### 1. Depoyu Fork Edin
GitHub'da projenin sağ üst köşesindeki "Fork" butonuna tıklayın.

### 2. Lokal Klonlayın
```bash
git clone https://github.com/YOUR_USERNAME/fullpython.git
cd fullpython
```

### 3. Upstream Ekleyin
```bash
git remote add upstream https://github.com/Muhammedcengizz598/fullpython.git
```

### 4. Sanal Ortam Oluşturun
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# veya
venv\Scripts\activate  # Windows
```

### 5. Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

---

## 🎯 Katkı Türleri

### 🐛 Hata Raporlama
Bir hata bulduysanız:

1. **Kontrol Edin** - Hata zaten raporlanmış mı?
2. **Detay Verin** - Hatanın nasıl oluştuğunu açıklayın
3. **Örnek Verin** - Tekrarlanabilir bir örnek sağlayın
4. **Ortam Bilgisi** - Python versiyonu, OS vb. belirtin

### ✨ Yeni Özellik Önerisi
Yeni bir özellik önermek için:

1. **Başlık** - Açık ve kısa bir başlık
2. **Açıklama** - Özelliğin ne olduğunu açıklayın
3. **Kullanım Durumu** - Neden gerekli olduğunu belirtin
4. **Alternatifler** - Başka çözümleri düşündünüz mü?

### 📚 Dokümantasyon İyileştirmesi
Dokümantasyon iyileştirmeleri her zaman hoş karşılanır:

- Yazım hatalarını düzeltin
- Açıklamaları iyileştirin
- Örnekler ekleyin
- Çeviriler yapın

### 💻 Kod Katkıları
Kod katkıları için aşağıdaki adımları izleyin.

---

## 🔧 Geliştirme Süreci

### 1. Issue Oluşturun veya Seçin
- Yeni bir özellik için issue oluşturun
- Mevcut bir issue'yu seçin
- Maintainer'dan onay alın

### 2. Feature Branch Oluşturun
```bash
git checkout -b feature/konu-adi
# veya
git checkout -b fix/hata-adi
```

### 3. Değişiklikleri Yapın
- Kod yazın
- Testler ekleyin
- Dokümantasyon güncelleyin

### 4. Testleri Çalıştırın
```bash
python manage.py test
```

### 5. Değişiklikleri Commit Edin
```bash
git add .
git commit -m "Açıklayıcı commit mesajı"
```

### 6. Branch'i Push Edin
```bash
git push origin feature/konu-adi
```

### 7. Pull Request Açın
GitHub'da Pull Request oluşturun.

---

## 📝 Kod Standartları

### Python Kodu
- **PEP 8** standartlarını izleyin
- **4 boşluk** indentation kullanın
- **Anlamlı değişken isimleri** kullanın
- **Docstring** ekleyin

```python
def python_giriş(request):
    """
    Python giriş sayfasını render eder.
    
    Args:
        request: HTTP request nesnesi
        
    Returns:
        Rendered template response
    """
    return render(request, 'python_giriş.html')
```

### HTML/CSS
- **Semantic HTML** kullanın
- **CSS class isimleri** anlamlı olmalı
- **Responsive tasarım** sağlayın
- **Accessibility** göz önünde bulundurun

### Türkçe İçerik
- **Tutarlı terminoloji** kullanın
- **Profesyonel dil** kullanın
- **Yazım kurallarına** uyun

---

## 💬 Commit Mesajları

### Format
```
[Tür] Kısa açıklama

Detaylı açıklama (opsiyonel)

Closes #123
```

### Türler
- `feat:` - Yeni özellik
- `fix:` - Hata düzeltmesi
- `docs:` - Dokümantasyon
- `style:` - Kod stili (formatting)
- `refactor:` - Kod yeniden yapılandırması
- `test:` - Test ekleme/düzeltme
- `chore:` - Diğer değişiklikler

### Örnekler
```
feat: Python decorators konusu eklendi

fix: Sayfanın responsive tasarımı düzeltildi

docs: README.md güncellendi

refactor: Views.py fonksiyonları optimize edildi
```

---

## 🔄 Pull Request Süreci

### PR Açmadan Önce
- [ ] Upstream'den güncel kodu çekin
- [ ] Testleri çalıştırın
- [ ] Kod standartlarını kontrol edin
- [ ] Dokümantasyonu güncelleyin

### PR Açarken
```markdown
## Açıklama
Bu PR'de ne yapıldığını açıklayın.

## Tür
- [ ] Hata düzeltmesi
- [ ] Yeni özellik
- [ ] Dokümantasyon
- [ ] Diğer

## İlgili Issue
Closes #123

## Değişiklikler
- Değişiklik 1
- Değişiklik 2

## Test Edildi
- [ ] Lokal olarak test edildi
- [ ] Tüm testler geçti
```

### PR Sonrası
- Geri bildirimleri bekleyin
- Gerekli değişiklikleri yapın
- Tekrar push edin
- Onay bekleyin

---

## 🎓 Yardımcı Kaynaklar

- [Django Dokümantasyonu](https://docs.djangoproject.com/)
- [Python PEP 8](https://www.python.org/dev/peps/pep-0008/)
- [Git Rehberi](https://git-scm.com/doc)
- [GitHub Rehberi](https://guides.github.com/)

---

## ❓ Sorularınız mı var?

- GitHub Issues'de soru sorun
- Discussions'da tartışın
- Email ile iletişime geçin

---

<div align="center">

**Katkılarınız için teşekkür ederiz! 🙏**

</div>
