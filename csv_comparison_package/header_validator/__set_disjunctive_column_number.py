from csv_comparison_package import Field
from csv_comparison_package import Compare
from csv_comparison_package.decorator import call_each


@call_each
def set_disjunctive_column_number(comparable: Compare):
    for header in comparable.header:
        if header[Field.column_type.value] == Field.disjunctive.value:
            comparable.number_of_disjunctive_columns += 1
