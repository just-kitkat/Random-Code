# WIP NOT DONE

import random
deck = ['2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD','2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS']
def deal():
  temp = deck.copy()
  res = []
  for _ in range(52):
    choice = random.choice(temp)
    res.append(choice)
    temp.remove(choice)
  return res

def points(hand):
  point = 0
  temp_deck = [i[:-1] for i in hand]
  for i in range(26):
    if str(temp_deck).find("A") >= 0 and str(temp_deck).find("9") >= 0:
      point += 5
      temp_deck.remove("A")
      temp_deck.remove("9")
    if str(temp_deck).find("2") >= 0 and str(temp_deck).find("8") >= 0:
      point += 5
      temp_deck.remove("2")
      temp_deck.remove("8")
    if str(temp_deck).find("3") >= 0 and str(temp_deck).find("7") >= 0:
      point += 5
      temp_deck.remove("3")
      temp_deck.remove("7")
    if str(temp_deck).find("4") >= 0 and str(temp_deck).find("6") >= 0:
      point += 5
      temp_deck.remove("4")
      temp_deck.remove("6")
    if str(temp_deck).count("5") >= 2:
      point += 5
      temp_deck.remove("5")
      temp_deck.remove("5")
    if str(temp_deck).count("J") >= 2:
      point += 10
      temp_deck.remove("J")
      temp_deck.remove("J")
    if str(temp_deck).count("Q") >= 2:
      point += 10
      temp_deck.remove("Q")
      temp_deck.remove("Q")
    if str(temp_deck).count("K") >= 2:
      point += 10
      temp_deck.remove("K")
      temp_deck.remove("K")
  point -= len(temp_deck)
  print(len(temp_deck))
    
  return point

# Test cases
print(points(['2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD','2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC']))

random_deal = deal()
p1, p2 = random_deal[:26], random_deal[26:]
print("Player 1 has {} points.".format(points(p1)))
print("Player 2 has {} points.".format(points(p2)))
if points(p1) != points(p2):
  print("Player {} wins.".format(1 if points(p1) > points(p2) else 2))
else:
  print("It's a tie.")