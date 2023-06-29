"""
Print the following patterns using loop :
a.
*
**
***
****
b.
  *  
 *** 
*****
 *** 
  *  
c.
1010101
 10101 
  101  
   1
"""

print("a. ")
x = 1
while x < 5:
  print("*" * x)
  x += 1

print("b. ")
x = -1
check = 0
while True:
  if x < 4 and check == 0:
    x += 2
    print(("*" * x).center(5)) # string.center(length, character) (character defaults to a space)
  else:
    x -= 2
    print(("*" * x).center(5))
    check += 1
    if check == 2:
      break

print("c. ")
x = 7
current = "1"
while True:
  if x < 1: break
  var = ""
  for i in range(x):
    var += current
    current = "0" if current == "1" else "1"
  print(var.center(7)) # variable.center(length, char) where char is space by default
  current = "1"
  x -= 2

    