from .mailer import Mailer

class Notify:
    def __init__(self, email, passwd, provider):
        # mailer
        self.mailer = Mailer(email, passwd, provider = provider)

    def sendNotification(self, to, title, message):
        # send notification now
        chk = self.mailer.sendMsg(to, title, message)

        if chk:
            return True
