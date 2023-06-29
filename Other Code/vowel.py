ptext = list(input("Plain text: ").lower()) # added closing bracket

for i in range(1,6): # changed 2 to 6
    vowel = input("Enter vowel {} to change: ".format(i)).lower()
    while vowel not in ["a", "e", "i", "o", "u"]: # made aeiou lowercase and list
        print("Input is not a vowel! Please re-enter.")
        vowel = input("Enter vowel {} to change: ".format(i)) #changed print to input
    change = input("Enter letter to replace vowel {}: ".format(i))
    for x in range(len(ptext)): # wrapped len() func in a range() func
        if ptext[x] == vowel: # changed = to ==
            ptext[x] = change # changed += to =

ctext = ""
for ch in ptext: # added colon
    ctext += ch # changed Ch to ch
print("Cipher text: {}".format(ctext)) # unindent print statement