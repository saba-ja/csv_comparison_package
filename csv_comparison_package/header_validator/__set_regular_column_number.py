from csv_comparison_package import Field
from csv_comparison_package import header_validator
from csv_comparison_package import Compare
from csv_comparison_package.decorator import call_each


@call_each
def set_regular_column_number(comparable: Compare):
    for header in comparable.header:
        if not header[Field.column_type.value] and not header_validator.is_index(comparable,
                                                                                 header):
            comparable.number_of_regular_columns += 1
