code = input("Enter a 12-digit UPC code: ")
process = code[:-1]

odd_sum = sum([int(num) for num_index, num in enumerate(process) if num_index%2 == 0])
multiplied_odd_sum = odd_sum*3
even_sum = sum([int(num) for num_index, num in enumerate(process) if num_index%2 == 1])
total_sum = multiplied_odd_sum + even_sum
remainder = total_sum%10

if remainder == 0:
  check_digit = 0
else:
  check_digit = 10 - remainder
  
if check_digit == int(code[-1]):
  print("Yes, it is a valid UPC code.")
else:
  print("No, it is an invalid UPC code.")