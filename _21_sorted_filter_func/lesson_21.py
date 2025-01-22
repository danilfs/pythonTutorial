# fruits = ["banana", "apple", "cherry", "date"]
# sorted_fruits = sorted(fruits)
# print(sorted_fruits)  # Output: ['apple', 'banana', 'cherry', 'date']
# print(fruits)  # Output: ['banana', 'apple', 'cherry', 'date']
#
# fruits = ["banana", "apple", "cherry", "date"]
# sorted_fruits = sorted(fruits, reverse=True)
# print(sorted_fruits)  # Output: ['date', 'cherry', 'banana', 'apple']
#
#
# def sort_by_len(element):
#     return len(element)

# fruits = ['banana', 'apple', 'cherry']
# print(sorted(fruits))
# print(sorted(fruits, reverse=True))
#
# def sort_by_len(element):
# 	return len(element)
#
# sorted_fruits = sorted(fruits, key=sort_by_len)
# print(sorted_fruits)

# fruits = ["banana", "apple", "cherry", "date"]
# sorted_fruits = sorted(fruits, key=sort_by_len)
# print(sorted_fruits)  # Output: ['date', 'apple', 'banana', 'cherry']
#
# sorted_fruits = sorted(fruits, key=sort_by_len)
# print(sorted_fruits)
#
# people = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 20},
#     {"name": "Charlie", "age": 30},
# ]
#

people = [
	{'name': 'Alice', 'age': 24},
	{'name': 'Gregor', 'age': 43},
	{'name': 'Patric', 'age': 12},
]

def sort_by_age(element):
	return element['age']

sorted_by_age = sorted(people, key= sort_by_age)
print(sorted_by_age)

#
# def sort_by_age(element):
#     return element["age"]
#
#
# sorted_people = sorted(people, key=sort_by_age)
# print(sorted_people)  # Output: [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}]
#
# people = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 20},
#     {"name": "Diana", "age": 30},
#     {"name": "Charlie", "age": 30},
# ]
#
#
# def sort_by_age_name(element):
#     return element["age"], element["name"]
#
#
# sorted_people = sorted(people, key=sort_by_age_name)
# print(sorted_people)  # Output: [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}, {'name': 'Diana', 'age': 30}]


# def is_even(n):
#     return n % 2 == 0
#
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# filtered_numbers = list(filter(is_even, numbers))
# print(filtered_numbers)  # Output will be [2, 4, 6, 8]


def is_even(n):
	return n % 2 == 0

numbers = [1,2,3,4,5,6,7,8,9]
filtered_numbers = list(filter(is_even, numbers))
print(filtered_numbers)

def filter_by_age(a):
	return a >= 4

sorted_by_number = list(filter(filter_by_age,numbers))
print(sorted_by_number)