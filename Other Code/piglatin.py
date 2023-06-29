# Now made to handle uppercase and punctuation!
VOWELS = ["a", "e", "i", "o", "u"]
PUNCTUATIONS = ["!", ".", ",", "?"]
text = input("Enter text to translate: ")
translated_text = ""
for word in text.split():
  translated = ""
  punctuation = ""

  # Checks if the last char is a punctuation
  if word[-1] in PUNCTUATIONS:
    punctuation = word[-1]
    word = word[:-1]

  # Checks for uppercase
  if word[0].isupper():
    upper = True
  else:
    upper = False

  # Checks if first letter is vowel
  if word[0] in VOWELS:
    translated = word + "way" 
    
  else:
    moved_letters = ""
    for i in range(len(word)):
      if word[i] not in VOWELS:
        moved_letters += word[i]
      else:
        number_moved = i
        break
    translated = (word[number_moved:] + moved_letters + "ay").lower()
  if upper:
    translated = list(translated)
    translated[0] = translated[0].upper()
    translated = "".join(translated)
  translated_text += translated + punctuation + " "

print(translated_text)
      