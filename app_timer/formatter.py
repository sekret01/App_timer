from .apps_time import AppTime

class JsonFormatter:
    """
    Formats data for translation into json object
    """
    def convert_process_info_to_json(self,processes_dict:  dict[str: dict[str: AppTime, str: bool, str: str]]) -> dict[dict[str: str, str: bool]]:
        copy_processes: dict[dict[str: str, str: bool]] = dict()
        for key in processes_dict.keys():
            copy_processes[key] = dict()
            copy_processes[key]["str_time"] = processes_dict[key]["str_time"]
            copy_processes[key]["run"] = processes_dict[key]["run"]
        return copy_processes
