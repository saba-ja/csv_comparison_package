from collections import Counter
from csv_comparison_package.field import Field
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def format_duplicate_column(comparable: Compare):
    header_count = Counter([header[Field.column_name.value] for header in comparable.header])
    repeated_header = [col_name for col_name, repeat_number in header_count.items()
                       if repeat_number > 1]

    duplicates_list = [(index, header) for index, header in enumerate(comparable.header) if
                       header[Field.column_name.value] in repeated_header and
                       header[Field.column_type.value] == Field.empty_string.value]

    for index, _ in duplicates_list:
        comparable.header[index][Field.column_name.value] = change_value(comparable, index)
        comparable.header[index][Field.column_type.value] = Field.duplicate.value


def change_value(comparable, index):
    return "{0}@{1}.{2}".format(comparable.header[index][Field.column_name.value],
                                  Field.duplicate.value,
                                  comparable.header[index][Field.column_location.value])
