from csv_comparison_package.error_handler import AppErrorHandler


def check_for_empty_dictionary(comparator):
    if not comparator.parameters:
        raise AppErrorHandler(AppErrorHandler.empty_list)
