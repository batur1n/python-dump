import smtplib
from email.MIMEText import MIMEText

me = 'misha.baturin@gmail.com'
you = 'fluoritius@gmail.com'
text = 'Test mail! Sending mail from python.'
subj = 'Test'

server = "aspmx.l.google.com"
port = 587 
user_name = "misha.baturin@gmail.com"
user_passwd = "c,xvr510-YeS"

msg = MIMEText(text, "", "utf-8")
msg['Subject'] = subj
msg['From'] = me
msg['To'] = you

s = smtplib.SMTP(server, port)
s.ehlo()
s.starttls()
s.ehlo()
s.login(user_name, user_passwd)
s.sendmail(me, you, msg.as_string())

s.quit()
