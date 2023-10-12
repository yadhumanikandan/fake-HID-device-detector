import subprocess
import re
import json

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


# def checkExist():                       ## check if the log timestamp already exists




def process(out):                       ## process the command output and timestamp
    # print(out)
    # timestamp_pattern = r'\[(\s*\d+\.\d+)\]'

    output_lines =out.strip().split('\n')

    log_data = []

    with open('log.json', 'r') as json_file:
        data = json.load(json_file)

    # Check if the file has data
    if data:
        print("The JSON file has data.")
    else:
        for line in output_lines:
            # timestamp = re.search(timestamp_pattern, line).group(1)
            # log_message = line.split('] ')[-1]  # Extract the log message
            log_data.append({"event": line})



    # with open('log.json', 'w') as json_file:
    #     json.dump(log_data, json_file, indent=4)

    # timestamps = [re.search(timestamp_pattern, line).group(1) for line in output_lines]
    
    # for lines in output_lines:
        # print(lines + "\n\n")
        

    # print(timestamps)



# def write(log):
#     file_path = "log.txt"

#     with open(file_path, "a") as file:
#         file.write("\n\n" + log)

# while True:
#     search_usb()


search_usb()