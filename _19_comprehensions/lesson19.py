# # Traditional way of creating a list with squares of numbers
# squares = []
# for x in range(10):
#     squares.append(x ** 2)
# print(squares)  # Outputs: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#
# squares = [x ** 2 for x in range(10)]
# print(squares)  # Outputs: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#
# even_squares = []
# for x in range(10):
#     if x % 2 == 0:
#         even_squares.append(x ** 2)
# print(even_squares)  # Outputs: [0, 4, 16, 36, 64]
#
# even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
# print(even_squares)  # Outputs: [0, 4, 16, 36, 64]

# squares = []
# for i in range(10):
# 	square = i ** 2
# 	squares.append(square)
# print(squares)
#
# squares_comp = [x ** 2 for x in range(10) ]
# print(squares_comp)

# even_squares = []
# for i in range(10):
# 	if i % 2 == 0:
# 		i = i ** 2
# 		even_squares.append(i)
# print(even_squares)
#
# even_squares_comp = [i ** 2 for i in range(10) if i % 2 == 0]
# print(even_squares_comp)

# numbers = [1, 2, 3, 4, 5]
# labelled_numbers = []
# for num in numbers:
#     if num % 2 == 0:
#         labelled_numbers.append("even")
#     else:
#         labelled_numbers.append("odd")
# print(labelled_numbers)  # Outputs: ['odd', 'even', 'odd', 'even', 'odd']
#
# labelled_numbers = ["even" if num % 2 == 0 else "odd" for num in numbers]
# print(labelled_numbers)  # Outputs: ['odd', 'even', 'odd', 'even', 'odd']

# square_dict = {x: x ** 2 for x in range(10)}
# print(square_dict)  # Outputs: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# list_numbers = [1,2,3,4,5,6]
# labelled_numbers = []
# for i in range(len(list_numbers)):
# 	if i % 2 == 0:
# 		labelled_numbers.append('even')
# 	else:
# 		labelled_numbers.append('odd')
# print(labelled_numbers)

# labelled_numbers = ['even' if i % 2 == 0 else 'odd' for i in list_numbers]
# print(labelled_numbers)

square_dict_comp = {x: x ** 2 for x in range (10)}
print(square_dict_comp)