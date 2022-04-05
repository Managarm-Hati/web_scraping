import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.facebook.com/marketplace/santiagocl/search?query=RTX%203060')

soup = BeautifulSoup(page.text, 'html.parser')
nombre_producto= 'a8nywdso e5nlhep0 rz4wbd8a linoseic'
span = soup.find_all('span')
for span in span:
    autor = span.find(class_ = nombre_producto).text


    print([nombre_producto])