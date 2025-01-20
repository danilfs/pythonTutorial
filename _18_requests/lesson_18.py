import json
import time

import requests

# response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
# content = response.content
# print(content)
# price_object = response.json()
# print(price_object)
# price = float(price_object['price'])
# print(price)

bitcoin_prices = []

for i in range(30):
	response = requests.get('https://api.binance.com/api/v3/ticker/price', params= {'symbol':'BTCUSDT'})
	price_object = response.json()
	price = float(price_object['price'])
	bitcoin_prices.append(price)


print(bitcoin_prices)
print(len(bitcoin_prices))
print(max(bitcoin_prices))
print(min(bitcoin_prices))