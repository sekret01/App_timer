import configparser
from .process_setting import ProcessSetting

conf_path = ProcessSetting().config_path


def update_configs(configs: configparser.ConfigParser):
    with open(conf_path, "w", encoding='utf-8') as f:
        configs.write(f)


def get_configs() -> configparser.ConfigParser:
    configs = configparser.ConfigParser()
    configs.read(conf_path)
    return configs

def update_day(date):
    conf = get_configs()
    conf["TIMES"]["last_day"] = date
    update_configs(configs=conf)