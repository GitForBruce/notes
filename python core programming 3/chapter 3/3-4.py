# -*- coding: utf-8 -*-

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

SMTP_SERVER = 'smtp.163.com'
SENDER = 'google_he@163.com'
PASSWD = 'xxxxxx'
RECIPS = 'baoguo.he@gecenet.com', '13480479@qq.com'
SOME_IMG_FILE = 'Lanbo.jpg'

def make_mpa_msg():
    email = MIMEMultipart('alternative')
    text = MIMEText('Hello World!\r\n\n', 'plain')
    email.attach(text)
    html = MIMEText(
        '<html><body><h4>Hello World!</h4>'
        '</body></html>', 'html')
    email.attach(html)
    return email

def make_img_msg(fn):
    f = open(fn, 'rb')
    data = f.read()
    f.close()

    email = MIMEImage(data, name=fn)
    email.add_header('Content-Disposition', 'attachment; filename="%s"' % fn)
    return email

def send_msg(fr, to, msg):
    s = SMTP(SMTP_SERVER)
    s.login(SENDER, PASSWD)
    s.sendmail(fr, to, msg)
    s.quit()

if __name__ == '__main__':
    print('Sending multipart alternative msg...')
    msg = make_mpa_msg()
    msg['From'] = SENDER
    msg['To'] = ', '.join(RECIPS)
    msg['Subject'] = 'multipart alternative test'
    send_msg(SENDER, RECIPS, msg.as_string())

    print('Sending image msg...')
    msg = make_img_msg(SOME_IMG_FILE)
    msg['From'] = SENDER
    msg['To'] = ''.join(RECIPS)
    msg['Subject'] = 'image file test'
    send_msg(SENDER, RECIPS, msg.as_string())