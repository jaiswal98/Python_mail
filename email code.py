"""
    The first step is to create an SMTP object, each object is used for connection 
    with one server.
"""

import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

#Next, log in to the server
server.login("#email_id", "passwd")

em=input("Enter your email")

#Send the mail
msg = "Welcome to python session!!!" 
server.sendmail("#email_id",em, msg)
print("done!!!")

