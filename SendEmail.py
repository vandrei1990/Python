# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
class SendEmail:
    """SendEmail class can be used after an instantiantion as SendEmail('yourEmail','yourEmailpassword','RecepientEmail','subject') The instantiantion should be an outlook email"""
    def __init__(self,fromx,password,to,subject):
        msg = MIMEMultipart()
        # create and start mail server
        server = smtplib.SMTP('smtp-mail.outlook.com: 587')      
        server.starttls()
        # Login Credentials for sending the mail
        msg['From']=fromx
        msg['To']=to
        msg['Subject'] =subject
        password=password
        server.login(msg['From'], password)
         
         
        # send the message via the server.
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
                 