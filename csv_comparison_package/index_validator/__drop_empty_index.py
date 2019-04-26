from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def drop_empty_index(comparable: Compare):
    comparable.data_frame = comparable.data_frame.drop(comparable.empty_index)
