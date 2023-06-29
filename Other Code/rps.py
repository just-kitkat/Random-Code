def RPS(p1, p2):
  if p1 == p2:
    return "It's a draw!"
  else:
    if p1 == "r":
      if p2 == "s":
        winner = "Player 1"
      else:
        winner = "Player 2"
        
    elif p1 == "p":
      if p2 == "r":
        winner = "Player 1"
      else:
        winner = "Player 2"

    elif p1 == "s":
      if p2 == "p":
        winner = "Player 1"
      else:
        winner = "Player 2"
        
    return winner +  " wins!"

for _ in range(3):
  print(RPS(input("Player 1 please enter either 'r', 'p' or 's': "), input("Player 2 please enter either 'r', 'p' or 's': ")))