# fake HID device detector

import subprocess
import json
import datetime


def search_usb():
    command = "dmesg | grep -i hid-generic"

    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode == 0:
        output = result.stdout
        process(output, current_time)

    else:
        error_message = result.stderr
        print(error_message)



def process(output, time):                       ## process the command output

    output_lines =output.strip().split('\n')

    log_data = []

    existing_events = []

    with open('log.json', 'r') as json_file:
        log = json.load(json_file)

    # Check if the file has data
    if log:
        # for entry in log:
        #     event = entry.get("event")
        #     if event is not None:
        #         existing_data.append(event)                     # read all existing log to program
        
        existing_events = [d["event"] for d in log]

        difference = [event for event in output_lines if event not in existing_events]

        # difference = list(set(output_lines) - set(existing_events))       #find its difference

        # log_data = []

        # for line in existing_events:
        #     log_data.append({"event": line})
        
        # for line in difference:
        #     log_data.append({"event": line})

        # current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Append events to list_of_dicts with the current time
        for event in difference:
            new_dict = {"event": event, "time": time}
            log.append(new_dict)


        with open('log.json', 'w') as json_file:
            json.dump(log, json_file, indent=4)

    else:
        for line in output_lines:
            log_data.append({"event": line, "time": time})

        with open('log.json', 'w') as json_file:
            json.dump(log_data, json_file, indent=4)



while True:
    search_usb()