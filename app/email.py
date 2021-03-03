from flask import render_template
from flask_mail import Message
from app import mail, app
 
def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

def send_email_login(user):
    send_email('[Lab7] Welcom login',
    sender='demo@mail.com',
    recipients=[user],
    text_body=render_template('email/send_mail_login.txt',
    user=user),
    html_body=render_template('email/send_mail_login.html',
    user=user))