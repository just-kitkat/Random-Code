"""
In this exercise you will create a program that computes the average of a collection of
values entered by the user. The user will enter 0 as a sentinel value to indicate that no
further values will be provided. Your program should display an appropriate error
message if the first value entered by the user is 0.
"""
num = []
while True:
  num.append(int(input("Enter an integer (0 to get the average): ")))
  if num[0] == 0:
    print("Your first number cannot be 0")
    num.remove(0)
  elif num[-1] == 0:
    num.remove(0)
    print("Average: ", sum(num)/len(num))
    break