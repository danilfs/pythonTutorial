import json
import requests

# book = '{"name": "fdfs", "usd": 12345, "rfdsf": "fdsfsd"}'
# my_string = json.loads(book)
# print(type(book))
# print(type(my_string))
# print(my_string)



response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
content = response.content
content_str =
print(content)