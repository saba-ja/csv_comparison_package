import os.path
from csv_comparison_package.error_handler import AppErrorHandler
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def check_for_input_file_existence(comparable: Compare):
    is_file_available = os.path.isfile(comparable.file_name)
    if not is_file_available:
        raise AppErrorHandler(AppErrorHandler.no_file)
