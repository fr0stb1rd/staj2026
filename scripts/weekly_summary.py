#!/usr/bin/env python3
"""
Haftalık Özet Oluşturucu
Her hafta otomatik olarak özet oluşturur ve GitHub Discussion'a ekler
"""

import requests
import json
import os
from datetime import datetime, timedelta
from collections import Counter
import re

# GitHub API ayarları
github_repo = os.getenv("GITHUB_REPOSITORY", "VB10/staj2026")
github_api_url = f"https://api.github.com/repos/{github_repo}"

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
        print("GITHUB_TOKEN bulunamadı!")
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
        cleaned_text = text.replace('[', '').replace(']', '')
        return [item.strip() for item in cleaned_text.split(',')] if cleaned_text else []

    return {
        "name": name.strip(),
        "category": [c for c in clean_and_split(category) if c],
        "location": [l for l in clean_and_split(location) if l],
        "intern_type": [it for it in clean_and_split(intern_type) if it],
        "duration": [d for d in clean_and_split(duration) if d]
    }

def fetch_issues_since(since_date):
    """Belirli bir tarihten sonraki issue'ları çeker"""
    all_issues = []
    page = 1
    per_page = 100
    
    while True:
        try:
            response = requests.get(
                f"{github_api_url}/issues",
                headers=github_headers,
                params={
                    "state": "open",
                    "per_page": per_page,
                    "page": page,
                    "sort": "created",
                    "direction": "desc"
                }
            )
            
            if response.status_code != 200:
                print(f"Error fetching issues: {response.status_code}")
                break
            
            issues = response.json()
            if not issues:
                break
            
            # Tarih kontrolü
            filtered_issues = []
            for issue in issues:
                created_at = datetime.strptime(issue["created_at"], "%Y-%m-%dT%H:%M:%SZ")
                if created_at >= since_date:
                    filtered_issues.append(issue)
                else:
                    # Tarih sıralı olduğu için daha eski issue'ları görürsek dur
                    return all_issues
            
            all_issues.extend(filtered_issues)
            page += 1
            
            if len(issues) < per_page:
                break
                
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            break
    
    return all_issues

def calculate_weekly_stats(issues):
    """Haftalık istatistikleri hesaplar"""
    stats = {
        "total": len(issues),
        "categories": Counter(),
        "locations": Counter(),
        "intern_types": Counter(),
        "durations": Counter(),
        "new_applicants": []
    }
    
    for issue in issues:
        parsed = parse_issue_title(issue["title"])
        if not parsed:
            continue
        
        stats["new_applicants"].append({
            "name": parsed["name"],
            "url": issue["html_url"],
            "categories": parsed["category"]
        })
        
        for cat in parsed["category"]:
            stats["categories"][cat] += 1
        
        for loc in parsed["location"]:
            stats["locations"][loc] += 1
        
        for itype in parsed["intern_type"]:
            stats["intern_types"][itype] += 1
        
        for dur in parsed["duration"]:
            stats["durations"][dur] += 1
    
    return stats

def generate_weekly_summary(stats, week_start, week_end):
    """Haftalık özet markdown oluşturur"""
    md = []
    
    week_number = datetime.now().isocalendar()[1]
    year = datetime.now().year
    
    md.append(f"# 📅 Haftalık Özet - {week_number}. Hafta ({year})\n")
    md.append(f"**Tarih Aralığı:** {week_start.strftime('%d.%m.%Y')} - {week_end.strftime('%d.%m.%Y')}\n\n")
    
    md.append("---\n\n")
    
    md.append("## 📊 Bu Haftanın İstatistikleri\n\n")
    md.append(f"**Yeni Başvuru Sayısı:** {stats['total']}\n\n")
    
    if stats['total'] > 0:
        md.append("### 🎯 En Çok Tercih Edilen Alanlar\n")
        top_categories = stats['categories'].most_common(5)
        for i, (cat, count) in enumerate(top_categories, 1):
            percentage = (count / stats['total'] * 100) if stats['total'] > 0 else 0
            md.append(f"{i}. **{cat}**: {count} başvuru ({percentage:.1f}%)\n")
        md.append("\n")
        
        md.append("### 📍 Staj Yeri Tercihleri\n")
        for loc, count in stats['locations'].most_common():
            percentage = (count / stats['total'] * 100) if stats['total'] > 0 else 0
            md.append(f"- **{loc}**: {count} başvuru ({percentage:.1f}%)\n")
        md.append("\n")
        
        md.append("### 🎓 Staj Tipi Dağılımı\n")
        for intern_type, count in stats['intern_types'].most_common():
            percentage = (count / stats['total'] * 100) if stats['total'] > 0 else 0
            md.append(f"- **{intern_type}**: {count} başvuru ({percentage:.1f}%)\n")
        md.append("\n")
        
        md.append("### ⏱️ Staj Süresi Tercihleri\n")
        for dur, count in stats['durations'].most_common():
            percentage = (count / stats['total'] * 100) if stats['total'] > 0 else 0
            md.append(f"- **{dur}**: {count} başvuru ({percentage:.1f}%)\n")
        md.append("\n")
        
        md.append("### 👥 Yeni Başvuranlar\n")
        md.append(f"Bu hafta **{len(stats['new_applicants'])}** yeni aday başvurdu:\n\n")
        
        # Kategorilere göre grupla
        category_groups = {}
        for applicant in stats['new_applicants']:
            for cat in applicant['categories']:
                if cat not in category_groups:
                    category_groups[cat] = []
                category_groups[cat].append(applicant)
        
        for cat in sorted(category_groups.keys()):
            applicants = category_groups[cat]
            md.append(f"#### {cat.upper()}\n")
            for app in applicants[:10]:  # Her kategoriden max 10 kişi
                md.append(f"- [{app['name']}]({app['url']})\n")
            if len(applicants) > 10:
                md.append(f"- *...ve {len(applicants) - 10} kişi daha*\n")
            md.append("\n")
    else:
        md.append("Bu hafta yeni başvuru bulunmamaktadır.\n\n")
    
    md.append("---\n\n")
    md.append(f"*Bu özet otomatik olarak oluşturulmuştur. Son güncelleme: {datetime.now().strftime('%d.%m.%Y %H:%M')}*\n")
    
    return "".join(md)

def create_discussion(title, body):
    """GitHub Discussion oluşturur"""
    try:
        # GitHub Discussions API (GraphQL veya REST)
        # Not: REST API'de discussions yok, Issue kullanacağız
        response = requests.post(
            f"{github_api_url}/issues",
            headers=github_headers,
            json={
                "title": title,
                "body": body,
                "labels": ["weekly-summary", "otomatik"]
            }
        )
        
        if response.status_code == 201:
            print(f"Özet oluşturuldu: {response.json()['html_url']}")
            return response.json()
        else:
            print(f"Error creating issue: {response.status_code}")
            print(response.text)
            return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def main():
    # Bu haftanın başlangıcı (Pazartesi)
    # Bugün Pazartesi ise, geçen haftanın özetini çıkarmak için 7 gün geriye git.
    # Pazartesi değilse, bu haftanın Pazartesisinden başla.
    today = datetime.now()
    days_since_monday = today.weekday()

    if days_since_monday == 0:
        week_start = today - timedelta(days=7)
    else:
        week_start = today - timedelta(days=days_since_monday)

    week_start = week_start.replace(hour=0, minute=0, second=0, microsecond=0)
    week_end = datetime.now()
    
    print(f"Haftalık özet oluşturuluyor: {week_start.strftime('%d.%m.%Y')} - {week_end.strftime('%d.%m.%Y')}")
    
    issues = fetch_issues_since(week_start)
    print(f"Bu hafta {len(issues)} yeni başvuru bulundu")
    
    stats = calculate_weekly_stats(issues)
    summary = generate_weekly_summary(stats, week_start, week_end)
    
    print("\n" + summary)
    
    # Issue olarak oluştur
    week_number = datetime.now().isocalendar()[1]
    title = f"📅 Haftalık Özet - {week_number}. Hafta ({datetime.now().year})"
    
    result = create_discussion(title, summary)
    
    if result:
        print(f"\n✅ Haftalık özet başarıyla oluşturuldu!")
        print(f"🔗 Link: {result['html_url']}")
    else:
        print("\n❌ Haftalık özet oluşturulamadı!")

if __name__ == "__main__":
    main()
