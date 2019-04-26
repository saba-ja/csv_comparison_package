from csv_comparison_package.field import Field
from csv_comparison_package import header_validator
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def format_unnamed_column(comparable: Compare):
    for index, header in enumerate(comparable.header):
        is_unnamed = all([header[Field.column_name.value] == Field.empty_string.value,
                          header[Field.column_type.value] == Field.empty_string.value,
                          not header_validator.is_index(comparable, header)])
        if is_unnamed:
            comparable.header[index][Field.column_name.value] = \
                f"@{Field.unnamed.value}.{comparable.header[index][Field.column_location.value]}"
            comparable.header[index][Field.column_type.value] = Field.unnamed.value
