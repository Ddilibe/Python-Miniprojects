import numpy as np

country = ['Great Britain', 'China', 'Russia','United States', 'Korea', 'Japan', 'Germany']
country_code = ['GBR','CHN','RUS','US','KOR','JPN','GER']
year = 2012
greaterthan_twenty = []
gold = [29,38,24,46,13,7,11]
silver = [17,28,25,28,8,14,11]
bronze = [19,22,32,29,7,17,14]

goldc = np.array(gold)
silverw = np.array(silver)
bronzed = np.array(bronze)
y = 0
for i in range(len(gold)):
	if goldc.max() == gold[y]:
		break
	y+=1
print(f"The country with the maximum gold medals is {country[y]}")
y=0
for i in range(len(gold)):
	if gold[i] > 20:
		greaterthan_twenty.append(y)
	y+=1 
print("Countries with more than 20 gold medal include ", end="")
t = 0
for i in greaterthan_twenty:
	if t == 3:
		print(f"and {country[i]}")
	else:
		print(f"{country[i]}, ",end="")
	t+=1
print("""\n Metal Tally\n Gold  Silver  Bronze""")
for i in range(len(gold)):
	print(f""" {gold[i]} 	{silver[i]} 	{bronze[i]}""")
print("""\n Country and Corresponding Number of gold medals""")
for i in range(len(gold)):
	print(f""" {country[i]} - {gold[i]}""")
print("""\n Countries and Total Number of medals won""")
for i in range(len(gold)):
	print(f""" {country[i]} - {gold[i]+silver[i]+bronze[i]}""")