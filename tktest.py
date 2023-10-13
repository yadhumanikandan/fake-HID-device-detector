import tkinter as tk

# Function to close the message window
def close_message_window():
    message_window.destroy()

# Create the main window
root = tk.Tk()
root.title("Message Window Example")

# Create a label with the message
message_label = tk.Label(root, text="This is a message.")
message_label.pack(pady=20)

# Create a button at the bottom to close the window
close_button = tk.Button(root, text="OK", command=close_message_window)
close_button.pack(pady=10)

# Run the tkinter main loop
root.mainloop()