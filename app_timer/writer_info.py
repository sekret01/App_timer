from .process_info_dict import ProcessInfoDict
from .formatter import JsonFormatter
from .logger import Logger
import json
import threading
import time


class WriterProcessInfo:
    """
    ...
    """
    def __init__(self, process_dict: ProcessInfoDict):
        self.process_dict = process_dict
        self.pause = 5
        self.formatter = JsonFormatter()
        self.writer_thr: threading.Thread = threading.Thread()
        self.work = True
        self.logger = Logger()

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

    def save_process_information(self):
        processes = self.process_dict.get_processes()
        processes_to_json = self.formatter.convert_process_info_to_json(processes)
        self.write_info(processes_to_json)

    def start_write(self):
        while self.work:
            time.sleep(self.pause)
            self.save_process_information()
        return

    def write_info(self, processes: dict[str: dict[str: str, str: bool]]) -> None:
        try:
            with open(self.process_dict.settings.save_file_path + 'test_data.json', 'w', encoding='utf-8') as file:
                json.dump(processes, file)
        except Exception as ex:
            self.logger.log_error(f"{__name__} :> {str(ex)}")


    def stop_write(self):
        self.work = False
        self.save_process_information()
        self.logger.log_info(f"{__name__} stop")




