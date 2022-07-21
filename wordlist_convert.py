from dump.wordtxt import words
def get_words():
  a = words.split("\n")
  output = []
  for i in a:
    if len(i) > 5:
      output.append(i)
  return output
