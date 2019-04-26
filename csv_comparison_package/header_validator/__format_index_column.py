from csv_comparison_package.field import Field
from csv_comparison_package import header_validator
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def format_index_column(comparable: Compare):
    for index, header in enumerate(comparable.header):
        if header_validator.is_index(comparable, header):
            comparable.header[index][Field.column_type.value] = Field.index.value
