import subprocess
import re

output = ""

def search_usb():
    # Your terminal command as a string
    command = "dmesg | grep -i hid-generic"

    # Run the command and capture the result
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        # Command was successful, capture the output
        output = result.stdout
        #print("Command Output:")
        #print(output)
        process(output)

    else:
        # Command failed, capture the error message
        error_message = result.stderr
        #print("Command Error:")
        print(error_message)




def process(out):
    # print(out)
    output_lines =out.strip().split('\n')
    
    for lines in output_lines:
        print(lines + "\n\n")

    timestamp_pattern = r'\[(\s*\d+\.\d+)\]'

    timestamps = [re.search(timestamp_pattern, line).group(1) for line in output_lines]

    print(timestamps)



# def write(log):
#     file_path = "log.txt"

#     with open(file_path, "a") as file:
#         file.write("\n\n" + log)

# while True:
#     search_usb()


search_usb()