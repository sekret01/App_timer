import configparser


class ProcessSetting:
    """Class with main settings of paths"""
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.config_path: str = "app_timer/configs/config.ini"
        self.ignore_process_path: str = ""
        self.tracked_process_path: str = ""
        self.logs_path: str = ""
        self.save_file_path: str = ""
        self.logger_config = ""
        self.last_day = ""
        self.write_pause = 10

        self.update_setting()

    def update_setting(self):
        self.conf.read("app_timer/configs/config.ini")
        self.ignore_process_path: str = self.conf["PATHS"]["ignore_process_path"]
        self.tracked_process_path: str = self.conf["PATHS"]["tracked_process_path"]
        self.logs_path: str = self.conf["PATHS"]["logs_path"]
        self.save_file_path: str = self.conf["PATHS"]["save_file_path"]
        self.logger_config = self.conf["PATHS"]["logger_config"]
        self.last_day = self.conf["TIMES"]["last_day"]
        self.write_pause = self.conf["TIMES"]["write_pause"]
