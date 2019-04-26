from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def set_data_frame(comparable: Compare):
    comparable.data_frame = comparable.original_data_frame.copy(deep=True)

