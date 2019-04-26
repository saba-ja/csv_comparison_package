from csv_comparison_package import Compare
from csv_comparison_package.decorator import call_each


@call_each
def set_start_end_index_column(comparable: Compare):
    comparable.index_column_start = comparable.start_column
    comparable.index_column_end = comparable.start_column + comparable.number_of_index_column - 1
