from csv_comparison_package import Field
from csv_comparison_package import Compare
from csv_comparison_package.decorator import call_each


@call_each
def set_unnamed_column_number(comparable: Compare):
    for header in comparable.header:
        if header[Field.column_type.value] == Field.unnamed.value:
            comparable.number_of_unnamed_columns += 1
