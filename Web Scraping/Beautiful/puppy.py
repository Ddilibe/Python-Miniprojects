import requests
from bs4 import BeautifulSoup

john = open('jaden.txt', 'r')

for i in john:
    response = requests.get(i)
    print(response)

john.close()