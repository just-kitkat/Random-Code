def sort(my_list: list) -> list:
    """
    A simple sort algorithm that uses 
    bubblesort to sort items in a list
    """
    check = True
    while check:
        check = False
        
        for ind, i in enumerate(my_list):
            if ind == len(my_list) - 1: break
            if i > my_list[ind+1]:
                check = True
                
                my_list[ind], my_list[ind+1] = my_list[ind+1], i

    return my_list
      
if __name__ == "__main__":
    list_ = input("Enter numbers to be sorted, separated with commas: ")
    try:
        print(sort(list(list_.split(","))))
    except Exception as err:
        print(
f"""AN ERROR OCCURED
Sample input: 4,3,2,1

Make sure the format of your input is valid!
Error: {err}
""")