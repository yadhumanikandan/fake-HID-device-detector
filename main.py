import subprocess
import re
import json


def search_usb():
    # Your terminal command as a string
    command = "dmesg | grep -i hid-generic"

    # Run the command and capture the result
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        output = result.stdout
        process(output)

    else:
        error_message = result.stderr
        print(error_message)



def process(out):                       ## process the command output and timestamp

    output_lines =out.strip().split('\n')

    log_data = []

    existing_data = []

    with open('log.json', 'r') as json_file:
        log = json.load(json_file)

    # Check if the file has data
    if log:
        for entry in log:
            event = entry.get("event")
            if event is not None:
                existing_data.append(event)                     # read all existing log to program
        
        difference = list(set(output_lines) - set(existing_data))       #find its difference

        log_data = []

        for line in existing_data:
            log_data.append({"event": line})
        
        for line in difference:
            log_data.append({"event": line})


        with open('log.json', 'w') as json_file:
            json.dump(log_data, json_file, indent=4)

    else:
        for line in output_lines:
            log_data.append({"event": line})

        with open('log.json', 'w') as json_file:
            json.dump(log_data, json_file, indent=4)




search_usb()