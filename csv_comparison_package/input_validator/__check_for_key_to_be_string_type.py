from csv_comparison_package.error_handler import AppErrorHandler


def check_for_key_to_be_string_type(comparator):
    for key_val in comparator.parameters:
        if not isinstance(key_val, str):
            raise AppErrorHandler(AppErrorHandler.invalid_key_type)
