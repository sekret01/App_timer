from .process_info_dict import ProcessInfoDict
from .apps_time import AppTime
import json
import threading
import time


class WriterProcessInfo:
    """
    ...
    """
    def __init__(self, process_dict: ProcessInfoDict):
        self.process_dict = process_dict
        self.pause = 10

    def run(self):
        writer_thr = threading.Thread(name="writer process info thread",
                                      target=self.start_write,
                                      daemon=True)
        writer_thr.start()

    def start_write(self):
        while True:
            time.sleep(self.pause)
            processes = self.convert_process_info_to_json()
            self.writer(processes)

    def writer(self, processes: dict[dict[str: str, str: bool]]) -> None:
        with open(self.process_dict.settings.save_file_path + 'test_data.json', 'w', encoding='utf-8') as file:
            json.dump(processes, file)


    def convert_process_info_to_json(self) -> dict[dict[str: str, str: bool]]:
        processes = self.process_dict.get_processes()
        copy_processes: dict[dict[str: str, str: bool]] = dict()
        for key in processes.keys():
            copy_processes[key] = dict()
            copy_processes[key]["str_time"] = processes[key]["str_time"]
            copy_processes[key]["run"] = processes[key]["run"]
        return copy_processes
