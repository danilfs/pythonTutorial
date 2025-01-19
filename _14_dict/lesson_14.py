# person = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }
# print(person)  # Outputs: {'name': 'John', 'age': 30, 'city': 'New York'}
# person["job"] = "Engineer"
# print(person)  # Outputs: {'name': 'John', 'age': 40, 'city': 'New York', 'job': 'Engineer'}
#
# person = {}  # or person = dict()
# person["name"] = "John"
# person["age"] = 30
# person["city"] = "New York"
# print(person)  # Outputs: {'name': 'John', 'age': 30, 'city': 'New York'}
#
# person = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }
# print(person["name"])  # Outputs: 'John'
# print(person.get("name"))  # Outputs: 'John'
# print(person.get("country"))  # Outputs: None
# print(person.get("country", "USA"))  # Outputs: USA
# print(person.get("name", "Jack"))  # Outputs: John

# ---------------------------------------------------------------

# person = {
# 	"name": "Danil",
# 	"age": 32,
# 	"city":"SPB"
# }
#
# print(person)
# person["job"] = "Engineer"
# print(person)

# person = {}
# # or person = dict()
# person["name"] = "Danil"
# person["city"] = "SPB"
# person["age"] = 32
# print(person)


person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

add_info = {
	"job":"Kae",
	"name": "Dan",
}

person = person | add_info
print(person)

# person.update(add_info)
# print(person)


# for item in person.items():
#     print(item)
#     print(type(item))
#
# for key, value in person.items():
#     print(key)
#     print(value)
#
# for key in person.keys():
#     print(key)
#
# for value in person.values():
#     print(value)


# for item in person.items():
# 	print(item)
# 	print(type(item))

# for key,value in person.items():
# 	print(key)
# 	print(value)
