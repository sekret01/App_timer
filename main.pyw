from main_window import Window
from main_counter import main_counter_function
from control_app import ControlApp
import multiprocessing



def main():
    controller = ControlApp()
    window = Window()

    if not controller.is_work():
        counter = multiprocessing.Process(target=main_counter_function,
                                          name='time_counter',
                                          daemon=False)
        counter.start()

    window.mainloop()



if __name__ == "__main__":
    main()
