import random
num_students = 24
placement = []
#names = input(f"Names of all student separated by commas (e.g. Tom,John,Ben): ").split(",")
all_names = [str(i) for i in range(1,25)]
ALL_NAMES = all_names.copy()

def generate_groups(names, num_groups, per_group):
  groups = [[] for _ in range(num_groups)]
  for group in range(num_groups): # 4 groups of 6
    for _ in range(per_group):
      random_name = random.choice(names)
      groups[group].append(random_name)
      names.remove(random_name)
  return groups

groups = generate_groups(all_names, 4, 6)
def format_groups(groups, formatting):
  res = formatting + " Brackets: "
  for i in range(len(groups)):
    res += "\nGroup {}: {}".format(i + 1, ', '.join(groups[i]))
  res += "\nStart your game!"
  return res
  
print(format_groups(groups, "Starter"))

winners = input("Enter the register numbers of everyone who got top 3 in each group, separared by commas (e.g. 3,8,14): ").split(",")
print("Winners:", ', '.join(winners))

loser1_groups = generate_groups([i for i in ALL_NAMES if i not in winners], 2, 6)
semi_final_groups = generate_groups(winners, 2, 6)
print("\n")
print(format_groups(semi_final_groups, "Semi Finals") + "\n\n"+ format_groups(loser1_groups, "Loser 1"))

semi_winners = input("Enter the register numbers of everyone who got top 3 in each group (6 SEMI FINAL WINNERS), separared by commas (e.g. 3,8,14): ").split(",")
loser1_winners = input("Enter the register numbers of everyone who got top 3 in each group (6 LOSER 1 BRACKET WINNERS), separared by commas (e.g. 3,8,14): ").split(",")

print(loser1_groups)
loser3_groups = generate_groups([i for i in loser1_groups[0]+loser1_groups[1] if i not in loser1_winners], 1, 6) #losers of loser1
loser2_groups = generate_groups(loser1_winners, 1, 6) #winners of loser1
final_groups = generate_groups(semi_winners.copy(), 1, 6)
semi_loser_groups = generate_groups([i for i in semi_final_groups[0]+semi_final_groups[1] if i not in semi_winners.copy()], 1, 6)
print("\n")
print(format_groups(final_groups, "Finals") + "\n\n" + format_groups(semi_loser_groups, "Semi-Finals (losers)") + "\n\n" + format_groups(loser2_groups, "Loser 2") + "\n\n" + format_groups(loser3_groups, "Loser 3"))

print("Enter the following results in this format - winner,runner_up1,runner_up2,runner_up3 \n(ENTER ALL 6 NAMES IN ORDER OF MERIT)")
top6 = input("Winners in Finals: ").split(",")
second6 = input("Winners in Semi-Finals (losers): ").split(",")
third6 = input("Winners in Loser 2: ").split(",")
fourth6 = input("Winners in Loser 3: ").split(",")

lb = top6+second6+third6+fourth6
print(lb)
msg = ""
for i in range(len(lb)):
  msg += "\n    {}. {}".format(i + 1, lb[i])
print("Leaderboards:", msg)

# 1,2,3,4,5,6,7,8,9,10,11,12

