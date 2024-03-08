import os

# def get_default_username():
#     return os.getlogin()

default_username = os.getlogin()
if default_username:
    print("Default username:", default_username)
else:
    print("Unable to determine default username.")
