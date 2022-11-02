VOWELS = ["a", "e", "i", "o", "u"]
text = input("Enter text to translate: ")
translated_text = ""
for word in text.split():
  translated = ""
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
    translated = word[number_moved:] + moved_letters + "ay"
  translated_text += translated + " "

print(translated_text)
      