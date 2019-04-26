from csv_comparison_package import Compare
from csv_comparison_package import Field
from csv_comparison_package import header_validator


def get_checked_column_name(comparable: Compare):
    return [val for val in comparable.header if
            (val[Field.column_type.value] == Field.empty_string.value or
             val[Field.column_type.value] == Field.mapped.value) and
            not header_validator.is_index(comparable, val)]
