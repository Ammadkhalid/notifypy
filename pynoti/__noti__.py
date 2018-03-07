from .notify import Notify
from .mailer import Gmail

def sendNoti(user, passwd, to, title, message = None):
    noti = Notify(user, passwd)

    noti.sendNotification(to, title, message)
