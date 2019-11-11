import smtplib

mailFrom = 'Your automation system'
mailTo = ['mails']
mailSubject = 'test'
mailBody = '''Hello 
Test mail 
Have nice day!'''
message = '''From: {}
Subject: {}

{}'''.format(mailFrom, mailSubject, mailBody)

user = 'user'
password = 'passwordg'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, mailTo, message)
    server.close()
except:
    print('wystapil blad')

