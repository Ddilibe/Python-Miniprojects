import requests 
from bs4 import BeautifulSoup


def Scraping_multiple_websites():   
    file = open('jaden.txt', 'r')
    num = 1
    for i in file:
        new_file = f"new_file{num}.txt"
        NewContentFile = open(new_file, 'w')
        response = requests.get(i)
        soup = BeautifulSoup(response.content, 'html.parser')
        title_write = "TITLE\n"
        title = soup.find('h1', {'class':'mvp-post-title left entry-title'})
        title = title.string
        print(title)
        if title not in ["None"] :
                NewContentFile.writelines(title_write)
                NewContentFile.writelines(title)
        image_write = "IMAGE sECTION\n"
        image = soup.find('div', {'id':'mvp-post-content'})
        image = image.find('img')
        if image != 'None':
                image = image['src']
                NewContentFile.writelines(image_write)
                NewContentFile.writelines(image)
        text_write = "The Note section of the ndews article\n"
        texts = soup.find('div', {'id':'mvp-content-main'})
        texts = texts.find_all('p')
        NewContentFile.writelines(text_write)
        for i in texts:
            i = i.strings
            if i not in ["None", " Advertisement ", "Follow Us on Google News "]:
                NewContentFile.writelines(i)
                NewContentFile.writelines('\n')
        NewContentFile.close()
        num += 1
        if num >= 10:
                break
    file.close()



