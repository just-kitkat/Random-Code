# Simple hangman game
from wordlist_convert import get_words
import random, time

word = random.choice(get_words())
guessed = []
chance = 6
progress = "_" * len(word)
start = time.time()

while progress != word:
    print(f"Progress: {progress} \nChances Left: {chance} \n")
    guess = ""

    # input validation for guesses
    while len(guess) != 1:
        guess = input("Guess a Letter: ")
        if len(guess) != 1:
            print("Please guess 1 letter!")

    # Check if guess is correct
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