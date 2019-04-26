from csv_comparison_package import Compare
from csv_comparison_package import Field
from csv_comparison_package.decorator import call_each


@call_each
def extract_not_checked_column(comparable: Compare):
    header_not_checked = [header[Field.column_name.value] for header in comparable.header if
                          header[Field.column_type.value] == Field.not_checked.value]
    comparable.not_checked_column = comparable.data_frame[header_not_checked]
