import json
import requests
from idna.idnadata import joining_types

book = {
    'title': '1984',
    'author': 'George Orwell',
    'isbn': '978-0451524935',
    'uuid': 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
}

json_string = json.dumps(book)
print(type(json_string))
print(json_string)

json_string = '{"title": "1984", "author": "George Orwell", "isbn": "978-0451524935", "uuid": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"}'
book = json.loads(json_string)
print(type(book))
print(book)


# book = '{"name": "fdfs", "usd": 12345, "rfdsf": "fdsfsd"}'
# my_string = json.loads(book)
# print(type(book))
# print(type(my_string))
# print(my_string)



# response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
# content = response.content
# content_str =
# print(content)