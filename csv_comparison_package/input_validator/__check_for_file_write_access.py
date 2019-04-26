import os
from csv_comparison_package.error_handler import AppErrorHandler
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def check_for_file_write_access(comparable: Compare):
    is_file_writeable = os.access(comparable.file_name, os.W_OK)
    if not is_file_writeable:
        raise AppErrorHandler(AppErrorHandler.write_access)
