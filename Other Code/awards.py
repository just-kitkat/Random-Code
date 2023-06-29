numsubjects = 3 # 2 to 3
subject = ['English','Mathematics','Science']
subjectscore = [] # = to = []
flag = True # False to True
while flag == True:
    subjectscore = []
    for i in range(numsubjects):
        score = int(input("Enter the student's {} score: ".format(subject[i]))) # added int function
        subjectscore.append(score)
                    
    if subjectscore[0] >= 75 and subjectscore[1] >=75 and subjectscore[2] >= 75: # changed or to and
        print("Platimun award")
    elif (subjectscore[0] >= 75 and subjectscore[1] >=75) or (subjectscore[0] >= 75 and subjectscore[2] >= 75): # changed middle and to or
        print("Gold Award") # Silver to Gold
    elif subjectscore[0] >= 75:
        print("Silver Award") # Gold to silver
    else: # elif to else
        print("No Award")

    reply = input("Anymore student (Y / N) : ").upper()
    while reply not in ['Y', 'N']: # 'yn' to ['Y', 'N']
        print("Enter Y or N only!")
        reply = input("Anymore student (Y / N) : ").upper()
    if reply == "Y":
        flag = True # False to True
    else:
        flag = False