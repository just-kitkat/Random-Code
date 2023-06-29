import os
username = os.getenv("REPL_OWNER")
print(f"Your username is {username if username != '' else 'not defined as you are not logged in'}!")