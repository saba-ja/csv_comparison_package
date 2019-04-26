from csv_comparison_package import index_validator as idx
from csv_comparison_package import Field
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def check_for_empty_index(comparable: Compare):
    """
    Find row number of empty values in the index column
    """
    index_column = comparable.data_frame[idx.get_index_name(comparable)]
    comparable.empty_index = [index for index, value in enumerate(index_column)
                              if value == Field.empty_string.value
                              or value != value or value is None]
