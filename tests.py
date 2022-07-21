s = input('Enter a string: ')
a = s.split(" ")
high = ""
x = max(a)
for i in a:
    if len(i) == len(x):
        high += i
        
print(high)