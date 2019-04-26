from csv_comparison_package.error_handler import AppErrorHandler


def check_for_type_dictionary(comparator):
    if not isinstance(comparator.parameters, dict):
        raise AppErrorHandler(AppErrorHandler.invalid_dictionary)
