import requests


url = "https://api.binance.com/api/v3/ticker/price"

responce = requests.get(url , params={'symbol': 'BTCUSDT'})

# content = responce.content

# content = responce.json()

price_object = responce.json()

price = float(price_object['price'])

print(price)
print(type(price))

# print(content)
# print(type(content))

# print(content)
# print(type(content))
