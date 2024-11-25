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

    # create process name list

    def get_all_processes(self) -> str:
        """Get all information running processes (use cmd)"""
        processes = subprocess.run(["tasklist", "/FO", "CSV", "/FI", "STATUS eq RUNNING", "/NH"],
                                   capture_output=True)
        return processes.stdout.decode('utf-8', errors='ignore')

    def get_all_names_processes(self, processes: str) -> list:
        """Take only names of processes"""
        proc_info_list = processes.replace('\"', '').split('\n')
        proc_names = [line.split(',')[0] for line in proc_info_list]
        return proc_names

    def filter_process_names(self, processes: list[str]) -> list:
        """Removes all duplicates and ignored processes"""
        process_set: set = set(processes)
        process_names_list: list[str] = [proc for proc in process_set if self.no_ignore_process(proc)]
        return process_names_list

    def no_ignore_process(self, process) -> bool:
        """Check process in ignore processes"""
        with open(self.settings.ignore_process_path, "r", encoding='utf-8') as f:
            ignore = f.read()
            return True if process not in ignore else False

    def get_processes_list(self) -> list[str]:
        """create list with processes"""
        processes_info: str = self.get_all_processes()
        all_process_names: list[str] = self.get_all_names_processes(processes_info)
        process_names = self.filter_process_names(all_process_names)
        return process_names

    # update data

    def update_process_list(self) -> None:
        """Update list with process, adding new process"""
        processes: list[str] = self.get_processes_list()
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



