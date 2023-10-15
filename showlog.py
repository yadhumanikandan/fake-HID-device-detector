import tkinter as tk
from tkinter import ttk
import json


with open("log.json", "r") as json_file:
    elements = json.load(json_file)


root = tk.Tk()
root.title("Log")
root.geometry("1000x600")

canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", on_frame_configure)

for element in reversed(elements):
    colour = "black"

    if element["suspected"] == True:
        colour = "red"

    empty_label = tk.Label(frame, text="", anchor='w', justify='left', padx=10, pady=5)
    empty_label.pack(side=tk.TOP, fill=tk.BOTH)
    label = tk.Label(frame, text="Event: "+element["event"], anchor='w', justify='left',fg=colour, padx=10, pady=5)
    label.pack(side=tk.TOP, fill=tk.BOTH)
    label = tk.Label(frame, text="Name: "+element["name"], anchor='w', justify='left',fg=colour, padx=10, pady=5)
    label.pack(side=tk.TOP, fill=tk.BOTH)
    label = tk.Label(frame, text="Time: "+element["time"], anchor='w', justify='left',fg=colour, padx=10, pady=5)
    label.pack(side=tk.TOP, fill=tk.BOTH)
    label = tk.Label(frame, text="PID: "+element["pid"], anchor='w', justify='left',fg=colour, padx=10, pady=5)
    label.pack(side=tk.TOP, fill=tk.BOTH)
    label = tk.Label(frame, text="VID: "+element["vid"], anchor='w', justify='left',fg=colour, padx=10, pady=5)
    label.pack(side=tk.TOP, fill=tk.BOTH)
    empty_label = tk.Label(frame, text="", anchor='w', justify='left', padx=10, pady=5)
    empty_label.pack(side=tk.TOP, fill=tk.BOTH)
    separator = ttk.Separator(frame, orient="horizontal")
    separator.pack(side=tk.TOP, fill=tk.BOTH)

root.mainloop()

