def simplegenerator():
    yield 'aaa'
    yield 'bbb'
    yield 'ccc'

def list_tripler(somelist):
    for item in somelist:
        item *= 3
        yield item

def limit_iterator(somelist, max):
    for item in somelist:
        if item > max:
            return
        yield item

def test():
    print( '1.', '-' * 30)
    it = simplegenerator()
    for item in it:
        print (item)
    print ('2.', '-' * 30)
    alist = range(5)
    it = list_tripler(alist)
    for item in it:
        print (item)
    print ('3.', '-' * 30)
    alist = range(8)
    it = limit_iterator(alist, 4)
    for item in it:
        print (item)
    print('4.', '-' * 30)
    it = simplegenerator()
    try:
        print (it._next_())
        print (it.next())
        print (it.next())
        print (it.next())
    except (StopIteration, exp):
        print ('Reached end of sequence')

if __name__ == '__main__':
    test()
import requests

from bs4 import BeautifulSoup


url = "https://www.imdb.com/chart/moviemeter/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

table = soup.find('table',  {'class': 'chart full-width'})

rows = table.find_all('tr')

movies = []

for row in rows:
    image = row.find('img')
    if image:
        movies.append(image['alt'])