durian_num = 5
lightest = 99
heaviest = 0
counter = 0
lower_limit = 2.5
upper_limit = 6.5
durian_list = []

while counter < durian_num:
    new = float(input("Enter the durian’s weight: "))
    while not (lower_limit < new < upper_limit):
        new = float(input("Please make sure the weight is between {} and {}. \nEnter the durian’s weight: ".format(lower_limit, upper_limit)))

    if new < lightest:
        lightest = new
    if new > heaviest:
        heaviest = new

    counter = counter + 1

    durian_list.append(new)

print("The lightest durian weighs ", lightest, "kg ")
print("The heaviest durian weighs ", heaviest, "kg ")
print("Total weight of all durians weighs ", sum(durian_list), "kg ")