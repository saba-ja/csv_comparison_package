from csv_comparison_package import Compare
from csv_comparison_package import Field
from csv_comparison_package.decorator import call_each


@call_each
def extract_duplicate_column(comparable: Compare):
    header_duplicate = [header[Field.column_name.value] for header in comparable.header if
                        header[Field.column_type.value] == Field.duplicate.value]
    comparable.duplicate_column = comparable.data_frame[header_duplicate]
