from app_timer.processes_list import ProcessListCreator
from app_timer.process_info_dict import ProcessInfoDict
from app_timer.apps_time import AppTime
from time import time, sleep
import os


class TestProcessListCreator:
    def test_speed(self):
        plc = ProcessListCreator()
        all_times = []
        print("Start test: [100 get_processes_list]")

        for i in range(100):
            start = time()
            processes = plc.get_processes_list()
            end = time()
            all_times.append(end-start)

        print("End test")
        print('\n')
        print(f"Average value:   [{round(sum(all_times)/len(all_times), 4)}]")
        print(f"Min value: [{round(min(all_times), 4)}]\nMax value: [{round(max(all_times), 4)}]")

    def test_view(self):
        plc = ProcessListCreator()
        try:
            while True:
                start = time()
                sleep(1)
                os.system('cls')
                processes = plc.get_processes_list()
                for proc in processes:
                    print(proc)
                end = time()
                print(f"\nWork time: [{round(end-start, 2)}] sec")

        except KeyboardInterrupt:
            os.system('cls')
            return


class TestProcessInfoDict:
    def test_speed(self):
        pid= ProcessInfoDict()
        all_times = []
        print("Start test: [100 update_process_list]")

        for i in range(100):
            start = time()
            pid.update_process_list()
            end = time()
            all_times.append(end-start)

        print("End test")
        print('\n')
        print(f"Average value:   [{round(sum(all_times) / len(all_times), 4)}]")
        print(f"Min value: [{round(min(all_times), 4)}]\nMax value: [{round(max(all_times), 4)}]")

    def test_view(self):
        pid= ProcessInfoDict()

        try:
            while True:
                start = time()
                sleep(1)
                os.system('cls')
                pid.update_process_list()
                pid.print_process_info()

                end = time()
                print(f"\n\n{end-start}")
        except KeyboardInterrupt:
            return

def test_timer():
    timer = AppTime()

    for i in range(10000):
        timer += 1
        print(f"\r{timer}", end='')
        sleep(0.01)


def main():
    test_timer()


if __name__ == "__main__":
    main()
