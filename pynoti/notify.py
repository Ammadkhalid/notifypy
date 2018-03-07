from .mailer import Gmail

class Notify:
    def __init__(self, email, passwd):
        # mailer
        self.mailer = Gmail(email, passwd)

    def sendNotification(self, to, title, message):
        # send notification now
        chk = self.mailer.sendMsg(to, title, message)

        if chk:
            return True
