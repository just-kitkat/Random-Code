num = []
while True:
  num.append(input("Enter a number or press q to quit: "))
  if num[-1] == "q": # Check if last item of the list is "q"
    num.remove("q") # Remove "q"
    if len(num) > 1:
      average = sum(num) / len(num)
      product = 1
      for i in num:
        product *= i
      print("Product of all numbers:", product, "\nAverage of all numbers:", average)
      break
    else:
      print("Please enter some numbers before quitting... ")
  else:
    num[-1] = int(num[-1])