import requests
from bs4 import BeautifulSoup

url = 'https://diaonline.supermercadosdia.com.ar/almacen?page=2'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting the HTML content as a string

prices = soup.find_all('a', class_='vtex-product-price-1-x-sellingPriceValue')
print(prices)
