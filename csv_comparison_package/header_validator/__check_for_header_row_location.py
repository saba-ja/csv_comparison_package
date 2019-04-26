from csv_comparison_package.error_handler import AppErrorHandler
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def check_for_header_row_location(comparable: Compare):
    """Check for header row location in the file to not exceed number of lines in the file"""
    num_lines = sum(1 for _ in open(comparable.file_name, encoding=comparable.encoding))
    if num_lines < comparable.header_row:
        raise AppErrorHandler(AppErrorHandler.header_row_out_of_range)
