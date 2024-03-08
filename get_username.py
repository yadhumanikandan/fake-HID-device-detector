import os



default_username = os.getlogin()
if default_username:
    print("Default username:", default_username)
else:
    print("Unable to determine default username.")
