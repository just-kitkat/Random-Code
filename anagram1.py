"""
Create a user defined function called anagram, that takes in two strings and returns if the strings
are anagrams of each other.

def anagram(string1, string2):
pass
Your function needs to be able to remove spaces and handle anagrams like
"dirty room" and "dormitory"
"I am Lord Voldemort" and "Tom Marvolo Riddle"
"""
#UDF (GIVEN)
def lettersort(word):
    result = list(word)
    result.sort()
    return result
  
def anagram(string1, string2):
  # Returns True if they are anagrams
  # .replace(" ", "") removes spaces by replacing them with empty strings
  # .lower() makes all the letters lowercase!
  return lettersort(string1.replace(" ", "").lower()) == lettersort(string2.replace(" ", "").lower())

# Test cases
print(
      anagram("dormitory", "dirty room"), 
      anagram("I am Lord Voldemort", "Tom Marvolo Riddle"),
      anagram("Not an anagram", "XD")
  )

  