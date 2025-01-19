import requests
from urllib3 import request

responce = requests.get('https://api.binance.com/api/v3/ticker/price', params= {'symbol':'BTCUSDT'})
content = responce.content
print(content)
print(type(content))
price_object = responce.json()
print(price_object)
price = price_object["price"]
print(price)