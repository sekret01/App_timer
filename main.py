from app_timer import ProcessInfoDict
from app_timer import WriterProcessInfo
from app_timer import Logger
import time
import os


def main():
    logger = Logger()
    logger.log_info(f"Start program")
    pause = 1

    process_dict = ProcessInfoDict()
    process_writer = WriterProcessInfo(process_dict)
    process_writer.run()

    start = time.time()

    while True:

        try:

            time.sleep(pause)
            process_dict.update_process_list()
            os.system('cls')
            process_dict.print_process_info()

            end = time.time()
            cycle_time = round(end - start, 3)
            if cycle_time > 1.5:
                logger.log_warning(f"[MAIN]: time of cycle more 1.5 sec  [{cycle_time}]")
            pause = round(1 / (end - start), 3)
            start = end

        except KeyboardInterrupt:
            process_writer.stop_write()
            logger.log_info(f"Stop program with KeyboardInterrupt")
            break

        except Exception as ex:
            logger.log_error(str(ex))


if __name__ == "__main__":
    main()
