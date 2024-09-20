# def add (*, x = int, y = int) -> int :
# 	return (x * y)
# print (f"Multiply is: {add(x=2, y=3)}")

def add_all (*args):
	summary = 0
	for num in args:
		summary += num
	return summary

print(add_all(2,4,3))