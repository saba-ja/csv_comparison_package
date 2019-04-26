from csv_comparison_package import Field
from csv_comparison_package import AppErrorHandler
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def check_for_map_column_existence(comparable: Compare):
    """ Only check if the mapped column name exists in the header. It does not check for location"""
    for comparable_dict in Compare.map_columns:
        header_index = [index for index, val in enumerate(comparable.header)
                        if val[Field.column_name.value] == comparable_dict[comparable.order][
                            Field.column_name.value]]
        if not header_index:
            raise AppErrorHandler(AppErrorHandler.missing_mapped_column)
