import logging
import logging.config


logging.config.fileConfig("logging.conf")


class Logger:
    def __init__(self):
        self.error_logger = logging.getLogger("ErrorLogger")
        self.main_logger = logging.getLogger("MainLogger")

    def log_info(self, msg: str):
        self.main_logger.info(msg=msg)

    def log_error(self, msg: str):
        self.main_logger.error(msg=msg)
        self.error_logger.error(msg=msg)

