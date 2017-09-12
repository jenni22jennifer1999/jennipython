#!/usr/bin/python3
import smtplib
 
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("@gmail.com", "")
 
# message to be sent
message = ""
 
# sending the mail
s.sendmail("@gmail.com", "@gmail.com", message)
 
# terminating the session
s.quit()