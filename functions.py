num = []
while len(num) == 0 or num[-1] != "":
  num.append(input("Enter a number. (Enter a blank line to stop): "))
num.remove("")

# Makes all numbers int type
for i in range(len(num)):
  num[i] = int(num[i])
num.sort()
  
def add(num1, num2):
  return num1 + num2

print("Highest number: {}, Lowest number: {}".format(max(num), min(num)))

# Manual mode calculation
mode, gcount = "", 0 # where mode is the number and gcount is the frequency
for i in num: # Loops through the list, num
  count = 0
  for a in num: # Checks how many times the number appears
    if a == i:
      count += 1
  if count > gcount: # Check if frequency is more than previous number
    mode = i
    gcount = count

print("Median: {}, Mode: {}, Average: {}".format(num[len(num)//2], mode, round(sum(num) / len(num), 2)))