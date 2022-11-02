my_list = []
while True:
  x = input("Enter a number: (blank to sort)")
  if x == "":
    break
  else:
    my_list.append(int(x))

# Bubble sort algorithm
check = 1
while check != 0:
  check = 0
  for i in range(len(my_list)-1):
    print(my_list)
    if my_list[i] > my_list[i+1]:
      check += 1
      temp = my_list[i] 
      my_list[i] = my_list[i+1]
      my_list[i+1] = temp
print("Final Result: {}".format(my_list))
      
    