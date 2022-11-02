"""
Task 2
You will be given a list of words. You are required to create a program
that will arrange these words into a separate list of similar words.
"""
words = ["shore", "debit card", "countries", "punishment", "school master",
"neurotics", "horse", "the classroom", "nine thumps", "cretinous",
"bad credit", "I am lord voldemort", "tom marvolo riddle"]
looped_list = words
#UDF (GIVEN)
def lettersort (word):
    result = list(word)
    result.sort()
    return result

sorted_words = []
ordered_words = []
for word in looped_list:
  ordered_words.append(lettersort(word.replace(" ", "").lower()))
  
for word in range(len(ordered_words)):
  temp = [word]
  if ordered_words[word] != "":
    for i in range(len(ordered_words)):
      if ordered_words[word] == ordered_words[i] and word != i:
        temp += [i]
        print(temp)
    sorted_words += [[words[i] for i in temp]] # List comprehension, basically a for loop
    for i in temp:
      ordered_words[i] = ""
      
  
print(sorted_words)