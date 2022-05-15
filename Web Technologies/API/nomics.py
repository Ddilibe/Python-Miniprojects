"""
	This is a script for scraping nomics cryptocurrency table
"""
import urllib.request
import requests
import json
url = "https://api.nomics.com/v1/currencies"
w = requests.get(url)
print(w)
w = (w.json)
w

with open('r.json','w') as file:
	json.dump(w, file, indent=4)
	file.close()

""" url = "https://api.nomics.com/v1/dashboard?key=d04088a8034acc4bfa8a059cb64eb4a992bb9123"
# curl "https://api.nomics.com/v1/dashboard?key=your-key-here"
# import urllib.request
# print(urllib.request.urlopen(url).read())

import urllib.request
url = "https://api.nomics.com/v1/currencies?key=d04088a8034acc4bfa8a059cb64eb4a992bb9123&ids=BTC,ETH,XRP&attributes=id,name,logo_url&platform-currency=ETH"
url = "https://api.nomics.com/v1/dashboard?key=d04088a8034acc4bfa8a059cb64eb4a992bb9123"
print(urllib.request.urlopen(url).read())
"""