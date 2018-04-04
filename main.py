import smtplib

sender = "dhcptester@gmail.com"  #Email of sender
psw = "beGITeglypcy"  #password
recipient = ["budkomaximidu55555@gmail.com", "sashaioda12345@gmail.com"]  #Email of recipients
message = "Hello my dear friend!"  #message

server = smtplib.SMTP("smtp.gmail.com", 587) #connecting with email server
server.starttls() #encryption
server.login(sender, psw)
server.sendmail(sender, recipient, message) #send to email
server.quit()
