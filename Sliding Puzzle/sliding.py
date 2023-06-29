"""
This is a simple version of a sliding puzzle game using TKinter. 

I coded this simplified version to get an idea on how the game 
will look like and function, before rewriting it using kivy. 

The rewritten version has more features like animations and art, 
and is available on Windows and Android. The final game is available 
in my Sliding Puzzle repo on github.

How to play: 
    Use arrow keys to move the tiles, slide them in numerical order, 
    with the empty space at the bottom right corner.
"""
from tkinter import * # Import tkinter
import time
import random
print("Sliding Puzzle starting...")
print("This is a simplified version, read docstring in source code (sliding.py) for more info")
width = 200
height = 200

def getInvCount(arr):
    inv_count = 0
    empty_value = -1
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count
 
     
# This function returns true
# if given 8 puzzle is solvable.
def isSolvable(puzzle) :
 
    # Count inversions in given 8 puzzle
    inv_count = getInvCount([j for sub in puzzle for j in sub])
 
    # return true if inversion count is even.
    return (inv_count % 2 == 0)



class MainGUI:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Sliding Puzzle") # Set a title

        self.canvas = Canvas(window, bg = "white", width = width, height = height)
        self.canvas.pack()
        self.start_time = 0
        self.grid = [[],[],[]]
        
        self.gridder(self.grid, True, "start")
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

        #self.canvas.delete('all')
        #self.canvas.create_text(100, 100, text = gridder(grid, False, "up"), font=(None, 15))
        #self.canvas.pack()

    def checker(self, puzzle, t):
        for i in range(3):
            try:
                c = puzzle[i].index(-1)
            
                if t == "up" and i > 0:
                    puzzle[i][c] = puzzle[i-1][c]
                    puzzle[i-1][c] = -1
                elif t == "down":
                    puzzle[i][c] = puzzle[i+1][c]
                    puzzle[i+1][c] = -1
                    break
                
                elif t == "left" and c > 0:
                    puzzle[i][c] = puzzle[i][c-1]
                    puzzle[i][c-1] = -1
                elif t == "right":
                    puzzle[i][c] = puzzle[i][c+1]
                    puzzle[i][c+1] = -1
            except Exception as e:
                pass
        x = self.check_win(puzzle)
        if x == True:
            return x
            
        return puzzle

    def gridder(self, puzzle, type, t):
        print("RUNNING: t status:", t)
        text = ""
        if type:
            iter = 0
            while True:
                iter += 1
                dump = [1,2,3,4,5,6,7,8,-1]
                puzzle = [[],[],[]]
                for i in range(3):
                    for a in range(3):
                        temp = random.choice(dump)
                        puzzle[i].append(temp)
                        dump.remove(temp)
                if isSolvable(puzzle):
                    print("Iter:", iter)
                    self.grid = puzzle
                    print(isSolvable(puzzle))
                    break
            self.start_time = time.time()
            print(puzzle, isSolvable(self.grid))
        else:
            puzzle = self.checker(puzzle, t)
            if puzzle == True:
                self.canvas.delete('all')
                self.canvas.create_text(width//2, height//2, text = f"YOU WIN!!! \nTime taken: {round((time.time() - self.start_time), 2)}s", font=(None, 12))
                self.canvas.pack()
                print(f"YOU WIN!!! \nTime taken: {round((time.time() - self.start_time), 2)}")
                return
        self.canvas.delete('all')
        self.create_grid(width, height)
        for item in range(3):
            for i in range(3):
                self.generate_num(item, i)
        self.canvas.pack()
        print(isSolvable(self.grid))

        text += "\n"
        self.grid = puzzle
        print(self.grid)
        return text

    def create_grid(self, width, height):
        for y in range(3):
            self.canvas.create_line(0, y*width//3, height, y*width//3)
            self.canvas.create_line(y*height//3, 0, y*height//3, width)

    def generate_num(self, y, x):
        self.canvas.create_text(x*width//3 + width//6, y*height//3 + height//6, text = self.grid[y][x] if self.grid[y][x] > 0 else " ", font=(None, 30))

    def check_win(self, grid):
        return grid == [[1, 2, 3], [4, 5, 6], [7, 8, -1]]
  
    def up(self, event):
        self.gridder(self.grid, False, "up")

    def down(self, event):
        self.gridder(self.grid, False, "down")

    def left(self, event):
        self.gridder(self.grid, False, "left")

    def right(self, event):
        self.gridder(self.grid, False, "right")

MainGUI()