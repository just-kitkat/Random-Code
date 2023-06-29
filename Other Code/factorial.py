num = int(input("Enter a number: "))
factorial = 1
for i in range(2, num + 1):
  factorial *= i
print("The factorial of", num, "is", factorial)

# Faster Way:
"""
from math import factorial
num = factorial(int(input("Enter a number: ")))
print("Factorial:", num)
"""

# 1 line:
# import math; num = math.factorial(int(input("Enter a number: "))); print("Factorial:", num)