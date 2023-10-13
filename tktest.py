import tkinter as tk
import subprocess

# Function to close the message window
def close_message_window():
    command = "python3 /home/manik/project/cp/tktest.py"
    root.destroy()
    subprocess.run(command, shell=True)

# Create the main window
root = tk.Tk()
root.title("Message Window Example")
root.geometry("400x150")  # Adjust the window size here (width x height)

# Create a label with the message
message_label = tk.Label(root, text="This is a message.", fg="red", font=("Helvetica", 18))
message_label.pack(pady=25)  # Increase pady for more space

# Create a button at the bottom to close the window
close_button = tk.Button(root, text="OK", command=close_message_window, width=10, height=3)
close_button.pack(pady=10)  # Increase pady for more space

# Run the tkinter main loop
root.mainloop()
