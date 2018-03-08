from .notify import Notify
from .mailer import Gmail

def sendNoti(user, passwd, to, title, message = None, provider = 'none'):
    noti = Notify(user, passwd, provider)

    noti.sendNotification(to, title, message)
