from csv_comparison_package import Compare
from csv_comparison_package.decorator import call_each


@call_each
def remove_nan(comparable: Compare):
    comparable.data_frame = comparable.data_frame.fillna('')
