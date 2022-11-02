string = input("Enter a string: ")
not_index = string.find("not")
poor_index = string.find("poor")
if not_index < poor_index:
  string.replace("not ", "").replace("poor", "good")
print(string)
# WIP, NOT DONE