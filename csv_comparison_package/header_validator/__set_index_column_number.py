from csv_comparison_package import Compare
from csv_comparison_package.decorator import call_each


@call_each
def set_index_column_number(comparable: Compare):
    comparable.number_of_index_column = 1  # Not supporting multiple index
