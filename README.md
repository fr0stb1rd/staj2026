
# 💻 Staj 2026

Zorunlu staj ihtiyacı olan öğrenci arkadaşların kendini tanıtabileceği, plan yapabileceği ve staj fırsatlarına ulaşabileceği yer. **Odak: öğrencileri öne çıkarmak ve planlama.**


<img src="./images/1714633070470.jpeg" alt="staj2024"  height="100">

## 📪 Staj Başvurusu

- Repoda bulunan **Issues** alanına tıklanır.
- Bu alandan **New Issue** butonuna basılır.
- **"Staj Başvuru Formu"** seçilir ve içindeki boş alanlar doldurulur.
- Burada format **şu şekilde olmak zorundadır**:  
  **AD-SOYAD [ALAN][STAJ YERİ][STAJ TİPİ][STAJ SÜRESİ]**
  
- **Alan** kısmı şu bilgilerden birini veya birden fazlasını içerebilir:  
  `["mobile", "backend", "computer-vision", "frontend", "devops", "pm", "qa", "game", "data-science", "data-analyst", "database", "embedded", "cyber-security", "blockchain", "system", "networking", "hardware", "sap-abap"]`
  
- **Staj Yeri** için şu seçeneklerden biri belirtilmelidir:  
  `["uzaktan", "yüzyüze"]`
  
- **Staj Tipi** için şu seçeneklerden biri belirtilmelidir:  
  `["zorunlu", "gönüllü"]`
  
- **Staj Süresi** için şu seçeneklerden biri belirtilmelidir:  
  `["4-hafta", "6-hafta", "8-hafta"]`
  
- Bu bilgiler dışında başka bir format kabul edilmemektedir. Örneklere bakarak birden fazla giriş yapabilirsiniz.

- **Formata uygun olmayan başlıklar otomatik olarak kapatılacaktır. Tekrar açılması için başlığı güncellemeniz yeterli olacaktır.**

> Yeni eklemeler duruma göre olacaktır. Önerisi olan label.json içinde ekleyip pr da atabilir.

## 📍 Örnek başvuru başlıkları

```yaml
Veli Bacik [pm,qa][uzaktan][zorunlu][4-hafta]
Veli Bacik [mobile,backend][uzaktan][zorunlu][4-hafta]
Veli Bacik [uzaktan][mobile,backend][zorunlu][4-hafta]
Veli Bacik [pm,qa][mobile,backend][zorunlu][4-hafta]
Veli Bacik4 [mobile,backend][uzaktan,zorunlu][yüzyüze][4-hafta,6-hafta]
Veli Bacik 3 [mobile][gönüllü][zorunlu,yüzyüze][4-hafta,6-hafta]
Veli Bacik 2 [mobile][uzaktan,gönüllü][zorunlu,yüzyüze][4-hafta]
Veli Bacik [pm,qa,data-science][uzaktan][zorunlu][4-hafta]
```

## 📚 Dokümantasyon

- [Adaylar İçin Detaylı Rehber](docs/applicant-guide.md) – Başvuru süreci ve format kuralları
- [Deploy ve Test Rehberi](docs/TESTING.md) – GitHub’a deploy sonrası workflow’ları test etmek için adımlar
- [Katkıda Bulunma](CONTRIBUTING.md) – Projeye nasıl katkıda bulunabilirsiniz

*Şirket başvuru akışı şu an pasif; gerektiğinde tekrar açılabilir.*

## 🤝 Katkıda Bulunma

### 📝 Yeni bir alan eklemek istersem ne yapmalıyım?

- Repo'dan bir clone alınır.
- Bu alanın içinde label.json içinde yer alan context ile aynı şekilde label tanımlamaları yapılır.
- Bu değişiklikler commit edilir.
- Pull request oluşturulur.
- Pull request kabul edilir.
- Yeni bir alan eklenecektir otomatik olarak.

### 📝 Staj fırsatları (şirket listesi) eklemek istersem ne yapmalıyım?

- Repo'dan bir clone alınır.
- [Staj fırsatları olan şirketler](usefull_company.md) açılır ve yeni şirket şablonu okunur.
- Bu şablona uygun şirketlerin bilgileri eklenir.
- Değişiklikler commit edilir, pull request oluşturulur.
- PR kabul edildikten sonra listeye eklenir. *(Şirket tarafı otomasyonu şu an pasif.)*

## ✨ Öğrencileri Öne Çıkarma ve Planlama

### 📊 Otomatik İstatistikler
- Her gün istatistikler güncellenir
- En çok tercih edilen alanlar, lokasyonlar ve staj tipleri README’de görünür

### 📅 Haftalık Özetler
- Her Pazartesi otomatik haftalık özet (yeni başvurular, trendler)
- Issues’da `weekly-summary` etiketi ile bulunur

### ✅ Gelişmiş Validasyon
- Başvuru formatı kontrolü, detaylı hata mesajları ve örnekler
- Doğru formatta başvuranlar otomatik etiketlenir

## 📊 İstatistikler
**Toplam Başvuru:** 126
**Son 24 Saat:** 5 başvuru
**Bu Hafta:** 31 başvuru
**Bu Ay:** 125 başvuru

### 🎯 En Çok Tercih Edilen Alanlar
1. **backend**: 84 başvuru (66.7%)
2. **data-science**: 62 başvuru (49.2%)
3. **mobile**: 49 başvuru (38.9%)
4. **data-analyst**: 47 başvuru (37.3%)
5. **database**: 44 başvuru (34.9%)
6. **frontend**: 42 başvuru (33.3%)
7. **system**: 20 başvuru (15.9%)
8. **networking**: 16 başvuru (12.7%)
9. **embedded**: 13 başvuru (10.3%)
10. **cyber-security**: 13 başvuru (10.3%)

### 📍 Staj Yeri Tercihleri
- **yüzyüze**: 113 başvuru (89.7%)
- **uzaktan**: 85 başvuru (67.5%)

### 🎓 Staj Tipi Dağılımı
- **zorunlu**: 90 başvuru (71.4%)
- **gönüllü**: 28 başvuru (22.2%)
- **zorunlu,gönüllü**: 4 başvuru (3.2%)
- **zorunlu, gönüllü**: 2 başvuru (1.6%)
- **gönüllü, zorunlu**: 1 başvuru (0.8%)

### ⏱️ Staj Süresi Tercihleri
- **4-hafta**: 87 başvuru (69.0%)
- **8-hafta**: 62 başvuru (49.2%)
- **6-hafta**: 61 başvuru (48.4%)
- **[4-hafta**: 1 başvuru (0.8%)

*Son güncelleme: 06.03.2026 04:06*
## FAQ

#### Yeni issue açıyorum ama hemen kapanıyor ne yapsam oluşturamadım. Ne yapmalıyım?

- Bu durumun sebebi, issue formatının doğru olmamasıdır.(Noktalama işaretleri, boşluklar, kelimelerin doğru yazılması gibi)
- Lütfen issue formatını kontrol ediniz.
- Örnekleri inceleyebilirsiniz.

#### Formata uygun yapmazsam ne olur?

Açılan **issue**, formata uygun değilse otomatik olarak kapanacaktır.

#### Gönüllü staj yapmak istiyorum, başvurabilir miyim?

Evet, başvurabilirsiniz. Ancak önceliğimiz daima **zorunlu staj** yapması gereken arkadaşlar olacaktır.

#### Uzun dönem staj yapmak istiyorum ama alanlarda göremedim. Ne yapmalıyım? (3 veya 6 ay)
  Burada daha çok yaz dönemi stajını hedefliyoruz. Ondan dolayı uzun dönem staj yer almayacak. Ek olarak staj dönemleri bittiğinde repo kapatılıp tüm bilgiler silinecektir.

#### İyi bir repom yok, bu bir sorun mu?

Öğrencilik döneminde olmamanız bir sorun değil. Ancak henüz zaman varken, bir alanda örnek bir repo hazırlamak çok değerli olacaktır. Bu noktada, [https://www.uplabs.com/](https://www.uplabs.com/) gibi platformlardan bir tasarım seçip, ister **backend**, ister **mobil**, isterseniz **frontend/web** olarak kodlayabilirsiniz.

Bu yazı bu konuda yardımcı olacaktır: [ilk-adımını-at-ekip-çalışmasıyla-proje-geliştirme-rehberi](https://medium.com/@vbacik-10/i̇lk-adımını-at-ekip-çalışmasıyla-proje-geliştirme-rehberi-1a794972e724)



# Geçmiş Dönemler

## 2025 
Yaklaşık 500+ arkadaşa bu repo ile bir imkan sağlamıştık. (Kapatılan)
https://www.linkedin.com/feed/update/urn:li:activity:7312058541031264256/

## 2024 
Yaklaşık 300+ arkadaşa bu repo ile bir imkan sağlamıştık. (Kapatılan)
https://www.linkedin.com/feed/update/urn:li:activity:7191692371082854401/

## 2023

Yaklaşık 100+ arkadaşa bu repo ile bir imkan sağlamıştık.
https://www.linkedin.com/posts/veli-bacik-345978a9_github-vb102023-staj-2023-yaz-d%C3%B6nemi-activity-7066365173573312512-xtiO/


## Authors

- [@vb10](https://www.github.com/vb10)

## Screenshots


<img src="https://media.licdn.com/dms/image/v2/D4D22AQGmeTbvkROM7w/feedshare-shrink_2048_1536/feedshare-shrink_2048_1536/0/1714633072814?e=1741219200&v=beta&t=PGRQmLQczAKP4HECfFq-iaJa6ipeeLplq0uFLTJoXHo" alt="staj2024" width="500" height="375">
