import tkinter as tk
import subprocess
from showlog import show_logs

def popup(device_name):
    root = tk.Tk()
    root.title("Device detected")
    root.geometry("400x200")

    message_label = tk.Label(root, text="A suspected device has\n been connected\nname: "+device_name, fg="red", font=("Helvetica", 18))
    message_label.pack(pady=25)

    def close_message_window():
        root.destroy()
        show_logs()
        # command = "python3 /home/manik/project/cp/showlog.py"
        # subprocess.run(command, shell=True)

    close_button = tk.Button(root, text="Show Log", command=close_message_window, width=10, height=3)
    close_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    popup()
