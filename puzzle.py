# Sliding puzzle using tkinter for the GUI.
from tkinter import * # Import tkinter
import random
print("starting")
width = 350
height = 300
grid = [[],[],[]]
def checker(grid, t):
    for i in range(3):
        try:
          c = grid[i].index("  ")
          
          if t == "up" and i > 0:
            grid[i][c] = grid[i-1][c]
            grid[i-1][c] = "  "
          elif t == "down":
            grid[i][c] = grid[i+1][c]
            grid[i+1][c] = "  "
            
          elif t == "left" and c > 0:
            grid[i][c] = grid[i][c-1]
            grid[i][c-1] = "  "
          elif t == "right":
            grid[i][c] = grid[i][c+1]
            grid[i][c+1] = "  "
        except Exception as e:
          pass
    check_win(grid)
        
    return grid
def gridder(grid, type, t):
    text = ""
    if type:
      dump = [1,2,3,4,5,6,7,8, "  "]
      for i in range(3):
        for a in range(3):
          temp = random.choice(dump)
          grid[i].append(temp)
          dump.remove(temp)
          print(f"Row: {i+1}, Column: {a+1}")
    else:
      grid = checker(grid, t)
    for item in range(3):
      for i in range(3):
        text += f" |   {grid[item][i]}   | "
        
      text += "\n"
    print(grid)
    return text

def check_win(grid):
  if grid == [[1, 2, 3], [4, 5, 6], [7, 8, "  "]]:
    print("You win!")
    exit()

class MainGUI:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Sliding Puzzle") # Set a title

        self.canvas = Canvas(window, bg = "white", width = width, height = height)
        self.canvas.pack()
        
        self.canvas.create_text(100, 100, text = gridder(grid, True, "start"), font=(None, 15))
        self.canvas.pack()
        
        
              
        # Bind canvas with key events
        self.canvas.bind("<Up>", self.up)
        self.canvas.bind("<Down>", self.down)
        self.canvas.bind("<Left>", self.left)
        self.canvas.bind("<Right>", self.right)
        self.canvas.focus_set()

        self.x = width / 2
        self.y = height / 2
        window.mainloop() # Create an event loop

        
  
    def up(self, event):
        self.canvas.delete('all')
        self.canvas.create_text(100, 100, text = gridder(grid, False, "down"), font=(None, 15))
        self.canvas.pack()

    def down(self, event):
        self.canvas.delete('all')
        self.canvas.create_text(100, 100, text = gridder(grid, False, "up"), font=(None, 15))
        self.canvas.pack()

    def left(self, event):
        self.canvas.delete('all')
        self.canvas.create_text(100, 100, text = gridder(grid, False, "right"), font=(None, 15))
        self.canvas.pack()

    def right(self, event):
        self.canvas.delete('all')
        self.canvas.create_text(100, 100, text = gridder(grid, False, "left"), font=(None, 15))
        self.canvas.pack()

MainGUI()
