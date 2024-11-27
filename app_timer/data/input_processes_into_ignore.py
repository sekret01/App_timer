import json


def input_processes():
    """
    !!!!! WARNING !!!!!
    REWRITING
    """
    processes_list = []
    while (text := input()) != "":
        processes_list.append(text)

    with open('ignore_process.json', 'w', encoding='utf-8') as f:
        json.dump(processes_list, f)

input_processes()