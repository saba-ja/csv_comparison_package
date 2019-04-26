from csv_comparison_package.error_handler import AppErrorHandler
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def check_for_negative_header_row(comparable: Compare):
    if comparable.header_row <= 0:
        raise AppErrorHandler(AppErrorHandler.header_row_out_of_range)
