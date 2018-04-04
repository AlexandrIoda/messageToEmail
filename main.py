import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header
import email
import os

mail_from   = "dhcptester@gmail.com" # отправитель
mail_to     = "sashaioda12345@gmail.com"  # получатель
mail_text   = 'Hello!!!' # текст письма
mail_subj   = 'Тестовое письмо' # заголовок письма
mail_coding = 'windows-1251'
attach_file = '/home/mrRobot/Документы/lol.png' # прикрепляемый файл

smtp_server = "smtp.gmail.com"
smtp_port   = 587
smtp_user   = "dhcptester@gmail.com" # пользователь smtp
smtp_pwd    = "beGITeglypcy" # пароль smtp

#формирование письма
multi_msg = MIMEMultipart()
multi_msg['From'] = Header(mail_from, mail_coding)
multi_msg['To'] = Header(mail_to, mail_coding)
multi_msg['Subject'] = Header(mail_subj, mail_coding)

msg = MIMEText(mail_text.encode('cp1251'), 'plain', mail_coding)
msg.set_charset(mail_coding)
multi_msg.attach(msg)

#прикрепление файла
if(os.path.exists(attach_file) and os.path.isfile(attach_file)):
    file = open(attach_file, 'rb')
    attachment = MIMEBase('application', "octet-stream")
    attachment.set_payload(file.read())
    email.encoders.encode_base64(attachment)
    file.close()
    only_name_attach = Header(os.path.basename(attach_file),mail_coding);
    attachment.add_header('Content-Disposition','attachment; filename="%s"' % only_name_attach)
    multi_msg.attach(attachment)
else:
    if(attach_file.lstrip() != ""):
        print("Файл для атача не найден - " + attach_file)

smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.ehlo()
smtp.starttls()
smtp.ehlo()
smtp.login(smtp_user, smtp_pwd)
smtp.sendmail(mail_from, mail_to, multi_msg.as_string())
smtp.quit()
