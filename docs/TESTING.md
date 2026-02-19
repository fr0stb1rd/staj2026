# Deploy ve Test Rehberi

Repoyu kendi GitHub hesabına push ettikten sonra workflow'ların doğru çalıştığını bu adımlarla kontrol edebilirsin.

---

## 1. Issue Title Check (Staj Başvuru Formatı)

**Ne zaman çalışır:** Bir issue açıldığında veya başlığı düzenlendiğinde.

### Test 1 – Doğru format (başarılı)

1. **Issues** → **New Issue** → **Staj Başvuru Formu** seç.
2. Başlığı şu formatta yaz (adı kendi adınla değiştir):
   ```
   Test Kullanici [backend,frontend][uzaktan][zorunlu][4-hafta]
   ```
3. Formu doldur, **Submit new issue** tıkla.

**Beklenen:**
- Workflow **Automatic Issue Labeler** Actions’ta yeşil (başarılı) biter.
- Issue’ya `backend`, `frontend`, `uzaktan`, `zorunlu`, `4-hafta` label’ları eklenir.
- Sen assignee olarak atanırsın.
- Bir yorumda “staj başvurun başarı ile taglendi” benzeri mesaj görünür.

### Test 2 – Yanlış format (hata mesajı + kapanma)

1. Yeni issue aç, başlığı yanlış yaz, örn.:
   ```
   Test Kullanici backend uzaktan zorunlu
   ```
   (köşeli parantez yok)

**Beklenen:**
- Workflow yine çalışır.
- Issue’ya “Format Hatası” ile ilgili detaylı bir yorum gelir.
- Issue **closed** olur.
- Başlığı doğru formata çevirip **Reopen** edersen, tekrar açılır ve doğru formatta ise etiketlenir.

---

## 2. Sync Labels

**Ne zaman çalışır:** `main`’e push (özellikle `.github/labels.json` değişince) veya **Run workflow** ile manuel.

### Test

1. **Actions** → **Sync Labels** workflow’unu seç.
2. **Run workflow** → **Run workflow** (branch: main).

**Beklenen:**
- Job yeşil biter.
- Repo **Labels** sayfasında `labels.json`’daki etiketlerin (mobile, backend, uzaktan, zorunlu, 4-hafta vb.) tanımlı olduğunu kontrol et.

İstersen `labels.json`’a geçici bir label ekleyip push ederek de tetikleyebilirsin; merge sonrası aynı workflow çalışır.

---

## 3. Generate Statistics

**Ne zaman çalışır:** Günlük 02:00 UTC, ilgili dosya değişikliği push’u veya **Run workflow** ile manuel.

### Test

1. **Actions** → **Generate Statistics** → **Run workflow** → **Run workflow**.

**Beklenen:**
- Job yeşil biter.
- `scripts/output/stats/latest_stats.json` oluşur/güncellenir.
- En az bir tane açık (staj formatında) issue varsa, **README.md** içinde “İstatistikler” bölümü güncellenir (commit atılır).

Açık issue yoksa istatistikler 0 olur; yine de workflow hatasız tamamlanır.

---

## 4. Weekly Summary

**Ne zaman çalışır:** Her Pazartesi 09:00 UTC veya **Run workflow** ile manuel.

### Test

1. **Actions** → **Weekly Summary** → **Run workflow** → **Run workflow**.

**Beklenen:**
- Job yeşil biter.
- Yeni bir **Issue** oluşur; başlığı “Haftalık Özet – X. Hafta (2026)” benzeri olur.
- Issue içeriğinde o haftanın başvuru sayısı ve özet bilgiler yer alır.

---

## Hızlı kontrol listesi

| Workflow              | Tetikleme              | Başarı = Yeşil + beklenen sonuç        |
|-----------------------|------------------------|----------------------------------------|
| Automatic Issue Labeler| Issue aç/düzenle       | Doğru formatta label + yorum; yanlışta kapanma + format yorumu |
| Sync Labels           | Run workflow / push    | Labels sayfasında etiketler görünür     |
| Generate Statistics   | Run workflow          | Stats JSON + isteğe göre README güncellemesi |
| Weekly Summary        | Run workflow          | Yeni “Haftalık Özet” issue’su açılır    |

---

## Sorun çıkarsa

- **Permission / token:** Workflow’lar `GITHUB_TOKEN` kullanır; repo **Settings → Actions → General** içinde “Read and write permissions” açık olsun.
- **Branch:** Varsayılan branch’in `main` olduğundan emin ol; bazı workflow’lar `main`’e push veya merge ile tetiklenir.
- **Log:** Her test için **Actions** sekmesinden ilgili run’a tıklayıp adım adım log’a bak; hata mesajı genelde hangi adımda koptuğunu gösterir.

Bu adımlarla deploy sonrası tüm akışları test edebilir ve doğru çalışıp çalışmadığını net görebilirsin.
