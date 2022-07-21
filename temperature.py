# temp erature conversion table ( celc * 1.8 + 32 )
print("""
_____________________________________
|   Temperature Conversion Table    |
_____________________________________
|    Celcius    |    Fahrenheit     |
_____________________________________
""")

for i in range(0, 101, 10): # 101 cause it is non-inclusive, step 10 so it shows the numbers in multiples of 10.
  print("        ", i, "      |     ", i*1.8+32, "    |\n" )
  print("_____________________________________")