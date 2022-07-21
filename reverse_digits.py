"""
Write a program to print a number given by user but digits reversed. E.g.-
INPUT : 123         OUTPUT : 321
INPUT : 12345        OUTPUT : 54321
"""
num = input("Input a number: ")
print(num[::-1]) # step of -1 reverses the string!