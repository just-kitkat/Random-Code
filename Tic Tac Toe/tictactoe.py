from tkinter import * # Bad code but meh :/
import math, time
print("starting")
width = 300
height = 300
font = 48
txt_x, txt_y = 155, 190
turn = "X"
grid = [["   ", "   ", "   "], ["   ", "   ", "   "], ["   ", "   ", "   "]]
win_con = [[0,1,2], [3,4,5], [6,7,8], [0,4,8], [2,4,6], [0,3,6], [1,4,7], [2,5,8]]

class MainGUI:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Tic Tac Toe") # Set a title

        self.canvas = Canvas(
          window, 
          bg = "white", 
          width = width, 
          height = height
        )
        self.create_grid()
        self.canvas.pack()
        self.gridder(0,0,True)
        # Bind canvas with key events
        self.canvas.bind("<Button 1>", self.origin)
        self.canvas.focus_set()

        self.x = width / 2
        self.y = height / 2
        window.mainloop() # Create an event loop

    def create_grid(self):
      for y in range(1, 4):
        self.canvas.create_line(0, y* 100, 300, y*100)
        self.canvas.create_line(y * 100, 0, y * 100, 300)

    def win(self, winner):
      self.canvas.delete("all")
      self.canvas.create_text(width/2, height/2, text = f"{winner} has won!!! \nThank you for playing :D", font=(None, 15))
      self.canvas.pack()

    def check_win(self):
      global grid
      check = 0
      temp = grid[0] + grid[1] + grid[2]
      for win in win_con:
        if temp[win[0]] == "X" and temp[win[1]] == "X" and temp[win[2]] == "X": self.win("X")
        elif temp[win[0]] == "O" and temp[win[1]] == "O" and temp[win[2]] == "O": self.win("O")
        
        else: pass

    def gridder(self, x, y, start):
      print(x, y)
      global grid, turn
      count = 0
      returner = ""
      if not start:
        for i in range(100,301,100):
          if y <= i :
            ind = math.ceil(i/100) - 1
            
            if grid[ind][math.ceil(x/100)-1] == "   ":
              grid[ind][math.ceil(x/100)-1] = turn 
              turn = "X" if turn == "O" else "O"
            else:
              break
            break
      for y in range(1,4):
        for x in range(1,4):
          self.canvas.create_text(x*100 - 50, y*100 - 50, text = grid[y-1][x-1], font=(None, font))
      
      self.create_grid()
      self.canvas.create_text(txt_x, txt_y, text = returner, font=(None, font))
      self.canvas.pack()
      self.check_win()
        
    def origin(self, event): # Triggers when user clicks
      self.canvas.delete("all")
      self.gridder(event.x, event.y, False)

MainGUI()
