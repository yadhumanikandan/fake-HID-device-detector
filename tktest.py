import tkinter as tk
from tkinter import messagebox

# Function to show the popup message
def show_popup_message():
    messagebox.showinfo("Popup Message", "This is a message.")
    
# Create the main window
root = tk.Tk()
root.title("Popup Message Example")

# Create a button to trigger the popup message
button = tk.Button(root, text="Show Popup Message", command=show_popup_message)
button.pack(pady=20)

# Run the tkinter main loop
root.mainloop()
