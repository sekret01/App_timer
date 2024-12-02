from .process_info_dict import ProcessInfoDict
from .formatter import JsonFormatter
from .logger import Logger
from .day_counter import ObserverOfDays
import json
import threading
import time
from .process_setting import ProcessSetting


class WriterProcessInfo:
    """
    ...
    """
    def __init__(self, process_dict: ProcessInfoDict):
        self.setting = ProcessSetting()
        self.logger = Logger()
        self.formatter = JsonFormatter()
        self.writer_thr: threading.Thread = threading.Thread()

        self.process_dict = process_dict
        self.work = True
        self.pause = int(self.setting.write_pause)
        self.last_day = self.setting.last_day

    def run(self):
        self.writer_thr = threading.Thread(name="writer process info thread",
                                           target=self.start_write,
                                           daemon=True)
        self.work = True
        try:
            self.writer_thr.start()
            self.logger.log_info(f"{__name__} run")
        except Exception as ex:
            self.logger.log_error(f"{__name__} :> {str(ex)}")
            self.work = False

    def check_new_day(self):
        if ObserverOfDays().is_new_day():
            self.last_day = ObserverOfDays().get_day_now()

    def save_process_information(self):
        processes = self.process_dict.get_processes()
        processes_to_json = self.formatter.convert_process_info_to_json(processes)
        self.write_info(processes_to_json)

    def start_write(self):
        while self.work:
            time.sleep(self.pause)
            self.check_new_day()
            self.save_process_information()
        return

    def write_info(self, processes: dict[str: dict[str: str, str: bool]]) -> None:
            try:
                with open(self.process_dict.settings.save_file_path, 'r', encoding='utf-8') as file:
                    old_data = json.load(file)
                    old_data[self.last_day] = processes

            except json.JSONDecodeError:
                    old_data = {self.last_day: processes}
                    self.logger.log_info(f"{__name__} json time-data was empty")

            except Exception as ex:
                self.logger.log_error(f"{__name__} :> {str(ex)}")
                return

            with open(self.process_dict.settings.save_file_path, 'w', encoding='utf-8') as file:
                json.dump(old_data, file)


    def stop_write(self):
        self.work = False
        self.save_process_information()
        self.logger.log_info(f"{__name__} stop")
