import notify2

# Initialize the notify2 library
notify2.init("Your App Name")

# Create a notification
notification = notify2.Notification("Title of the Notification", "Message of the Notification")

# Show the notification
notification.show()
