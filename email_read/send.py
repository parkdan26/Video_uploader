import time
import smtplib
import datetime
from shutil import copyfile
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



YOU = "parkdan26@gmail.com"
PASS = "kebo coao ngjl ywhb"
TARGET = "sungeunp623@gmail.com"

SUBJECT = "TESTING"
subject_short = SUBJECT.replace(' ', '-')
LINK = "https://parkdan26.pythonanywhere.com/static/download.jpeg"

curr_time = datetime.datetime.now()
time_string = curr_time.strftime("%m-%d-%Y/%H-%M-%S")

max_subject_len = 30
if len(subject_short) > max_subject_len:
    subject_short = subject_short[0:max_subject_len-3] + "..."

html = f"""\
<html>
  <head></head>
  <body>
    <p>TESTING<br>
       <br>
       <img src="{LINK}">
    </p>
  </body>
</html>
"""
html.format(LINK)
print(html)
server = smtplib.SMTP('smtp.gmail.com' , 587)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(YOU, PASS)

msg = MIMEMultipart('alternative')
msg['Subject'] = SUBJECT
msg['From'] = YOU
msg['To'] = TARGET
text = ""
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')
msg.attach(part1)
msg.attach(part2)
server.sendmail(YOU, TARGET, msg.as_string())
server.quit()