num_words = 3

for i in range(num_words):
  word = "placeholder1"
  check = False
  while not word.isalpha():
    if check:
      print("Please make sure your input countains letters only!")
    word = input("Enter a word: ")
    check = True
      
  num_vowels = 0
  num_consonants = 0
  for letter in word:
    if letter in ["a", "e", "i", "o", "u"]:
      num_vowels += 1
    else:
      num_consonants += 1
  print("The total number of vowels in", word, "is: ", num_vowels, "\nThe total number of consonants in", word, "is:", num_consonants)