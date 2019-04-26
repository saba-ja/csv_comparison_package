import os
from csv_comparison_package.error_handler import AppErrorHandler
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def check_for_file_size(comparable: Compare):
    if os.path.getsize(comparable.file_name) == 0:
        raise AppErrorHandler(AppErrorHandler.empty_file)
