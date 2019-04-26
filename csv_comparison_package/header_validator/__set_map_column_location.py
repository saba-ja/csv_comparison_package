from csv_comparison_package import Field
from csv_comparison_package import AppErrorHandler
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def set_map_column_location(comparable: Compare):
    for comparable_index, comparable_dict in enumerate(Compare.map_columns):
        if Field.column_location.value not in comparable_dict:
            header_index = [index for index, val in enumerate(comparable.header)
                            if val[Field.column_name.value] == comparable_dict[comparable.order][
                                Field.column_name.value]]
            if len(header_index) > 1:
                raise AppErrorHandler(AppErrorHandler.ambiguous_map_column)
            elif not header_index:
                raise AppErrorHandler(AppErrorHandler.missing_mapped_column)
            else:
                Compare.map_columns[comparable_index][comparable.order][
                    Field.column_location.value] = \
                    comparable.header[header_index[0]][Field.column_location.value]
