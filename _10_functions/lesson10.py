# numbers1 = [1,2,3,5,6,7]
# numbers2 = [1,9,3,1,1,1]
#
# def find_average (some_numbers):
# 	average = sum(some_numbers) / len(some_numbers)
# 	return average
#
# average1 = find_average(numbers1)
# average2 = find_average(numbers2)
#
# print(average2, average1)

# def find_vowels (some_word):
# 	VOWELS = "aeiouAEIOU"
# 	count = 0
# 	for char in some_word:
# 		if char in VOWELS:
# 			count += 1
# 	return count
# print(find_vowels('ijfiojodsjfo'))

# def format_day (*, day: int , month: str) -> str:
# 	return f"The day is {day} , the month is {month}"
# print(format_day(day = 15 ,month ='October'))


def greetings (*, name: str , greeting: str = 'Good morning') -> str :
	return f"{name}, {greeting}"
print (greetings(name = "Fanty" ))
print (greetings(name = "John" , greeting= "Hi"))
