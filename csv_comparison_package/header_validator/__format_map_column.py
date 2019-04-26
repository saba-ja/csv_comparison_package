from csv_comparison_package.compare import Compare
from csv_comparison_package import header_validator
from csv_comparison_package.field import Field
from csv_comparison_package.decorator import call_each


@call_each
def format_map_column(comparable: Compare):
    """ Format mapped columns with different names to [column1]-[column2] """
    for tuple_val in Compare.map_columns:
        is_header = header_validator.is_header(comparable, tuple_val[comparable.order])
        is_identical = \
            tuple_val[0][Field.column_name.value] == tuple_val[1][Field.column_name.value]

        if is_header:
            header_index = header_validator.get_header_index(comparable,
                                                             tuple_val[comparable.order])
            is_index = header_validator.is_index(comparable, comparable.header[header_index])

            if not is_index:
                comparable.header[header_index][Field.column_type.value] = Field.mapped.value
                is_changeable = all([is_header, not is_identical])
                if is_changeable:
                    comparable.header[header_index][Field.column_name.value] = \
                        f"[{tuple_val[0][Field.column_name.value]}]-" \
                        f"[{tuple_val[1][Field.column_name.value]}]"

