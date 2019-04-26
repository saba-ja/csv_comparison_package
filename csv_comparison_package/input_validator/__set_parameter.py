from csv_comparison_package import Compare
from csv_comparison_package import AppErrorHandler
from csv_comparison_package import Field


def set_parameter(setting, comparable_a, comparable_b):
    for prm_key in setting.parameters:
        if Field.file_1_2_flag.value in prm_key:
            setattr(Compare, format_parameter(prm_key, Field.file_1_2_flag.value),
                    setting.parameters[prm_key])
        elif Field.file_1_flag.value in prm_key:
            setattr(comparable_a, format_parameter(prm_key, Field.file_1_flag.value),
                    setting.parameters[prm_key])
        elif Field.file_2_flag.value in prm_key:
            setattr(comparable_b, format_parameter(prm_key, Field.file_2_flag.value),
                    setting.parameters[prm_key])
        else:
            raise AppErrorHandler(AppErrorHandler.invalid_key)


def format_parameter(prm_key, flag):
    key = prm_key.replace(flag, "_")
    if "file_name" not in key:
        key = key.replace("file_", "")
    return key
