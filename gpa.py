# 5 inputs!

total = 0
def check(grade_arg):
  grade_ref = {
    "a+" : 4.0,
    "a" : 4.0,
    "a-" : 3.7,
    "b+" : 3.3,
    "b" : 3,
    "b-" : 2.7,
    "c+" : 2.3,
    "c" : 2.0,
    "c-" : 1.7,
    "d+" : 1.3, 
    "d" : 1.0,
    "f" : 0
  }
  return grade_ref[grade_arg.lower()]
  lst = []
for i in range(5):
  grade = input("Enter a grade: ")
  total += check(grade)
print("Average:", total/5)

