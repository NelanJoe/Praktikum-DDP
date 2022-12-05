'''
    * Beutifulsoup4
'''

from bs4 import BeautifulSoup


html_soup = BeautifulSoup(open("index.html"), "html.parser")

judul = html_soup.find("p", class_="judul")
judul_aja = html_soup.find("p", class_="judul").text
paragraf = html_soup.find("p", class_="paragraf")


print(judul)
print(paragraf)
print(judul_aja)