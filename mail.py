import imaplib #imports imap package
import smtplib 
import json
from email.mime.multipart import MIMEMultipart




#sendmail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('USEREMAIL@GMAIL.COM', 'PASSWORD')




