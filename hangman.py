from wordlist_convert import get_words
import random, os, time, json
word = random.choice(get_words())
guessed = []
chance = 6
username = os.environ['REPL_OWNER']
if username == None or username == "":
  print("You are not loggen in so you won't appear on the leaderboard!")
  check = False
else:
  check = True
progress = "_" * len(word)
start = time.time()
while progress != word:
  print(f"Progress: {progress} \nChances Left: {chance} \n")
  guess = ""
  while len(guess) != 1:
    guess = input("Guess a Letter: ")
    if len(guess) != 1:
      print("Please guess 1 letter!")
  if guess in word and guess not in guessed:
    progress = ""
    guessed.append(guess)
    for letter in word:
      if letter in guessed:
        progress += letter 
      else:
        progress += "_"
  elif guess not in word:
    print("Wrong Guess! ")
    chance -= 1
    if chance <= 0:
      print("You lose! Word:", word)
      exit()
  else:
    print("You have already guessed this before! ")
end = time.time()
time_taken = round((end-start), 2)
print(f"You win! Word: {word} \nTime Taken: {time_taken}s")

with open('db.json') as dbjson:
    db = json.load(dbjson)

if check:
  if (username in db["hangman"] and db["hangman"][username] > time_taken) or username not in db["hangman"]:
    db["hangman"][username] = time_taken
    with open("db.json", "w") as outfile:
      json.dump(db, outfile, indent = 4)
  
lb = {users : timing for users, timing in sorted(db["hangman"].items(), key=lambda item: item[1])}

count = 1
format_lb = ""
for item in lb:
  name = item
  timing = lb[name]
  format_lb += f"{count}. {name}: {timing}s \n"
  count += 1
print(f"""
Leaderboards:
{format_lb}
""")
