from app_timer import ProcessInfoDict

import threading
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
    thr = threading.Thread()

    start = time.time()

    while True:

        time.sleep(pause)
        p.update_process_list()
        os.system('cls')
        p.print_process_info()

        if not thr.is_alive():
            thr = threading.Thread(target=writer,
                                   args=[p.settings.save_file_path + "test_file.txt", p],
                                   name="Writer",
                                   daemon=True)
            thr.start()

        end = time.time()
        print(f"\n\ntime: {round(end - start, 3)}")
        pause = round(1 / (end - start), 3)
        start = end







if __name__ == "__main__":
    main()
