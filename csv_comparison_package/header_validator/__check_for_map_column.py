from csv_comparison_package import AppErrorHandler
from csv_comparison_package import Compare
from csv_comparison_package import header_validator as h
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def check_for_map_column(comparable: Compare):
    for map_col in Compare.map_columns:
        if not h.is_header(comparable, map_col[comparable.order]):
            raise AppErrorHandler(AppErrorHandler.missing_mapped_column)
        if h.is_index(comparable, map_col[comparable.order]):
            raise AppErrorHandler(AppErrorHandler.map_and_index_conflict)
