import json
import pathlib
from tkinter import *
from tkinter import ttk
from data_getter import get_today_data, get_name_of_process

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x450")
        self.title("App timer")

        # top line
        self.frame_top_line = ttk.Frame(borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_top_line.columnconfigure(index=0, weight=4)
        self.frame_top_line.columnconfigure(index=1, weight=1)

        # status info
        self.status_info_frame = ttk.Frame(self.frame_top_line, borderwidth=1, relief=SOLID, padding=[0, 0])
        self.status_info = ttk.Label(self.status_info_frame, text = "Work..", borderwidth=1, relief=SOLID, font=("Times New Roman", 14))

        # switch
        self.switch_frame = ttk.Frame(self.frame_top_line, borderwidth=1, relief=SOLID, padding=[5, 5])
        self.switch_button = ttk.Button(self.switch_frame, text="OFF", command=self.switch)

        # table
        self.table_frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[25, 25, 25, 0])
        self.table_frame.columnconfigure(index=0, weight=1)
        self.table_frame.columnconfigure(index=1, weight=1)
        self.table_frame.rowconfigure(index=0, weight=1)
        self.table_frame.rowconfigure(index=1, weight=1)

        self.time_table = ttk.Treeview(self.table_frame, columns=("app", "time", "status"), show="headings")

        self.time_table.heading("app", text="Программа")
        self.time_table.heading("time", text="Время")
        self.time_table.heading("status", text="Состояние")

        self.time_table.column("#1", stretch=NO, width=320, anchor=W)
        self.time_table.column("#2", stretch=NO, width=110, anchor=CENTER)
        self.time_table.column("#3", stretch=NO, width=80, anchor=CENTER)

        self.scrollbar_table = ttk.Scrollbar(self.table_frame, orient=VERTICAL, command=self.time_table.yview)


        # update
        self.update_button = ttk.Button(self.table_frame, text="Обновить", command=self.update_table)

        # ----------------------------------------------------------------

        self.status_info.pack(fill=BOTH, expand=True)
        self.status_info_frame.grid(row=0, column=0, sticky=NSEW)

        self.switch_button.pack(expand=True, pady=10)
        self.switch_frame.grid(row=0, column=1, sticky=NSEW)

        self.frame_top_line.pack(fill=X, padx=0, pady=0)

        self.time_table.grid(row=0, column=0)
        self.scrollbar_table.grid(row=0, column=1, sticky=NS)
        self.update_button.grid(row=1, column=0, columnspan=2, sticky=E, padx=0, pady=10)

        self.table_frame.pack(expand=True, padx=5, pady=5)

    def switch(self):
        """On or Off app"""
        ...

    def update_table(self):
        """Update values in table"""
        self.time_table.delete(*self.time_table.get_children())
        data_for_table = get_today_data()
        for i, (process, info) in enumerate(data_for_table.items(), start=0):
            process_name = get_name_of_process(process)
            time = info["str_time"]
            status = "ON" if info["run"] else "OFF"
            self.time_table.insert("", i, values=(process_name, time, status))


w = Window()
w.mainloop()

