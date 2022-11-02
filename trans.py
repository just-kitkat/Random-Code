from googletrans import Translator, LANGUAGES
trans = Translator()
t = input("Translator: ")
if t == "view":
  print(LANGUAGES)
else:
  x = t.split(" ")
  final = trans.translate(x[0:-1], dest = x[1])
  print("Translated verison:", final)