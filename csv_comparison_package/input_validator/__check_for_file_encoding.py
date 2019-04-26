from csv_comparison_package.error_handler import AppErrorHandler
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def check_for_file_encoding(comparable: Compare):
    with open(comparable.file_name, newline='', encoding=comparable.encoding) as file:
        try:
            file.readline()
        except UnicodeDecodeError:
            raise AppErrorHandler(AppErrorHandler.unknown_encoding)
