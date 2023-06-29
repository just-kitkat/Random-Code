def check(ana1: str, ana2: str) -> str:
    """
    Simple code to check if 2 strings are anagrams
    You may add a .replace(" ", "") if you want to ignore spaces
    Note: This code is space-sensitive but case-insensitive
    """
    return sorted(ana1.lower()) == sorted(ana2.lower())

if __name__ == "__main__":
    words = input("Enter 2 words, seperated by commas: ").split(",")
    result = check(words[0], words[1])
    print("They are anagrams!" if result else "They are not anagrams!")