import os, time

blacklist = [] # This prevents users from running potentially dangerous code
# Toggle if the file specified in variable main should be ran immediately
autorun = False
# if "main" entered during file selection, the below will run
main = "Tic Tac Toe/tictactoe"

shortcut = {
  "anagram": "Anagram Checker/anagram",
  "binomial": "Binomial Expansion/binomial",
  "bubblesort": "Bubblesort Algorithm/bubblesort",
  "caesar": "Caesar Cipher/caesar",
  "chess": "Chess/chess",
  "hangman": "Hangman/hangman",
  "sliding": "Sliding Puzzle/sliding",
  "tictactoe": "Tic Tac Toe/tictactoe",
  "wordle": "Wordle/wordle"
}

if autorun:
  print(f"WARNING: AUTORUN HAS BEEN ENABLED. \nPLEASE DISABLE IT TO RUN OTHER FILES!!! \nRUNNING {main.upper()}.PY NOW...")
  exec(open(f'{main}.py', "r").read())

files = ""
while True:
  to_run = input("""
Enter the file path that you want to run.
Example: If you want to run anagram1.py, type in 'Other Code/anagram1'.

For files in their own folder(e.g. binomial.py), you may enter the file name directly. (e.g. binomial instead of Binomial Expansion/binomial)

Note: Not all files are working and most do not have data validation To view a file's source code, click the 'view files' at the top left of the screen! (For users viewing on replit)

If you are confused about the presence of certain files, read the README.md file!

File path: 
"""
)
  if to_run == "": to_run = main
  if to_run not in blacklist:
    if to_run == "main":
      to_run = main
    elif to_run in shortcut:
      to_run = shortcut[to_run]
    print("Executing File... ")
    try:
      exec(open(f'{to_run}.py', "r").read())
      print("Code has finished running. Select another file in 5 seconds... ")
      time.sleep(5)
    except FileNotFoundError:
      print("File does not exist! \nNote: Do not include the '.py' at the back!")
    time.sleep(4)
  elif to_run in blacklist:
    print("You are not allowed to run this file!")
    time.sleep(4)
    
          
# Coded by kitkat3141 :D