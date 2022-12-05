'''
    * Import modul Beautifulsoup4
    * Modul didapat dari install modul: pip install beautifulsoup4

    * Import modul requests
    * Modul didapat dari install modul: pip install requests
'''
from bs4 import BeautifulSoup
import requests

def jadwal_sholat(url):
    '''
        * Definisikan variabel sholat:
        * - subuh
        * - dzuhur
        * - ashar
        * - maghrib
        * - isya
    '''
    subuh = ""
    dzuhur = ""
    ashar = ""
    maghrib = ""
    isya = ""

    '''
        * Coba get koneksi ke url
        * Jika gagal maka 
    '''
    try:
        content = requests.get(url)
        print("Berhasil Koneksi Ke URL")
    except Exception:
        print("Gagal Koneksi Ke URL")
        return None

    '''
        * Jika status code dari content == 200 maka jalankan body if
    '''
    if (content.status_code == 200):
        
        # Buat variabel soup dengan function built-in BeautifulSoup
        soup = BeautifulSoup(content.text, "html.parser")

        '''
            * Definisikan variabel jadwal_all
            * dengan isinya dari variabel soup dengan memanggil function built-in find_all
        '''
        jadwal_all = soup.find_all("p", {"class": "praytime"})
        
        i = 0
        for jadwal in jadwal_all:
            if i == 1:
                subuh = jadwal.text
            elif i == 2:
                dzuhur = jadwal.text
            elif i == 3:
                ashar = jadwal.text
            elif i == 4:
                maghrib = jadwal.text
            elif i == 5:
                isya = jadwal.text

            i += 1


    print(f"Waktu Sholat Subuh   : {subuh} WIB")
    print(f"Waktu Sholat Dzuhur  : {dzuhur} WIB")
    print(f"Waktu Sholat Ashar   : {ashar} WIB")
    print(f"Waktu Sholat Maghrib : {maghrib} WIB")
    print(f"Waktu Sholat Isya    : {isya} WIB")
    