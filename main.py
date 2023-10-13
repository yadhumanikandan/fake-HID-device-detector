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
        save(output, current_time)

    else:
        error_message = result.stderr
        print(error_message)


def checkEvent(event):
    suspected = ["Raspberry Pi"]

    if suspected in event:
        return True
    else:
        return False


def save(output, time):

    output_lines =output.strip().split('\n')

    log_data = []

    existing_events = []

    with open('log.json', 'r') as json_file:
        log = json.load(json_file)

    # Check if the file has data
    if log:        
        existing_events = [d["event"] for d in log]

        difference = [event for event in output_lines if event not in existing_events]

        for event in difference:
            new_dict = {"event": event, "time": time, "suspected": checkEvent(event)}
            log.append(new_dict)


        with open('log.json', 'w') as json_file:
            json.dump(log, json_file, indent=4)

    else:
        for event in output_lines:
            log_data.append({"event": event, "time": time, "suspected": checkEvent(event)})

        with open('log.json', 'w') as json_file:
            json.dump(log_data, json_file, indent=4)



while True:
    search_usb()