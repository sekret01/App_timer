from app_timer import ProcessInfoDict
from app_timer import WriterProcessInfo
import time
import os


def writer(path: str, proc: ProcessInfoDict, pause = 10):
    data = proc.get_process_info()
    with open(path, 'w', encoding='utf-8') as f:
        f.write(data)
    time.sleep(pause)


def main():
    pause = 1

    p = ProcessInfoDict()
    process_writer = WriterProcessInfo(p)
    process_writer.run()

    start = time.time()

    while True:

        try:

            time.sleep(pause)
            p.update_process_list()
            os.system('cls')
            p.print_process_info()

            end = time.time()
            print(f"\n\ntime: {round(end - start, 3)}")
            pause = round(1 / (end - start), 3)
            start = end

        except KeyboardInterrupt:
            process_writer.stop_write()
            break







if __name__ == "__main__":
    main()
