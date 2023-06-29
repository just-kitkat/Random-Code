"""
Write a program to print all prime number in between 1 to 100.
"""
print(2)
for i in range(1, 101): #101 is non-incusive
  for num in range (2, i): # starts from 2 cause everything can be divided by 1
    if i % num == 0 and num < i:
      break
    if num == i-1:
      print(i)

    