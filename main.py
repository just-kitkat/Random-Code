import os, time
blacklist = ["eval", "maze"]
main = "tourney"
files = ""
while True:
  for file in os.listdir():
    if file.endswith(".py"):
      if file[:-3] not in blacklist: files += " "*15 + file + "\n"
  to_run = input("Enter the file name that you want to run. \nExample: If you want to run fib.py, type in 'fib'. \nList of files:" + files[14:] + "\nNote: Not all files are working and most do not have data validation \n**To view a file's source code, click the 'view files' at the top left of the screen!** \nFile Name: ")
  if to_run + ".py" in os.listdir() and to_run not in blacklist:
    if to_run == "main":
      to_run = main
    print("Executing File... ")
    exec(open(f'{to_run}.py', "r").read())
    print("Code has finished running. Select another file in 5 seconds... ")
    time.sleep(5)
  elif to_run in blacklist:
    print("You are not allowed to run this file!")
    time.sleep(4)
  else:
    print("File does not exist! \nNote: Do not include the '.py' at the back!")
    time.sleep(4)

# Coded by kitkat3141 :D