from csv_comparison_package import Field
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def sort_index(comparable: Compare):
    """ Sort the index column(s). It assumes all the values are of type string """
    index_list = [col[Field.column_name.value] for col in comparable.index_column_name]
    comparable.data_frame.sort_values(by=index_list, inplace=True)
