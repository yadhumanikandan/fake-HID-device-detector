# fake HID device detector

import subprocess
import json
import datetime
import re
import threading
from popup import popup



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


def extract(event):
    suspected = ["Raspberry Pi"]
    check = 0

    pattern = r"\[.*\] hid-generic (\w+:\w+:\w+\.\w+):.*\[(.*?)\] on .*"

    match = re.search(pattern, event)

    if match:
        device_id = match.group(1)
        print(device_id)
        device_name = match.group(2)
        p, vendor_id, product_id = device_id.split(':')
        product_id, p = product_id.split('.')

    for s in suspected:
        if s in event:
            check = 1
    
    if check == 0:
        return {"suspected": False, "name": device_name, "vid": vendor_id, "pid": product_id}
    else:
        return {"suspected": True, "name": device_name, "vid": vendor_id, "pid": product_id}


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
            data = extract(event)
            log.append({"event": event, "time": time, "name": data["name"], "suspected": data["suspected"], "vid": data["vid"], "pid": data["pid"]})
            if data["suspected"] == True:
                thread = threading.Thread(target=popup(data["name"]))
                thread.start()

        with open('log.json', 'w') as json_file:
            json.dump(log, json_file, indent=4)

    else:
        for event in output_lines:
            data = extract(event)
            log_data.append({"event": event, "time": time, "name": data["name"], "suspected": data["suspected"], "vid": data["vid"], "pid": data["pid"]})

        with open('log.json', 'w') as json_file:
            json.dump(log_data, json_file, indent=4)



def main():
    while True:
        search_usb()


if __name__ == "__main__":
    main()