#!/usr/bin/python
#sending mail
import smtplib
fromaddr = '@gmail.com'
toaddrs  = '@gmail.com'
msg = 'hello!'
username = '@gmail.com'
password = ''
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
