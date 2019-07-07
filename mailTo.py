end_attachment.py
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import argparse
 
### arguments created
parser = argparse.ArgumentParser()
parser.add_argument('fromx', help='From Email')
parser.add_argument('password', help='Password of your email account')
parser.add_argument('to', help='To [email] be sent')
 

args = parser.parse_args() 
 
#### 
 
 
# create message object instance
msg = MIMEMultipart()
 
 
# setup the parameters of the message
password = args.password
msg['From'] = args.fromx
msg['To'] = args.to
msg['Subject'] = "Hard coded subject"
 
# attach image to message body
#msg.attach(MIMEImage(file("google.jpg").read()))
 
 
# create server
server = smtplib.SMTP('smtp-mail.outlook.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
print("successfully sent email to %s:" % (msg['To']))


