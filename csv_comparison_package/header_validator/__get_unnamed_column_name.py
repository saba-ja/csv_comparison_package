from csv_comparison_package import Compare
from csv_comparison_package import Field


def get_unnamed_column_name(comparable: Compare):
    return [val for val in comparable.header if
            val[Field.column_type.value] == Field.unnamed.value]
