def shift(char):
# Shifts lowercase letter down by one position: a → b ... y → z → a
# Does nothing to other characters.
    if char == 'z':
        return 'a'
    elif char.islower():
        return chr(ord(char) + 1)
    else:
        return char

def encrypt(message, position):
  for i in list(message):
    
  