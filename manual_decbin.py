binary = input("Enter binary number: ")
count = 1
decimal = 0
for i in list(binary)[::-1]: # makes it a list and reverses it 
  if i == "1":
    decimal += count
  count = count * 2 # 1 2 4 8 16 32 ...
print(decimal)