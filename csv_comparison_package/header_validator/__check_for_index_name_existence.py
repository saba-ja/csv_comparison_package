from csv_comparison_package import Field
from csv_comparison_package import AppErrorHandler
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def check_for_index_name_existence(comparable: Compare):
    """ Only checks if the index_name exists in the header. It does not check for the location"""
    for comparable_dict in comparable.index_column_name:
        header_index = [index for index, val in enumerate(comparable.header)
                        if val[Field.column_name.value] == comparable_dict[
                            Field.column_name.value]]
        if not header_index:
            raise AppErrorHandler(AppErrorHandler.missing_index_column)
