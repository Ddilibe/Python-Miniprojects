import json
"""To call the complete coin list with the HTTP Client using Python"""

import http.client
conn = http.client.HTTPSConnection("coingecko.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "031b653673mshab6231fd8e4d6a5p1c87dbjsn3fd45cd52256",
    'x-rapidapi-host': "coingecko.p.rapidapi.com"
    }
conn.request("GET", "/coins/list", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
with open('r.json','w') as file:
    json.dump(data.decode('utf-8'), file, indent=4)
    file.close()



"""To retrieve the complete list of cryptocurrency exchange tokens using HTTP & Python"""

# import http.client
# conn = http.client.HTTPSConnection("coingecko.p.rapidapi.com")
# headers = {
#     'x-rapidapi-key': "input-your-api-key-here",
#     'x-rapidapi-host': "coingecko.p.rapidapi.com"
#     }
# conn.request("GET", "/exchanges/list", headers=headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))

"""To return background information on the “Bitcoin” ID using an HTTP request in Python"""

# import http.client
# conn = http.client.HTTPSConnection("coingecko.p.rapidapi.com")
# headers = {
#     'x-rapidapi-key': "insert-your-api-key-here",
#     'x-rapidapi-host': "coingecko.p.rapidapi.com"
#     }
# conn.request("GET", "/coins/bitcoin?localization=true&tickers=true&market_data=true&community_data=true&developer_data=true&sparkline=false", headers=headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))


"""To return the background information on the “Aave” exchange using the Exchange ID and an HTTP request in Python"""

# import http.client
# conn = http.client.HTTPSConnection("coingecko.p.rapidapi.com")
# headers = {
#     'x-rapidapi-key': "insert-api-key-here",
#     'x-rapidapi-host': "coingecko.p.rapidapi.com"
#     }
# conn.request("GET", "/exchanges/aave", headers=headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))
"""

Please see the RapidAPI interface page for the CoinGecko API project for a complete list of Python snippets and counterexamples for each working methodology"""