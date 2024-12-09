from app_timer import ProcessInfoDict
from app_timer import WriterProcessInfo
from app_timer import Logger
from app_timer import ObserverOfDays
from app_timer import update_day
from app_timer import ProcessSetting
from control_app import ControlApp
import time
import json


def set_quantity_days(quantity, logger):
    path = ProcessSetting().save_file_path

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data: dict = json.load(f)
    except json.decoder.JSONDecodeError:
        logger.log_info(f"{__name__} json-file no data")
        data = dict()

    if len(data) <= quantity: return

    while len(data) > quantity:
        keys = list(data.keys())
        data.pop(keys[0])
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f)



def main_counter_function():
    controller = ControlApp()
    controller.set_work_status(1)

    observer = ObserverOfDays()

    logger = Logger()
    logger.log_info(f"Start program")

    pause = 1

    set_quantity_days(controller.get_day_quantity(), logger)

    if observer.is_new_day():
        process_dict = ProcessInfoDict()
        update_day(observer.get_day_now())
    else:
        process_dict = observer.load_day_information()

    process_writer = WriterProcessInfo(process_dict)
    process_writer.run()

    start = time.time()

    while True:

        try:

            if controller.is_stop_program():
                process_writer.stop_write()
                observer.save_day_information(process_dict)
                logger.log_info(f"Stop program")
                controller.set_work_status()
                controller.set_command_stop()
                break

            time.sleep(pause)
            process_dict.update_process_list()
            end = time.time()
            cycle_time = round(end - start, 3)

            if cycle_time > 1.5:
                logger.log_warning(f"[MAIN]: time of cycle more 1.5 sec  [{cycle_time}]")

            pause = round(1 / (end - start), 3)
            start = end

        except KeyboardInterrupt:
            process_writer.stop_write()
            observer.save_day_information(process_dict)
            logger.log_info(f"Stop program with KeyboardInterrupt")
            controller.set_work_status()
            break

        except Exception as ex:
            observer.save_day_information(process_dict)
            logger.log_error(str(ex))
            controller.set_work_status()
            break


if __name__ == "__main__":
    main_counter_function()
