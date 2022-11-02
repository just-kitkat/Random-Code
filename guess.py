num = int(input("Enter a number for player 2 to guess: "))
while not (1 <= num <= 100):
  num = int(input("Invalid Input, make sure your number is between 1 and 100! \nEnter a number for player 2 to guess: "))
num_range = [1, 100]
win = False
for count in range(5):
  guess = int(input("Guess a number from {} to {}. ".format(num_range[0], num_range[1])))
  if guess == num:
    print("You guessed the correct number.")
    win = True
    break
  if num_range[0] < guess < num_range[1]:
    if guess > num:
      num_range[1] = guess
    else:
      num_range[0] = guess
  print("You did not guess the correct number.")
if not win:
  print("Game over!")
  