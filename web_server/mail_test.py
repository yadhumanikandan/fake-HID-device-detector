import threading
from send_mail import send_email

subject = "Suspicious Activity Detected"
body = f"Alert! Suspicious activity detected."
to_email = "yadhumanikandan0@gmail.com"  # Change to actual recipient

# send_email(to_email, subject, body)

email_thread = threading.Thread(target=send_email, args=(to_email, subject, body))
email_thread.start()