import os
total = 0
for file in os.listdir(os.curdir):
  if not file.endswith(".py"): continue
  with open("countlines.py", 'r') as fp:
      for count, line in enumerate(fp):
          pass
      total += count
print('Total Lines', total + 1)