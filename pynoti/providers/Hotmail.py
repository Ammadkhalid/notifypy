import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from ..ProviderInterface import ProviderInterface

class Hotmail(ProviderInterface):

    def __init__(self, user, password):
        self.user = user
        self.password = password
    
    def send(self, to, sub, msg):

        #Initialise message and headers
        message = MIMEMultipart('alternative')
        message['From'] = self.user
        message['To'] = to
        message['Subject'] = sub

        # Converts and attaches the HTML message
        html_msg = MIMEText(msg, 'html')
        message.attach(html_msg)

        # Initialise the connection and login user
        s = smtplib.SMTP('smtp.live.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(self.user, self.password)

        # Sends the email
        s.sendmail(self.user, to, message.as_string())
        s.quit()
        return True