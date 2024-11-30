import logging
import logging.config


logging.config.fileConfig("logger/logging.conf")


class Logger:
    def __init__(self):
        self.main_logger = logging.getLogger("MainLogger")
        self.error_logger = logging.getLogger("ErrorLogger")


    def log_info(self, msg: str):
        self.main_logger.info(msg=msg)

    def log_error(self, msg: str):
        self.error_logger.error(msg=msg)

l = Logger()
for i in range(-50, 50, 1):
    if i%2:
        l.log_info("all ok")
    else:
        l.log_error(f"{i} is not work")