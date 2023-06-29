def check(ana1: str, ana2: str) -> str:
    """
    Simple code to check if 2 strings are anagrams
    You may add a .replace(" ", "") if the question requires you to ignore spaces
    """
    return "Anagrams" if sorted(ana1.lower()) == sorted(ana2.lower()) else "Not anagrams"
    
print(check("Listen", "Silent"), check("modern", "norman"))