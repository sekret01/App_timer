from .apps_time import AppTime
from .process_setting import ProcessSetting
from .processes_list import ProcessListCreator
import subprocess
import logging
import json
import threading





class ProcessInfoDict:
    """
    ...
    """
    def __init__(self):
        self.processes: dict[str:AppTime] = dict()
        self.settings: ProcessSetting = ProcessSetting()
        self.processes_list_creator = ProcessListCreator()

    # update data

    def update_process_list(self) -> None:
        """Update list with process, adding new process"""
        processes: list[str] = self.processes_list_creator.get_processes_list()
        for proc in processes:
            self.processes.setdefault(proc, AppTime())
        self.update_process_time(processes)

    def update_process_time(self, active_processes: list[str]):
        """Update time all processes, adding 1 second"""
        for proc, proc_time in self.processes.items():
            if proc in active_processes:
                self.processes[proc] += 1


    # output

    def get_process_info(self) -> str:
        """Create formatted text with information about processes"""
        text = ""
        for proc, time in self.processes.items():
            text += f"{proc:<30} {time}\n"

        return text

    def print_process_info(self) -> None:
        """
        Create formatted text with information about processes
        ONLY FOR TESTS
        """
        text = ""
        for proc, time in self.processes.items():
            text += f"{proc:<30} {time}\n"

        print(text)



