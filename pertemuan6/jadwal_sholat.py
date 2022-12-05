from bs4 import BeautifulSoup
import requests

def jadwal_sholat(url):
    try:
        content = requests.get(url)
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, "html.parser")

        jadwal_all = soup.find_all("p", {"class": "praytime"})
        
        subuh = jadwal_all[0].text
        dzuhur = jadwal_all[1].text
        ashar = jadwal_all[2].text
        maghrib = jadwal_all[3].text
        isya = jadwal_all[3].text

    print(f"Waktu Sholat Subuh: {subuh}")
    print(f"Waktu Sholat Dzuhur: {dzuhur}")
    print(f"Waktu Sholat Ashar: {ashar}")
    print(f"Waktu Sholat Maghrib: {maghrib}")
    print(f"Waktu Sholat Isya: {isya}")