from csv_comparison_package import Field
from csv_comparison_package import AppErrorHandler
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def set_index_column_location(comparable: Compare):
    """ Each column has a location in the original file. If the location of the index column
        is not given this function will try to auto detect the location of the column.
        The locations are 1 base and are determined in the comparable.header dictionary.
    """
    for comparable_index, comparable_dict in enumerate(comparable.index_column_name):
        if Field.column_location.value not in comparable_dict:
            header_index = [index for index, val in enumerate(comparable.header)
                            if val[Field.column_name.value] == comparable_dict[
                                Field.column_name.value]]
            if len(header_index) > 1:
                raise AppErrorHandler(AppErrorHandler.ambiguous_index_column)
            elif not header_index:
                raise AppErrorHandler(AppErrorHandler.missing_index_column)
            else:
                comparable.index_column_name[comparable_index][Field.column_location.value] = \
                    comparable.header[header_index[0]][Field.column_location.value]
