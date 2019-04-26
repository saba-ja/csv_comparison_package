import os
from csv_comparison_package.error_handler import AppErrorHandler
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def check_for_file_read_access(comparable: Compare):
    is_file_readable = os.access(comparable.file_name, os.R_OK)
    if not is_file_readable:
        raise AppErrorHandler(AppErrorHandler.read_access)
