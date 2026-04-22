#!/usr/bin/env python3
"""
İstatistik ve Dashboard Oluşturucu
GitHub Issues'dan istatistikler çıkarır ve README'ye ekler
"""

import requests
import json
import os
from collections import Counter
from datetime import datetime, timedelta
import re

# GitHub API ayarları
github_repo = os.getenv("GITHUB_REPOSITORY", "VB10/staj2026")
github_api_url = f"https://api.github.com/repos/{github_repo}/issues"

# Import token from config file
try:
    from config import GITHUB_TOKEN
    github_headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {GITHUB_TOKEN}"
    }
except ImportError:
    github_token = os.getenv("GITHUB_TOKEN")
    if github_token:
        github_headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {github_token}"
        }
    else:
        print("GITHUB_TOKEN bulunamadı! Lütfen config.py dosyasını oluşturun veya GITHUB_TOKEN environment variable'ını ayarlayın.")
        exit(1)

def parse_issue_title(title):
    """Issue başlığını parse eder"""
    pattern = re.compile(r"^(.*?)\s*\[(.*?)\]\[(.*?)\]\[(.*?)\]\[(.*?)\]$")
    cleaned_title = (
        title.replace(" [", "[")
        .replace("[ ", "[")
        .replace(" ]", "]")
        .replace("] ", "]")
        .strip()
    )
    
    match = pattern.match(cleaned_title)
    if not match:
        return None
    
    name, category, location, intern_type, duration = match.groups()

    def clean_and_split(text):
        return [item.strip() for item in text.replace('[', '').replace(']', '').split(',') if item.strip()]

    return {
        "name": name.strip(),
        "category": clean_and_split(category),
        "location": clean_and_split(location),
        "intern_type": clean_and_split(intern_type),
        "duration": clean_and_split(duration)
    }

def fetch_all_issues():
    """Tüm açık issue'ları çeker"""
    all_issues = []
    page = 1
    per_page = 100
    
    while True:
        try:
            response = requests.get(
                github_api_url,
                headers=github_headers,
                params={
                    "state": "open",
                    "per_page": per_page,
                    "page": page
                }
            )
            
            if response.status_code != 200:
                print(f"Error fetching issues: {response.status_code}")
                break
            
            issues = response.json()
            if not issues:
                break
            
            all_issues.extend(issues)
            page += 1
            
            # Rate limit kontrolü
            if len(issues) < per_page:
                break
                
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            break
    
    return all_issues

def calculate_statistics(issues):
    """İstatistikleri hesaplar"""
    stats = {
        "total_applications": len(issues),
        "categories": Counter(),
        "locations": Counter(),
        "intern_types": Counter(),
        "durations": Counter(),
        "recent_applications": 0,
        "this_week_applications": 0,
        "this_month_applications": 0
    }
    
    now = datetime.now()
    week_ago = now - timedelta(days=7)
    month_ago = now - timedelta(days=30)
    
    for issue in issues:
        parsed = parse_issue_title(issue["title"])
        if not parsed:
            continue
        
        # Kategoriler
        for cat in parsed["category"]:
            stats["categories"][cat] += 1
        
        # Lokasyonlar
        for loc in parsed["location"]:
            stats["locations"][loc] += 1
        
        # Staj tipi
        for itype in parsed["intern_type"]:
            stats["intern_types"][itype] += 1
        
        # Süreler
        for dur in parsed["duration"]:
            stats["durations"][dur] += 1
        
        # Tarih bazlı istatistikler
        created_at = datetime.strptime(issue["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        if created_at >= month_ago:
            stats["this_month_applications"] += 1
        if created_at >= week_ago:
            stats["this_week_applications"] += 1
        if created_at >= now - timedelta(days=1):
            stats["recent_applications"] += 1
    
    return stats

def generate_stats_markdown(stats):
    """Markdown formatında istatistik oluşturur"""
    md = []
    md.append("## 📊 İstatistikler\n")
    md.append(f"**Toplam Başvuru:** {stats['total_applications']}\n")
    md.append(f"**Son 24 Saat:** {stats['recent_applications']} başvuru\n")
    md.append(f"**Bu Hafta:** {stats['this_week_applications']} başvuru\n")
    md.append(f"**Bu Ay:** {stats['this_month_applications']} başvuru\n\n")
    
    md.append("### 🎯 En Çok Tercih Edilen Alanlar\n")
    top_categories = stats['categories'].most_common(10)
    for i, (cat, count) in enumerate(top_categories, 1):
        percentage = (count / stats['total_applications'] * 100) if stats['total_applications'] > 0 else 0
        md.append(f"{i}. **{cat}**: {count} başvuru ({percentage:.1f}%)\n")
    md.append("\n")
    
    md.append("### 📍 Staj Yeri Tercihleri\n")
    for loc, count in stats['locations'].most_common():
        percentage = (count / stats['total_applications'] * 100) if stats['total_applications'] > 0 else 0
        md.append(f"- **{loc}**: {count} başvuru ({percentage:.1f}%)\n")
    md.append("\n")
    
    md.append("### 🎓 Staj Tipi Dağılımı\n")
    for intern_type, count in stats['intern_types'].most_common():
        percentage = (count / stats['total_applications'] * 100) if stats['total_applications'] > 0 else 0
        md.append(f"- **{intern_type}**: {count} başvuru ({percentage:.1f}%)\n")
    md.append("\n")
    
    md.append("### ⏱️ Staj Süresi Tercihleri\n")
    for dur, count in stats['durations'].most_common():
        percentage = (count / stats['total_applications'] * 100) if stats['total_applications'] > 0 else 0
        md.append(f"- **{dur}**: {count} başvuru ({percentage:.1f}%)\n")
    md.append("\n")
    
    md.append(f"*Son güncelleme: {datetime.now().strftime('%d.%m.%Y %H:%M')}*\n")
    
    return "".join(md)

def update_readme(stats_markdown):
    """README.md dosyasını günceller"""
    readme_path = "README.md"
    
    if not os.path.exists(readme_path):
        print(f"README.md bulunamadı: {readme_path}")
        return False
    
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # İstatistik bölümünü bul ve değiştir
    stats_pattern = r"## 📊 İstatistikler.*?(?=\n## |\Z)"
    
    if re.search(stats_pattern, content, re.DOTALL):
        # Mevcut istatistikleri güncelle
        content = re.sub(stats_pattern, stats_markdown.rstrip(), content, flags=re.DOTALL)
    else:
        # İstatistik bölümü yoksa, FAQ'dan önce ekle
        faq_pattern = r"(## FAQ)"
        if re.search(faq_pattern, content):
            content = re.sub(faq_pattern, stats_markdown + r"\1", content)
        else:
            # FAQ da yoksa, en sona ekle
            content += "\n\n" + stats_markdown
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    return True

def save_stats_json(stats):
    """İstatistikleri JSON olarak kaydeder"""
    output_dir = "scripts/output/stats"
    os.makedirs(output_dir, exist_ok=True)
    
    stats_data = {
        "generated_at": datetime.now().isoformat(),
        "total_applications": stats["total_applications"],
        "categories": dict(stats["categories"]),
        "locations": dict(stats["locations"]),
        "intern_types": dict(stats["intern_types"]),
        "durations": dict(stats["durations"]),
        "recent_applications": stats["recent_applications"],
        "this_week_applications": stats["this_week_applications"],
        "this_month_applications": stats["this_month_applications"]
    }
    
    file_path = os.path.join(output_dir, "latest_stats.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(stats_data, f, ensure_ascii=False, indent=2)
    
    print(f"İstatistikler kaydedildi: {file_path}")
    return file_path

def main():
    print("İstatistikler hesaplanıyor...")
    
    issues = fetch_all_issues()
    print(f"Toplam {len(issues)} açık issue bulundu")
    
    stats = calculate_statistics(issues)
    print("İstatistikler hesaplandı")
    
    stats_markdown = generate_stats_markdown(stats)
    print("\n" + stats_markdown)
    
    # JSON olarak kaydet
    save_stats_json(stats)
    
    # README'yi güncelle
    if update_readme(stats_markdown):
        print("\nREADME.md güncellendi")
    else:
        print("\nREADME.md güncellenemedi")

if __name__ == "__main__":
    main()
