from csv_comparison_package import Compare
from csv_comparison_package import Field
from csv_comparison_package.decorator import call_each


@call_each
def extract_unnamed_column(comparable: Compare):
    header_unnamed = [header[Field.column_name.value] for header in comparable.header if
                      header[Field.column_type.value] == Field.unnamed.value]
    comparable.unnamed_column = comparable.data_frame[header_unnamed]
