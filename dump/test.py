grid = []
dump = [1,2,3,4,5,6,7,8, "  "]
for i in range(9):
  temp = random.choice(dump)
  grid.append(temp)
  dump.remove(temp)
def num():
  text = ""
  for item in range(9):
    text += f" | {grid[item]} | "
    if item in (2, 5):
      text += "\n"
  canvas.create_text(100, 100, text = text)
  canvas.pack()