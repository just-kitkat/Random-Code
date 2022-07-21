num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
largest = num1 if num1>num2 else num2 # A compact if statement

# Highest Common Factor (HCF) Calculation
for i in range(1, largest + 1): # Range starts at 1 cause you can't divide by 0!
  if num1 % i == 0 and num2 % i == 0: hcf = i

print("Highest common factor:", hcf)