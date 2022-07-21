# Wordle with colors!
import random
from dump.wordlist5 import words, valid_words
from colorama import Fore, Style
tries = 0
win = False
answer = words[random.randint(0, len(words) - 1)].upper()
print(f"""
{Fore.GREEN}GREEN: Correct Letter and Position
{Fore.YELLOW}YELLOW: Corrct Letter, Wrong Position
{Fore.RED}RED: Wrong Letter.
{Style.RESET_ALL}
~ Good Luck! :D
""")

def check_ans(guess):
  global tries
  global win
  tries += 1
  reply = ""
  if guess == answer:
    print(Fore.GREEN + guess + Style.RESET_ALL)
    print("Correct!")
    win = True
  else:
    if tries >= 6:
      print("You lose! Answer: " + answer)
      exit()
    else:
      count = 0
      ans_list = list(answer)
      guess_list = list(guess)
      for letter in ans_list:
        if ans_list[count] == guess_list[count]:
          reply += Fore.GREEN + guess_list[count] + Style.RESET_ALL
        elif guess_list[count] in ans_list:
          reply += Fore.YELLOW + guess_list[count] + Style.RESET_ALL
        else:
          reply += Fore.RED + guess[count] + Style.RESET_ALL
        count += 1
      print(reply)

while not win:
  valid = False
  while not valid:
    guess = input("Guess: ").lower()
    print("\033[A                             \033[A")
    if len(guess) == 5 and guess in valid_words or guess in words:
      valid = True
      guess = guess.upper()
      check_ans(guess)
    elif len(guess) != 5:
      print("Please guess a 5 letter word!")
    elif guess not in valid_words:
      print("Word not in word list!")
      
  
