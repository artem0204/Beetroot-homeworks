from task1.task1 import to_power
from task2.task2 import is_palindrome
from task3.task3 import mult
from task4.task4 import reverse

# task1
print(to_power(2, 4) == 16)
print(to_power(3.5, 2) == 12.25)
try:
    print(to_power(2, -1))
except ValueError as message:
    print(message)

# task2
print(is_palindrome("sassas"))
print(is_palindrome("o"))
print(is_palindrome("MoM"))

# task3
print(mult(2, 4) == 8)
print(mult(2, 0) == 0)
try:
    print(mult(2, -4))
except ValueError as msg:
    print(msg)
# task4
print(reverse("hello") == "olleh")
print(reverse("o")== "o")
