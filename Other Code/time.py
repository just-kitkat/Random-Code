# Convert seconds to days, hours, mins, seconds using rjust
sec = int(input("Please input the time you want converted in seconds: "))
seconds = sec % 60
minutes = sec % 3600 // 60
hours = sec % 86400 // 3600
days = sec // 86400 
print("The equivalent duration is ", str(days) + ":" + str(hours).rjust(2, '0') + ":" + str(minutes).rjust(2, '0') + ":" + str(seconds).rjust(2, '0') + ". \n")