import pwd

def get_default_username():
    try:
        # Get the UID of the home directory
        home_dir = pwd.getpwuid(os.stat('/home')[stat.ST_UID]).pw_name
        return home_dir
    except KeyError:
        return None

default_username = get_default_username()
if default_username:
    print("Default username:", default_username)
else:
    print("Unable to determine default username.")
