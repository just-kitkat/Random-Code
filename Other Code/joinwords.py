num_of_words = 5 # only 5 words
result = ""
for count in range(num_of_words):
  word = input("Enter a word: ")
  while not 1 <= len(word) <= 15:
    word = input("Invalid Input! Make sure your word has a length of 1 to 15 characters. \nEnter a word: ")
  result += word
  if count < num_of_words - 1:
    result += " "
print("Word List:\n" + "\n".join(result.split(" ")))
print("Sentence =", result)
print("Total characters used =", len(result))