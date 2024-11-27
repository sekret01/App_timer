from .process_info_dict import ProcessInfoDict
from .formatter import JsonFormatter
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

    def run(self):
        self.writer_thr = threading.Thread(name="writer process info thread",
                                           target=self.start_write,
                                           daemon=True)
        self.work = True
        self.writer_thr.start()

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
        with open(self.process_dict.settings.save_file_path + 'test_data.json', 'w', encoding='utf-8') as file:
            json.dump(processes, file)


    def stop_write(self):
        self.work = False
        self.save_process_information()




