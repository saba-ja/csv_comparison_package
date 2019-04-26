from csv_comparison_package import Compare
from csv_comparison_package import Field
from csv_comparison_package.decorator import call_each


@call_each
def drop_disjunctive_column(comparable: Compare):
    header_disjunctive = [header[Field.column_name.value] for header in comparable.header if
                          header[Field.column_type.value] == Field.disjunctive.value]
    comparable.data_frame = comparable.data_frame.drop(columns=header_disjunctive)
