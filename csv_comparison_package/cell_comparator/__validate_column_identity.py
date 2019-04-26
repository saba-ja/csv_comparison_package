from csv_comparison_package import Compare
from csv_comparison_package import AppErrorHandler
from csv_comparison_package import header_validator


def validate_column_identity(comparable_a: Compare, comparable_b: Compare):
    header_a = list(comparable_a.data_frame.columns.values)
    header_b = list(comparable_b.data_frame.columns.values)
    is_a_in_b = [val in header_b for val in header_a ]
    if not all(is_a_in_b):
        raise AppErrorHandler(AppErrorHandler.invalid_header_list)
