num_students = int(input("Enter the number of students: "))
for student in range(1, num_students+1):
    height = float(input ("Enter student height in metres: "))
    while not (1.2 <= height <= 2.85):
        height = float(input ("Invalid input! Enter student height in metres (between 1.2m and 2.85m inclusive): "))
    weight = float(input ("Enter student weight in kg: "))
    name = input("Please enter the student's name: ")
    
    BMI = weight / height **2
    
    print("Student " + str(student) + ": " + name)
    if BMI >= 30:
        print("Student BMI is ",BMI)
        print("Student is in obese range! Arrange diet and exercise plan.")
    elif BMI >= 25:
        print("Student BMI is ",BMI)
        print ("Student is in overweight range! Arrange exercise plan.")
    elif BMI >= 18.5:
        print("Student BMI is ",BMI)
        print ("Student is in healthy weight range! Encourage student!")
    else:
        print("Student BMI is ",BMI)
        print ("Student is in underweight range! Eat more!")