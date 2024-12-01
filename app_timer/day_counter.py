from datetime import datetime
import pickle
from app_timer import ProcessInfoDict
from .logger import Logger
from .set_configs import get_configs, update_configs


class ObserverOfDays:
    def __init__(self):
        self.config = get_configs()
        self.logger = Logger()

    def get_day_now(self) -> str:
        date_now = datetime.now()
        str_date_now = f"{date_now.day}.{date_now.month}.{date_now.year}"
        return str_date_now

    def read_configs(self):
        self.config = get_configs()


    def is_new_day(self):
        self.read_configs()
        str_date_now = self.get_day_now()
        str_last_date = self.config["TIMES"]["last_day"]
        return str_date_now != str_last_date

    def save_day_information(self, save_object: ProcessInfoDict):
        with open(self.config["PATHS"]["day_info_file"], "wb") as file:
            pickle.dump(save_object, file)
            self.logger.log_info(f"{__name__} file day-save has been saved")

    def load_day_information(self) -> ProcessInfoDict:
        try:
            with open(self.config["PATHS"]["day_info_file"], "rb") as file:
                process_dict = pickle.load(file)
                return process_dict

        except EOFError:
            self.logger.log_info(f"{__name__} file day-save was empty")
            return ProcessInfoDict()

        except FileNotFoundError:
            self.logger.log_error(f"{__name__} file {self.config["PATHS"]["day_info_file"]} not found")
            self.logger.log_info(f"{__name__} create new file to day-save")
            with open(self.config["PATHS"]["day_info_file"], "w") as file:
                pass
            return ProcessInfoDict()

