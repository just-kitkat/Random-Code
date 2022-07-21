import time as t
ts = t.time()
for i in range(10000):
  print(i)
te = t.time()
print(round((te-ts)*1000), "ms")