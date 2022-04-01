import requests
from bs4 import BeautifulSoup

jaden = open('jaden.txt','w')

response = requests.get("https://saharareporters.com/")

soup = BeautifulSoup(response.content, 'html.parser')

links = soup.find_all('div', {'class':'block-module-content-footer-item block-module-content-footer-item-comments'})

for i in links:
    i = i.find('a')
    i = i['href']
    jaden.writelines(i)
    jaden.writelines('\n')
    
jaden.close()