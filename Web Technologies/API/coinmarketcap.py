from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/trending/latest'
parameters = {
  'start':'1',
  'limit':'1000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '5eb1bd46-b52c-4804-8350-71db80fecb34',
}

session = Session()
session.headers.update(headers)

try: 
	response = session.get(url, params=parameters) 
	data = json.loads(response.text) 
	with open('r.json','w') as file:
		json.dump(data, file, indent=4)
		file.close()

except (ConnectionError, Timeout,TooManyRedirects) as e: 
	print(e) 
"""

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

lo = ["id","name","symbol","slug","cmc_rank","num_market_pairs","circulating_supply","total_supply","max_supply","last_updated","date_added","tags","platform","self_reported_circulating_supply","self_reported_market_cap","quote"]
for i in data.get('data'): 
	for r in range(len(i)): 
		i.get(lo[r])
"""