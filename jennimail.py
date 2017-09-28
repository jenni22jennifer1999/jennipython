#!/usr/bin/python
#sending mail using python.
import smtplib  #small message transfer protocol.
fromaddr = '@gmail.com'    #sender mail id.
toaddrs  = '@gmail.com'    #reciever mail id.
msg = 'hello!'  #message to be sent.
username = '@gmail.com'    #sender mail id.
password = ''    #sender's password.
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)     #command to login.
server.sendmail(fromaddr, toaddrs, msg)    #command to send the mail. 
server.quit()   #exit. 
