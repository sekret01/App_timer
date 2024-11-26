from .apps_time import AppTime
from .process_setting import ProcessSetting
from .processes_list import ProcessListCreator


class ProcessInfoDict:
    """
    struct of process:
        {<process_name>: {"time": <AppTimer>, "run" <bool>}}
    """
    def __init__(self):
        self.processes: dict[str: dict[str: AppTime, str: bool, str: str]] = dict()
        self.settings: ProcessSetting = ProcessSetting()
        self.processes_list_creator = ProcessListCreator()

    # update data

    def update_process_list(self) -> None:
        """Update list with process, adding new process"""
        processes: list[str] = self.processes_list_creator.get_processes_list()
        for proc in processes:
            self.processes.setdefault(proc, {"time": AppTime(), "run": False})
        self._update_process_time(processes)

    def _update_process_time(self, active_processes: list[str]):
        """Update time all processes, adding 1 second"""
        for proc in self.processes.keys():
            if proc in active_processes:
                self.processes[proc]["time"] += 1
                self.processes[proc]["run"] = True
                self.processes[proc]["str_time"] = str(self.processes[proc]["time"])
            else:
                self.processes[proc]["run"] = False

    def get_processes(self):
        return self.processes

    # output

    def get_process_info(self) -> str:
        """Create formatted text with information about processes"""
        text = ""
        for proc, info in self.processes.items():
            text += f"{proc:<30} {info["str_time"]:<10} {info["run"]}\n"

        return text

    def print_process_info(self) -> None:
        """
        Create formatted text with information about processes
        ONLY FOR TESTS
        """
        text = ""
        for proc, info in self.processes.items():
            text += f"{proc:<30} {str(info["time"]):<10s} {info["run"]}\n"

        print(text)


