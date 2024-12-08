import configparser


class ControlApp:
    def __init__(self):
        self.config_path = "app_timer/configs/status_config.ini"
        self.config = configparser.ConfigParser()

    def _read_config(self):
        self.config.read(self.config_path)

    def _save_config(self):
        with open(self.config_path, 'w', encoding='utf-8') as file:
            self.config.write(file)


    def is_stop_program(self) -> bool:
        self._read_config()
        stop_command = int(self.config["COMMANDS"]["stop"])
        if stop_command: return True
        return False

    def set_error_status(self, er_status: int = 0):
        self._read_config()
        self.config["WORK_STATUS"]["error"] = str(er_status)
        self._save_config()

    def set_error_message(self, er_msg: str = ''):
        self._read_config()
        self.config["ERRORS"]["error_message"] = er_msg
        self._save_config()

    def set_work_status(self, work_status: int = 0):
        self._read_config()
        self.config["WORK_STATUS"]["working"] = str(work_status)
        self._save_config()

    def set_command_stop(self, stop: int = 0):
        self._read_config()
        self.config["COMMANDS"]["stop"] = str(stop)
        self._save_config()
