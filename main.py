import smtplib

sender = "dhcptester@gmail.com"  # Email of sender
psw = "beGITeglypcy"  # password
recipient = ["budkomaximidu55555@gmail.com", "sashaioda12345@gmail.com"]  # Email of recipients
message = "Hello my dear friend!"  # message


def sendToEmail(sender, psw, recipient, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)

    try:
        server.starttls()
        server.login(sender, psw)
        server.sendmail(sender, recipient, message)

        return True
    except Exception as e:
        print("The message was not sent")
        print(e)
    finally:
        server.quit()

    return False


sendToEmail(sender, psw, recipient, message)
