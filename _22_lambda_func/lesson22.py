# def sort_by_len(element: str) -> int:
#     return len(element)
#
#
# sort_by_len_lambda = lambda element: len(element)
# print(sort_by_len("banana"))  # Output: 6
# print(sort_by_len_lambda("banana"))  # Output: 6
#

# def sort_by_len(element: str) -> int:
# 	return len(element)
#
# sort_by_len_lambda = lambda element: len(element)
#
# print(sort_by_len('banana'))
# print(sort_by_len_lambda('banana'))
#
# fruits = ["banana", "apple", "cherry", "date"]
# sorted_fruits = sorted(fruits, key=lambda element: len(element))
#
# fruits = ['apple', 'banana', 'cherry']
# sorted_fruits = sorted(fruits, key= lambda x: len(x))
#
# print(sorted_fruits)
# print(sorted_fruits)
# fruits = ["apple", "banana", "cherry", "date"]
# longest_word = max(fruits, key=lambda x: len(x))
# print(longest_word)  # Output: 'banana'


fruits = ['apple', 'bananaaa', 'cherry']
max_fruit = max(fruits, key= lambda x: len(x))

print(max_fruit)
