from csv_comparison_package import Field
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def stringify_index(comparable: Compare):
    """ Convert values in the index column(s) to string """
    for index_dict in comparable.index_column_name:
        index_name = index_dict[Field.column_name.value]
        comparable.data_frame[index_name] = comparable.data_frame[index_name].astype(str)
