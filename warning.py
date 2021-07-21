import sys
import smtplib
import time
import imaplib
import email
from tkinter import messagebox


def send(mails, name):
    username="*********@abc.com" //EXAMPLE MAIL
    password="*********"   //EXAMPLE PASSWORD
    remail=mails
    subject="Warning Regarding Violation of COVID-19 Guidelines"
    message="Hello "+name+", You have been advised to carry and wear your mask. As the entry is prohibited without the mask."
    finalmessage='Subject:{}\n\n{}'.format(subject,message)
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(username,password)
    server.sendmail(username,remail,finalmessage)
    server.quit()
    messagebox.showinfo(title='Email Client',message='Email Sent Successfully')