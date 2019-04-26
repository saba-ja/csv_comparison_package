from csv_comparison_package import Compare
from csv_comparison_package import Field
from csv_comparison_package.decorator import call_each


@call_each
def freeze_pandas_index(comparable: Compare):
    comparable.original_data_frame[
        Field.pandas_original_index.value] = comparable.original_data_frame.index
