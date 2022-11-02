choice = input("Press B for conversion to Binary and D for conversion to Denary: ")
choice = choice.upper()
while choice not in ("B", "D"): # error 1
    print("Wrong input.")
    choice = input("Press B for conversion to Binary and D for conversion to Denary: ")
    choice = choice.upper()
    
if choice == "B":  # Changed check to B instead of D
    denary = input("Enter denary number: ")    
    denary = int(denary) # added int()
    binary = ""
    while True: 
        r = denary%2
        binary += str(r)
        denary = denary//2 # changed %2 to //2
        if denary == 0: 
            break # changed continue to break

    print("The binary number is:", binary[-1::-1]) # step -1

elif choice == "D":
    denary = 0
    binary = input("Enter binary number: ") # chaned denary to binary
    binary = binary[::-1]
    for n in range(len(binary)): # added len()
        denary += int(binary[n])*2**n # * to **
    print("The denary number is:", denary) 