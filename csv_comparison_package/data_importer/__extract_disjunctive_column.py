from csv_comparison_package import Compare
from csv_comparison_package import Field
from csv_comparison_package.decorator import call_each


@call_each
def extract_disjunctive_column(comparable: Compare):
    header_disjunctive = [header[Field.column_name.value] for header in comparable.header if
                          header[Field.column_type.value] == Field.disjunctive.value]
    comparable.disjunctive_column = comparable.data_frame[header_disjunctive]
