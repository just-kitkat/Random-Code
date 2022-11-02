pcode=input("Please enter the product code: ") # removed int() function
check = ["CHP", "CKS", "DFT"]
while pcode != "q": # removed not 
  valid=False
  while valid == False and pcode != "q": # Added check for q to exit program
    code=pcode[:3] # changed slicing from :2 to :3 
    if code.upper() not in check: # in check changed to not in check
      pcode=(input("Invalid product! Please re-enter the product code: "))
      valid = False
    elif not pcode[-3:].isdigit(): # removed int() function and changed .isdigit to .isdigit()
      pcode=(input("Invalid product! Please re-enter the product code: "))
      valid = False
    elif len(pcode) != 6: # changed len check from 5 to 6
      pcode=(input("Invalid product! Please re-enter the product code: ")) # Closed the bracket
      valid = False
    else:
      print("Valid product.")
      valid = True # Changed valid assingment from False to True
  if pcode != "q":
    pcode=input("Please enter the product code: ")
print("Quitting program. Thank you!") # Changed inverted comma from ' to "