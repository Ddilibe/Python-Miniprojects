import requests
from bs4 import BeautifulSoup
from saharapage import Scraping_multiple_websites

jaden = open('jaden.txt','w')

response = requests.get("https://www.naijanews.com/")

soup = BeautifulSoup(response.content, 'html.parser')

links = soup.find_all('section', {'class':'mvp-widget-home'})

for i in links:
    i = i.find('a')
    i = i['href']
    jaden.writelines(i)
    jaden.writelines('\n')
    
jaden.close()
    
Scraping_multiple_websites()