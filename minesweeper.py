from tkinter import * # Bad code but meh :/
import math, time, random
print("starting")
width = 300
height = 300
grid_prop = width//10
font = 12
txt_x, txt_y = 155, 190
turn = "X"


class MainGUI:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Minesweeper") # Set a title
        self.grid = [0] * 100
        self.clicked = False 
        self.canvas = Canvas(
          window, 
          bg = "white", 
          width = width, 
          height = height
        )
        self.create_grid()
        # Bind canvas with key events
        self.canvas.bind("<Button 1>", self.origin)
        self.canvas.focus_set()

        self.x = width / 2
        self.y = height / 2
        window.mainloop() # Create an event loop

    def create_grid(self):
      for y in range(1, 11):
        self.canvas.create_line(0, y*grid_prop, 300, y*grid_prop)
        self.canvas.create_line(y*grid_prop, 0, y*grid_prop, 300)
      self.canvas.pack()

    def win(self, time_taken=None):
      self.canvas.delete("all")
      self.canvas.create_text(width/2, height/2, text = f"You have won! \nTime: {time_taken}", font=(None, 15))
      self.canvas.pack()

    def check_win(self):
      pass

    def generate_bombs(self, x, y):
      while self.grid.count(9) < 15:
        try:
          self.grid[random.randint(0,100)] = 9
        except: 
          pass
      temp = []
      for chunk in range(0, len(self.grid), 10):
        temp.append(self.grid[chunk:chunk+10])
      self.grid = temp

      for row_ind, row in enumerate(self.grid):
        for col_ind, col in enumerate(row):
          count = 0
          print(row)
          print(col)
          curr = self.grid[row_ind][col_ind]
          if curr != 9:
            if col_ind != 9 and self.grid[row_ind][col_ind + 1] == 9:
              count += 1
            if col_ind != 0 and self.grid[row_ind][col_ind - 1] == 9:
              count += 1
            if row_ind != 0 and self.grid[row_ind-1][col_ind] == 9:
              count += 1
            if row_ind != 9 and self.grid[row_ind+1][col_ind] == 9:
              count += 1
            if col_ind != 9: # check right diags
              if row_ind != 9 and self.grid[row_ind+1][col_ind+1] == 9:
                count + 1
              if row_ind != 0 and self.grid[row_ind-1][col_ind+1] == 9:
                count + 1
            if col_ind != 0: # check left diags
              if row_ind != 0 and self.grid[row_ind-1][col_ind-1] == 9:
                count + 1
              if row_ind != 9 and self.grid[row_ind-1][col_ind-1] == 9:
                count + 1
              
          else:
            count = 9

          self.grid[row_ind][col_ind] = count
          print(self.grid)
      
  
    def place(self, x, y, start):
      print(x, y)
      gridx, gridy = x//grid_prop, y//grid_prop
      
      if start: 
        self.generate_bombs(gridx, gridy)
      for y_ind, y in enumerate(self.grid):
        for x_ind, x in enumerate(y):
          print(x, y, x_ind, y_ind)
          self.canvas.create_text(
            x_ind*grid_prop + grid_prop//2, # X-COORD
            y_ind*grid_prop + grid_prop//2, # Y-COORD
            text = self.grid[y_ind][x_ind], # TEXT
            font=(None, font))
      
      self.canvas.pack()
          
      """count = 0
      returner = ""
      if not start:
        for i in range(10,301,grid_prop):
          if y <= i :
            ind = math.ceil(i//grid_prop) - 1
            
            if grid[ind][math.ceil(x//grid_prop)-1] == "   ":
              grid[ind][math.ceil(x//grid_prop)-1] = turn
            else:
              break
            break
      for y in range(1,10):
        for x in range(1,10):
          self.canvas.create_text(x*grid_prop+grid_prop//2, y*grid_prop+grid_prop//2, text = grid[y-1][x-1], font=(None, font))
      
      self.create_grid()
      self.canvas.create_text(txt_x, txt_y, text = returner, font=(None, font))
      self.canvas.pack()
      self.check_win()"""
        
    def origin(self, event): # Triggers when user clicks
      #self.canvas.delete("all")
      self.place(event.x, event.y, not self.clicked)
      self.clicked = True

MainGUI()
