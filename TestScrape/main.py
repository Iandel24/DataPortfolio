import requests
from bs4 import BeautifulSoup

url = 'https://www.infobae.com/ultimas-noticias/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting the HTML content as a string

divs = soup.find_all('div', class_='col1')

for div in divs:
    # Remove img tags
    for img in div.find_all('img'):
        img.decompose()
    print(div.get_text(strip=True))
