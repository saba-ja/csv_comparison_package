from csv_comparison_package.field import Field
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def set_header(comparable: Compare):
    comparable.header = [{Field.column_name.value: value,
                          Field.column_location.value: index + 1,  # NOTE: column location is 1 base
                          Field.column_type.value: ""}
                         for index, value in enumerate(comparable.original_header)]
