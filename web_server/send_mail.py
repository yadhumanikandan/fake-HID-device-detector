import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email, subject, body, from_email="hiddetector@gmail.com", app_password="mvnkyahctkwaxami"):
    try:
        # Setting up the MIME structure
        msg = MIMEMultipart()
        msg["From"] = from_email
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Connect to Gmail SMTP server and send email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure connection
            server.login(from_email, app_password)
            server.sendmail(from_email, to_email, msg.as_string())

        print(f"Email sent successfully to {to_email}!")
    
    except Exception as e:
        print(f"Error sending email: {e}")


