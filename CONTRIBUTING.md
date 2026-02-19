# Katkıda Bulunma Rehberi

Bu projeye katkıda bulunmak istediğiniz için teşekkürler! 🎉

## 🤝 Nasıl Katkıda Bulunabilirim?

### 1. Yeni Alan Ekleme

Yeni bir alan (label) eklemek istiyorsanız:

1. Repository'yi fork edin
2. `.github/labels.json` dosyasını açın
3. `context` array'ine yeni alanı ekleyin
4. Değişiklikleri commit edin
5. Pull request oluşturun

**Örnek:**

```json
{
  "context": [
    "mobile",
    "backend",
    "frontend",
    "yeni-alan"  // Yeni eklenen alan
  ],
  ...
}
```

### 2. Şirket Ekleme

Yeni bir şirket eklemek istiyorsanız:

1. Repository'yi fork edin
2. `usefull_company.md` dosyasını açın
3. Şablonu kullanarak yeni şirket bilgilerini ekleyin
4. Değişiklikleri commit edin
5. Pull request oluşturun

**Şablon:**

```markdown
### [Şirket Adı]
- **Konum**: [Şehir]
- **Sektör**: [Yazılım/Finans/Otomotiv vb.]
- **Staj Dönemi**: [Yaz/Kış/Tüm Yıl]
- **Staj Süresi**: [Minimum-Maksimum gün/ay]
- **Başvuru Dönemi**: [Ay-Ay]
- **Başvuru Linki**: [Kariyer sayfası linki]
- **Staj Ücreti**: [Varsa belirtin / Belirtilmemiş]
- **Pozisyonlar**: 
  - [Pozisyon 1]
  - [Pozisyon 2]
- **Gereksinimler**:
  - [Gereksinim 1]
  - [Gereksinim 2]
- **Ek Bilgiler**: 
  - [Yemek/Ulaşım imkanı vb.]
```

### 3. Dokümantasyon İyileştirmeleri

Dokümantasyonu iyileştirmek için:

1. `docs/` klasöründeki dosyaları inceleyin
2. Eksik veya hatalı bilgileri düzeltin
3. Yeni bölümler ekleyin
4. Pull request oluşturun

### 4. Bug Düzeltmeleri

Bir hata bulduysanız:

1. Issue açarak hatayı bildirin
2. Hatayı düzeltmek için PR oluşturun
3. Değişikliklerinizi açıklayın

### 5. Yeni Özellikler

Yeni bir özellik önermek için:

1. Issue açarak özelliği açıklayın
2. Özelliği implement edin
3. Pull request oluşturun

## 📝 Pull Request Süreci

### PR Oluşturma Adımları:

1. **Fork**: Repository'yi fork edin
2. **Branch**: Yeni bir branch oluşturun
   ```bash
   git checkout -b feature/yeni-ozellik
   ```
3. **Değişiklikler**: Değişikliklerinizi yapın
4. **Commit**: Değişikliklerinizi commit edin
   ```bash
   git commit -m "feat: yeni özellik eklendi"
   ```
5. **Push**: Branch'inizi push edin
   ```bash
   git push origin feature/yeni-ozellik
   ```
6. **PR**: GitHub'da Pull Request oluşturun

### Commit Mesajları

Commit mesajlarınızı şu formatta yazın:

- `feat: yeni özellik eklendi`
- `fix: hata düzeltildi`
- `docs: dokümantasyon güncellendi`
- `refactor: kod refactor edildi`
- `test: test eklendi`

### PR Checklist

PR oluşturmadan önce kontrol edin:

- [ ] Kod çalışıyor mu?
- [ ] Testler geçiyor mu?
- [ ] Dokümantasyon güncellendi mi?
- [ ] Commit mesajları açıklayıcı mı?
- [ ] Kod formatı doğru mu?

## 🔍 Kod İnceleme Süreci

1. **Otomatik Kontrol**: GitHub Actions otomatik kontrolleri çalıştırır
2. **Review**: Repository owner PR'ı inceler
3. **Değişiklikler**: Gerekirse değişiklik istenir
4. **Onay**: PR onaylandıktan sonra merge edilir

## 🐛 Bug Bildirimi

Bir hata bulduysanız:

1. **Issue Açın**: Yeni bir issue oluşturun
2. **Açıklayın**: Hatayı detaylı olarak açıklayın
3. **Örnek Verin**: Mümkünse örnek verin
4. **Etiketleyin**: Uygun etiketleri ekleyin

## 💡 Öneriler

- Kod yazarken açıklayıcı yorumlar ekleyin
- Değişikliklerinizi test edin
- Dokümantasyonu güncel tutun
- Diğer katkıda bulunanlara saygılı olun

## 📞 İletişim

Sorularınız için:

- Issue açabilirsiniz
- Repository maintainer'ına ulaşabilirsiniz

## 🙏 Teşekkürler

Katkılarınız için teşekkürler! Her katkı bu projeyi daha iyi hale getiriyor. 🚀
