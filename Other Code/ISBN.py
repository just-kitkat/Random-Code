#ISBN-10

isbn_check = True

while isbn_check: # 1
  result = 0
  isbn = str(input("Enter the 10-digit ISBN number to be checked: ")) # 9
  for i in range(len(isbn)-1):
    print(int(isbn[i]),"x", (10-i)) ##visual checking
    result = result + (int(isbn[i]) * (10-i)) # 4

  print("Final result =", result)

  remainder = result % 11 # 5
  print("Remainder when divided by 11 =", remainder)

  if remainder == 0: # 8
    check_digit = 0
  else:
    check_digit = 11 - remainder # 6

  if check_digit == 10: # 7
    check_digit = "X" # 10

  print("The check_digit is", check_digit) # 2
  print()

  continue_checking = input("Do you wish to continue checking Y/N?: ")
  if continue_checking == "Y":
    isbn_check = True # 3
  else:
    isbn_check = False