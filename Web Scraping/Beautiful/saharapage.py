import requests 
from bs4 import BeautifulSoup

file = open('jaden.txt', 'r')

def Scraping_multiple_websites(file):   
    num = 1
    for i in file:
        response = requests.get(i)
        soup = BeautifulSoup(response.content, 'html.parser')
        title_write = "TITLE \n\n"
        title = soup.find('p', {'class':'page-header-lead'})
        title = title.string
        image_write = "\n\nIMAGE sECTION\n\n"
        image = soup.find('img', {'class':'media-element file-embedded'})
        image = image['src']
        text_write = "\n\nThe Note section of the news article\n\n"
        texts = soup.find('div', {'class':'story-content'})
        texts = texts.find('p')
        new_file = f"new_file{num}.txt"
        NewContentFile = open(new_file, 'w')
        NewContentFile.writelines(title_write)
        NewContentFile.writelines(title)
        NewContentFile.writelines(image_write)
        NewContentFile.writelines(image)
        NewContentFile.writelines(text_write)
        for i in texts:
            i = i.strings
            if (i != 'None'):
                NewContentFile.writelines(i)
                NewContentFile.writelines('\n')
        NewContentFile.close()
        num += 1

Scraping_multiple_websites(file)

file.close()
