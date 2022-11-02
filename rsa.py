import Crypto.Util.number as crypto
n = 1422450808944701344261903748621562998784243662042303391362692043823716783771691667
c = 843044897663847841476319711639772861390329326681532977209935413827620909782846667
e = 65537
"""primes = []
for i in range(1, 10000): 
  print(i)
  for num in range (2, i): # starts from 2 cause everything can be divided by 1
    if i % num == 0 and num < i:
      break
    if num == i-1:
      primes.append(i)


check = False
for p in primes:
  for q in primes:
    if n == p*q:
      check = True
      break
  if check:
    print("found")
    break"""
p,q = 2159947535959146091116171018558446546179, 658558036833541874645521278345168572231473
euler = (p-1)*(q-1)
def inverse(a, b):
    if a == 0:

        return (b, 0, 1)

    else:

        g, y, x = inverse(b % a, a)

        return (g, x - (b // a) * y, y)
d = inverse(e, euler)
print(crypto.long_to_bytes(pow(c,d[0],n)))

637788074230435463953736693062615449582297023194730994021586366598408802525766508