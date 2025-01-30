def find_average(*, numbers: list) -> float:
	return sum(numbers) / len(numbers)

# print(find_average(numbers= [1,2,3,4,5,6]))

try:
	find_average(numbers= [1,2,3,4,5])
except ZeroDivisionError:
	print('The list is empty')
