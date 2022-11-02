from tkinter import *
import random
import time, asyncio

width, height = 300, 300
class Gui:
  def __init__(self):
    self.window = Tk() # Create a self.window
    self.window.title("Sorting Animation") # Set a title
    self.check = True
    self.bars = []
    for i in range(150):
      self.bars.append(random.randint(4, height))
    self.canvas = Canvas(
      self.window, 
      bg = "white", 
      width = width, 
      height = height
    )
    self.canvas.create_text(width, height, text = "Click anywhere to begin")
    self.canvas.pack()
    # Bind canvas with key events
    self.canvas.bind("<Button 1>", self.origin)
    self.canvas.focus_set()

    self.width = width
    self.height = height
    self.x = width / 2
    self.y = height / 2
     # Create an event loop
  def tk_sleep(self, delay):
    v = self.window.IntVar()
    # update variable "delay" ms later
    self.window.after(delay, v.set, 0)
    # wait for update of variable
    self.window.wait_variable(v)
  def bubble_sort(self):
    check = 1
    count = 0
    while check != 0:
      check = 0
      for i in range(len(self.bars)-1):
        print(self.bars)
        if self.bars[i] > self.bars[i+1]:
          check += 1
          temp = self.bars[i] 
          self.bars[i] = self.bars[i+1]
          self.bars[i+1] = temp
          self.generate_bars()
          count += 1
          print(count)
          print("B")

  def insertion_sort(self):
    for step in range(1, len(self.bars)):
      key = self.bars[step]
      j = step - 1
      # Compare key with each element on the left of it until an element smaller than it is found
      # For descending order, change key<self.bars[j] to key>self.bars[j].        
      while j >= 0 and key < self.bars[j]:
          self.bars[j + 1] = self.bars[j]
          j = j - 1
      self.generate_bars()
      # Place key at after the element just smaller than it.
      self.bars[j + 1] = key
  def generate_bars(self):
    print(self.bars)
    self.canvas.delete("all")
    for i in self.bars:
      self.create_bar(self.bars.index(i))
    self.canvas.pack()
    print("PACKED \n\n\n\n\n\n\n\n\n\nPACKED")
    

  def create_bar(self, i):
    height = self.bars[i]
    width = 2
    self.bars[i] = height
    self.canvas.create_rectangle(i*2, self.height, i*2 + width, height, outline="#fb0", fill="#fb0") # Creates a rect (x1, y1, x2, y2)

  def start_sort(self):
    for i in self.bars:
      self.insertion_sort()

  def origin(self, event): # Triggers when user clicks
    print(self.bars)
    self.canvas.delete("all")
    if self.check:
      self.check = not self.check
      self.bars = [random.randint(2, self.height) for i in range(150)]
      self.generate_bars()
    else:
      self.start_sort()
    self.canvas.pack()
    

gui = Gui()
gui.generate_bars()
mainloop()