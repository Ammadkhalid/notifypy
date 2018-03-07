import logging
import os

class Logger:

    def __init__(self):
        self.formatter = 'At [%(asctime)s.%(msecs)03d] : [Level: %(levelname)s] : [%(filename)s:%(lineno)s%(funcName)20s()] : \n=======\n%(message)s\n======='
        self.dateFormate = "%Y-%m-%d %I:%m:%S %p"
        self.eFormatter = 'At [%(asctime)s.%(msecs)03d] : [Level: %(levelname)s] : [%(filename)s:%(lineno)s %(funcName)20s() ]\n=======Error Exception======='

    def create(self, name, filename, level=logging.DEBUG):
        if os.path.exists(filename):
            handler = logging.FileHandler(filename, "a")
        else:
            handler = logging.FileHandler(filename)

        # if programmer wants :D :p error level exception
        if name == 'bug' or name == 'bugs' or name == 'exception' or name == 'debug':
            formater = logging.Formatter(self.eFormatter, self.dateFormate)
        else:
            formater = logging.Formatter(self.formatter, self.dateFormate)
        handler.setFormatter(formater)

        # console logging
        console = logging.StreamHandler()
        # Set Level
        console.setLevel(logging.INFO)
        # add formatter
        console.setFormatter(formater)

        logger = logging.getLogger(name)

        # add console logger
        # logger.addHandler(console)
        # add file logger
        logger.addHandler(handler)


        logger.setLevel(level)

        return logger
