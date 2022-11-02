from kivy.config import Config
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window

import random
import time
import math

class PuzzleGame(Widget):
    def __init__(self, **kwargs):
        super(PuzzleGame, self).__init__(**kwargs)
        self.width, self.height = Window.size
        self.font = self.width // 20
        self.start_time = 0
        self.moves = 0
        self.grid = [[],[],[]]
        self.started = False
        self.grid_text = {}
        self.starting = Label(pos = (self.width//2, self.height//2), text = "Click anywhere to start! \nGame by kitkat3141", font_size = self.font)
        self.add_widget(self.starting)

    def on_touch_down(self, touch):
        ori = touch.y
        touch.y = abs(self.height - touch.y)
        with self.canvas:
            self.clear_widgets()
            if not self.started:
                self.gridder(self.grid, True, "start")
                self.started = True
                self.moves = 0
            else:
                self.click(touch)

    def getInvCount(self, arr):
        inv_count = 0
        empty_value = -1
        for i in range(0, 9):
            for j in range(i + 1, 9):
                if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                    inv_count += 1
        return inv_count
    
        
    # This function returns true
    # if given 8 puzzle is solvable.
    def isSolvable(self, puzzle) :
    
        # Count inversions in given 8 puzzle
        inv_count = self.getInvCount([j for sub in puzzle for j in sub])
    
        # return true if inversion count is even.
        return (inv_count % 2 == 0)

    def checker(self, puzzle, t):
        for i in range(3):
            try:
                c = puzzle[i].index(-1)
            
                if t == "up" and i > 0:
                    puzzle[i][c] = puzzle[i-1][c]
                    puzzle[i-1][c] = -1
                    break
                elif t == "down":
                    puzzle[i][c] = puzzle[i+1][c]
                    puzzle[i+1][c] = -1
                    break
                
                elif t == "left" and c > 0:
                    puzzle[i][c] = puzzle[i][c-1]
                    puzzle[i][c-1] = -1
                    break
                elif t == "right":
                    puzzle[i][c] = puzzle[i][c+1]
                    puzzle[i][c+1] = -1
                    break
            except Exception as e:
                pass
        self.moves += 1
        x = self.check_win(puzzle)
        if x == True:
            return x
            
        return puzzle

    def gridder(self, puzzle, type, t):
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
                if self.isSolvable(puzzle):
                    self.grid = puzzle
                    break
            self.start_time = time.time()
        else:
            puzzle = self.checker(puzzle, t)
            if puzzle == True:
                for i in self.grid_text:
                    self.grid_text[str(i)].text = " " if i != "11" else f"YOU WIN!!! \nTime taken: {round((time.time() - self.start_time), 2)}s \nMoves made: {self.moves} \nClick anywhere to start a new game!"

                print(f"YOU WIN!!! \nTime taken: {round((time.time() - self.start_time), 2)} \nMoves made: {self.moves}")
                self.started = False
                return
        self.create_grid(self.width, self.height)
        first = True if self.grid_text == {} else False
        for item in range(3):
            for i in range(3):
                self.generate_num(item, i, first)

        text += "\n"
        self.grid = puzzle
        return text

    def create_grid(self, width, height):
        for y in range(3):
            pass
            #self.canvas.create_line(0, y*width//3, height, y*width//3)
            #self.canvas.create_line(y*height//3, 0, y*height//3, width)

    def generate_num(self, y, x, first):
        if first:
            self.grid_text[f"{x}{y}"] = Label(pos = (
                x*self.width//3 + self.width//9, 
                self.height - y*self.height//3 - self.height//4.5
            ), 
                text = str(self.grid[y][x]) if self.grid[y][x] > 0 else " ", 
                font_size = self.font)
        else:
            self.grid_text[f"{x}{y}"].text = str(self.grid[y][x]) if self.grid[y][x] > 0 else " "

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

    def click(self, event):
        x = math.ceil(event.x/(self.width//3)) - 1
        y = math.ceil(event.y/(self.height//3)) - 1
        for i in range(4):
            try:
                if i == 0 and self.grid[y][x+1] == -1:
                    self.left(None); break
                if i == 1 and self.grid[y][x-1] == -1:
                    self.right(None); break
                if i == 2 and self.grid[y+1][x] == -1:
                    self.up(None); break
                if i == 3 and self.grid[y-1][x] == -1:
                    self.down(None); break
            except Exception:
                pass



class PuzzleApp(App):
    def build(self):
        return PuzzleGame()


if __name__ == '__main__':
    PuzzleApp().run()