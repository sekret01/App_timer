
class ProcessSetting:
    """Class with main settings of paths"""
    def __init__(self):
        self.config_path: str = "app_timer/configs/config.ini"
        self.ignore_process_path: str = "app_timer/data/ignore_process.json"
        self.tracked_process_path: str = "app_timer/data/tracked_process.json"
        self.logs_path: str = "app_timer/logs/logs.log"
        self.save_file_path: str = "save_time/"

    def set_ignores_path(self, path):
        self.ignore_process_path = path

    def set_tracked_path(self, path):
        self.tracked_process_path = path

    def set_save_file_path(self, path):
        self.save_file_path = path

    def set_default_path(self):
        """Set default paths"""
        self.config_path: str = "app_timer/configs/config.ini"
        self.ignore_process_path: str = "app_timer/data/ignore_process.json"
        self.tracked_process_path: str = "app_timer/data/tracked_process.json"
        self.logs_path: str = "app_timer/logs/logs.log"
        self.save_file_path: str = "save_time/"
