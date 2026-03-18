import smtplib

sender_email = "aarthimoorthi93@gmail.com"
receiver_email = "aarthi44899@gmail.com"
password = "your_app_password_here"

message = "Subject: Python Automation\n\nHello, this email was sent using Python."

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(sender_email, password)

server.sendmail(sender_email, receiver_email, message)

print("Email sent successfully")

server.quit()