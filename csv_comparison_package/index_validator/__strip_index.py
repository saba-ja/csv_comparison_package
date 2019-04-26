from csv_comparison_package import Field
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def strip_index(comparable: Compare):
    for index_dict in comparable.index_column_name:
        index_name = index_dict[Field.column_name.value]
        comparable.data_frame[index_name] = comparable.data_frame[index_name].apply(
            lambda x: "".join(x.split()) if type(x) is str else x)
