import subprocess
from .process_setting import ProcessSetting


class ProcessListCreator:
    """
    Creator list with running processes
    """
    def __init__(self):
        self.settings: ProcessSetting = ProcessSetting()

    def _get_all_processes(self) -> str:
        """Get all information running processes (use cmd)"""
        processes = subprocess.run(["tasklist", "/FO", "CSV", "/FI", "STATUS eq RUNNING", "/NH"],
                                   capture_output=True)
        return processes.stdout.decode('utf-8', errors='ignore')

    def _get_all_names_processes(self, processes: str) -> list[str]:
        """Take only names of processes"""
        proc_info_list = processes.replace('\"', '').split('\n')
        proc_names = [line.split(',')[0] for line in proc_info_list]
        return proc_names

    def _filter_process_names(self, processes: list[str]) -> list[str]:
        """Removes all duplicates and ignored processes"""
        process_set: set = set(processes)
        process_names_list: list[str] = [proc for proc in process_set if self._no_ignore_process(proc)]
        return process_names_list

    def _no_ignore_process(self, process: str) -> bool:
        """Check process in ignore processes"""
        with open(self.settings.ignore_process_path, "r", encoding='utf-8') as f:
            ignore = f.read()
            return True if process not in ignore else False

    def get_processes_list(self):
        """create list with processes"""
        processes_info: str = self._get_all_processes()
        all_process_names: list[str] = self._get_all_names_processes(processes_info)
        process_names = self._filter_process_names(all_process_names)
        return process_names
