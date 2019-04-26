from csv_comparison_package import Compare
from csv_comparison_package import header_validator
from csv_comparison_package import Field
from csv_comparison_package.decorator import call_each


@call_each
def format_not_for_checked_column(comparable: Compare):
    """
    When map_columns is not empty and compare_only_mapped_columns is true
    then mark all other columns that do not have any other type as notChecked.
    If the map_columns is empty compare_only_mapped_columns will not have effect
    """
    if Compare.map_columns and comparable.compare_only_mapped_columns:
        for index, header in enumerate(comparable.header):
            is_not_index = not header_validator.is_index(comparable, header)
            is_empty_type = header[Field.column_type.value] == Field.empty_string.value
            if is_not_index and is_empty_type:
                comparable.header[index][Field.column_type.value] = Field.not_checked.value
                comparable.header[index][Field.column_name.value] = change_value(comparable, index)


def change_value(comparable, index):
    return "{0}@{1}.{2}".format(comparable.header[index][Field.column_name.value],
                                Field.not_checked_column_tag.value,
                                comparable.header[index][Field.column_location.value])
