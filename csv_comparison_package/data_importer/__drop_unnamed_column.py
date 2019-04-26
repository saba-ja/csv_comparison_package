from csv_comparison_package import Compare
from csv_comparison_package import Field
from csv_comparison_package.decorator import call_each


@call_each
def drop_unnamed_column(comparable: Compare):
    header_unnamed = [header[Field.column_name.value] for header in comparable.header if
                      header[Field.column_type.value] == Field.unnamed.value]
    comparable.data_frame = comparable.data_frame.drop(columns=header_unnamed)
