import json
from app_timer import ObserverOfDays
from app_timer.process_setting import ProcessSetting

def get_today_data():
    try:
        with open(ProcessSetting().save_file_path, "r", encoding='utf-8') as file:
            data = json.load(file)
            data_for_table = data[ObserverOfDays().get_day_now()]
            return data_for_table
    except Exception as ex:
        print(ex)


def get_name_of_process(process_name: str) -> str:
    try:
        with open(ProcessSetting().tracked_process_path, "r", encoding='utf-8') as file:
            all_process_name = json.load(file)
            if process_name in all_process_name.keys():
                return all_process_name[process_name]
            return process_name
    except Exception as ex:
        return process_name

