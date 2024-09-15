# greeting = 'Hello, World!'
# indexes = []
#
# letters = 0
#
# for letter in greeting:
#     if letter == "o":
#         letters += 1
#         indexes.append()
# print(letters)
# print(indexes)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# for num in numbers:
#     # Skip odd numbers
#     if num %2 != 0:
#         continue
#     print(num)

numbers = [10,11,12,13,14,15]

for i in range(len(numbers)):
    numbers[i] += 1
print(numbers)