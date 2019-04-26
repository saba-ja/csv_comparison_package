from csv_comparison_package import Compare
from csv_comparison_package import Field
from csv_comparison_package import AppErrorHandler


def validate_index_identity(comparable_a: Compare, comparable_b: Compare):
    comparable_a_index_name = comparable_a.index_column_name[0][
        Field.column_name.value]  # not supporting multi index
    comparable_b_index_name = comparable_b.index_column_name[0][Field.column_name.value]
    df_a = list(comparable_a.data_frame[comparable_a_index_name])
    df_b = list(comparable_b.data_frame[comparable_b_index_name])
    is_a_in_b = [val in df_b for val in df_a]

    if not all(is_a_in_b):
        raise AppErrorHandler(AppErrorHandler.invalid_index_list)
