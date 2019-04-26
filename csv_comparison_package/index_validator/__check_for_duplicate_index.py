from csv_comparison_package import index_validator as idx
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def check_for_duplicate_index(comparable: Compare):
    index_name = idx.get_index_name(comparable)
    comparable.duplicate_index = comparable.data_frame[
        comparable.data_frame.duplicated([index_name], keep=False)]
