import logging
import logging.config
from .process_setting import ProcessSetting

path_setting = ProcessSetting()
logging.config.fileConfig(path_setting.logger_config)


class Logger:
    def __init__(self):
        self.main_logger = logging.getLogger("MainLogger")
        self.error_logger = logging.getLogger("ErrorLogger")


    def log_info(self, msg: str):
        self.main_logger.info(msg=msg)

    def log_warning(self, msg: str):
        self.main_logger.warning(msg=msg)

    def log_error(self, msg: str):
        self.error_logger.error(msg=msg)

