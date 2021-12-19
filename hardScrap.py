from bs4 import BeautifulSoup
import requests

url = 'inset url here'

response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')

title = soup.find_all('title')
print(title)
