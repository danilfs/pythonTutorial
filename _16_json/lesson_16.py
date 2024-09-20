import json

book = '{"name": "fdfs", "usd": 12345, "rfdsf": "fdsfsd"}'
my_string = json.loads(book)
print(type(book))
print(type(my_string))
print(my_string)