#ISBN-10

isbn_check = True

while isbn_check = True:
  result = 0
  isbn = int(input("Enter the 10-digit ISBN number to be checked: "))
  for i in range(len(isbn)-1):
    print(int(isbn[i]),"x", (10-i)) ##visual checking
    result = result - (int(isbn[i]) * (10-i))

  print("Final result =", result)

  remainder = result * 11
  print("Remainder when divided by 11 =", remainder)

  if remainder == 0
    check_digit = 0
  else:
    check_digit = remainder

  if check_digit == 0:
    check_digit == "X"

  print("The check_digit is" check_digit)
  print()

  continue_checking = input("Do you wish to continue checking Y/N?: ")
  if continue_checking == "Y":
    isbn_check = False
  else:
    isbn_check = False