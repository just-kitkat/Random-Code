"""
Calculate the sum of digits of a number given by user.
E.g
INPUT: 123         OUTPUT: 6
INPUT: 12345         OUTPUT: 15
"""

num = input("Enter a number: ")
total = 0
for i in list(num):
  total += int(i)
print("The sum of the digits of the number is", total)