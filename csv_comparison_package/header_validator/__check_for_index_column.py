from csv_comparison_package.error_handler import AppErrorHandler
from csv_comparison_package import header_validator as h
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def check_for_index_column(comparable: Compare):
    for index_col in comparable.index_column_name:
        if not h.is_header(comparable, index_col):
            raise AppErrorHandler(AppErrorHandler.missing_index_column)
