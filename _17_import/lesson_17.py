from _17_import.math_operations import add,subtract

print(add(1,3))
print(subtract(4,5))

from _17_import import math_operations

print(math_operations.add(6,7))


from _17_import.math_operations import add as addition
print(f'Addition = {addition(7,8)}')