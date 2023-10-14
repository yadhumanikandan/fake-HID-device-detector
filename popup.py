import tkinter as tk
import subprocess


def popup():
    # Function to close the message window
    def close_message_window():
        command = "python3 /home/manik/project/cp/tktest.py"            ### command to change
        root.destroy()
        subprocess.run(command, shell=True)

    # Create the main window
    root = tk.Tk()
    root.title("Device detected")
    root.geometry("400x150")  # Adjust the window size here (width x height)

    # Create a label with the message
    message_label = tk.Label(root, text="A suspected device has\n been connected", fg="red", font=("Helvetica", 18))
    message_label.pack(pady=25)  # Increase pady for more space

    # Create a button at the bottom to close the window
    close_button = tk.Button(root, text="Show Log", command=close_message_window, width=10, height=3)
    close_button.pack(pady=10)  # Increase pady for more space

    # Run the tkinter main loop
    root.mainloop()


if __name__ == "__main__":
    popup()