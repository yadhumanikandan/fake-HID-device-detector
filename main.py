import subprocess


def cmd():
    # Your terminal command as a string
    command = "dmesg | grep -i hid"

    # Run the command and capture the result
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        # Command was successful, capture the output
        output = result.stdout
        print("Command Output:")
        #print(output)
        check(output)

    else:
        # Command failed, capture the error message
        error_message = result.stderr
        print("Command Error:")
        print(error_message)




def check(out):
    
    suspected = "pico"

    if suspected in out:
        print("found !!!!")
    else:
        print("not found !!!")

cmd()
