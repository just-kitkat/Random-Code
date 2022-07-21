"""
A three digit number is called an Armstrong number if the sum of cube of its digit is
equal to number itself.
E.g. 153 is an Armstrong number because (1 3 ) + (5 3 ) + (3 3 ) = 153.
Print all Armstrong numbers between 100 to 500.
"""

print("Calculating Armstrong Numbers... ")
for i in range(100, 501): # last number (501) is non-inclusive! 
  i = str(i)
  if int(i[0])**3 + int(i[1])**3 + int(i[2])**3 == int(i):
    print(i)