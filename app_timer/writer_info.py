from .process_info_dict import ProcessInfoDict
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

    def create_thread(self):
        writer_thr = threading.Thread(name="writer process info thread",
                                      target=self.start_write(),
                                      args=(self.process_dict, ),
                                      daemon=True)
        writer_thr.start()

    def start_write(self):
        while True:
            time.sleep(self.pause)
            self.writer()

    def writer(self):
        with open(self.process_dict.settings.save_file_path, 'w', encoding='utf-8') as file:
            json.dump(self.process_dict, file)
