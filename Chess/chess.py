"""
This is chess!!!
Note: Console version of chess for now :D
Many features of chess have not been added in this version.
View my chess repo on github to view the complete chess game!
"""

from typing import Literal, Optional
import os
import time

class InvalidMove(Exception):
  pass

class Game:
  def __init__(self):
    self.board = [
      ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
      ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
      ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
      ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
      ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
      ["  ", "  ", "  ", "BP", "  ", "  ", "  ", "  "],
      ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
      ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"],
    ]
    self.turn = "white"
    self.moves = 0
    self.winner = None
    self.warning = ""
    self.letter_match = {
      "a": 0, 
      "b": 1, 
      "c": 2, 
      "d": 3, 
      "e": 4, 
      "f": 5, 
      "g": 6, 
      "h": 7
    }

  def get_actual_y(self, y):
    return 8 - int(y)

  def get_valid_moves(self, piece: str, curr_pos: str) -> list:
    """
    Returns a list of all valid moves the piece can make. (In list index format)
    """
    piece_x, piece_y = self.get_actual_y(curr_pos[1]), self.letter_match[curr_pos[0]]
    valid_moves = []

    # Check for pawn movement
    if piece[-1] == "P": # "P" in "WP"
      # Find valid pawn movements
      
      ## Find vert movements, define new_x and new_y as one position up/down depending on color
      new_x, new_y = (piece_x, piece_y-1) if piece[0] == "B" else (piece_x, piece_y+1)
      if self.board[new_y][new_x] == "  " and piece_x == new_x:
        valid_moves.append(f"{new_x}{new_y}")
        
      ## Check if pawn can move up 2 tiles (vertical first move)
      print(type(new_y), new_y, type(piece_y), piece_y)
      if piece[0] == "B": # check for white pieces
        # Check if it is moving up by 1 or 2 (if first move) (if 2, check if a piece is blocking)
        new_y = 1
        if new_y - piece_y == 2 and piece_y == 1 and self.board[piece_y + 1][piece_x] == "  ":
          valid_moves.append(f"{new_x}{new_y}")
      else: # check for black pieces
        new_y = 6
        if piece_y - new_y == 2 and piece_y == 6 and self.board[piece_y - 1][piece_x] == "  ":
          valid_moves.append(f"{new_x}{new_y}")
        
      ## Check diag movement (only valid if it can take another piece)
      # redefine new_x, new_y can be reused
      new_y = piece_y-1 if piece[0] == "B" else piece_y+1
      try:
        for new_x in (new_x-1, new_x+1):
          if self.board[new_y][new_x][0] not in (" ", piece[0]):
            valid_moves.append(f"{new_x}{new_y}")
      except IndexError:
        pass # when checking for diags, checks might go out of board

      print(valid_moves)
      return valid_moves

  def move(self, curr_pos: str, new_pos: str) -> None:
    """
    This function helps move a piece on the board

    curr_pos: the current position of the piece
    new_pos: the new position of the piece
    """

    # Get the piece type based on curr_pos (WR, WN, BP, etc)
    # Get x and y pos of pieces
    piece_y = self.get_actual_y(curr_pos[1])
    piece_x = self.letter_match[curr_pos[0]]
    new_y = self.get_actual_y(new_pos[1])
    new_x = self.letter_match[new_pos[0]]
    valid_move = False

    # Reset warning
    self.warning = ""
    
    piece_type = self.board[piece_y][piece_x]
    print(piece_type, piece_x, piece_y, new_x, (chr(ord(str(piece_x))+1), chr(ord(str(piece_x))-1)))

    valid_moves = self.get_valid_moves(piece_type, curr_pos)
        
    # Move the piece
    if 1 or valid_move: # added 1 for testing
      self.board[piece_y][piece_x] = "  "
      self.board[new_y][new_x] = piece_type#[0] + "P"
      return True
    self.warning = "That was an invalid move!"
    raise InvalidMove("Invalid Move!")

  def display(self):
    """
    This function displays the chess board
    """
    # Clear the console
    #os.system("clear")

    # Draw the board
    res = "  " + "-"*41 + "\n"
    for y, row in enumerate(self.board):
      res += f"{8 - y} |"
      for x in self.board[y]:
        res += f" {x} |"
      res += f"\n   {'-'*40} \n"

    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

    res += "  "
    for letter in letters:
      res += f"   {letter} "
    res += f"\n{self.warning}"
    return res

def main():
  game = Game()

  # Game Loop
  running = True
  while running:
    print(game.display())

    try:
      game.move(input("Enter piece to move: "), input("Enter coords to move to: "))
    except InvalidMove:
      print("Sorry, that was an invalid move!") # doesnt show for now as game.display clears the console
  
  time.sleep(20)

if __name__ == "__main__":
  main()
