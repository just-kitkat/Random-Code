number = int(input("Please enter a 12-digit number: "))
while len(str(number)) != 12: 
    number = int(input("Invalid input! Please enter a 12-digit number: "))

num_with_weights = []
for index, num in enumerate(str(number)):
    num = int(num)
    if index % 2 == 0:
        num_with_weights.append(num*1)
    else:
        num_with_weights.append(num*3)

remainder = sum(num_with_weights)%10
checkdigit = 10 - remainder

print("{} is the check digit for the twelve-digit number {}".format(checkdigit, number))