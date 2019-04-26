from csv_comparison_package import header_validator
from csv_comparison_package.field import Field
from csv_comparison_package import Compare


def format_disjunctive_column(comparable_a: Compare, comparable_b: Compare):
    """
    If they are not index, and not mapped, and not the same they are disjunctive
    """
    for index, header in enumerate(comparable_a.header):

        is_not_index = not header_validator.is_index(comparable_a, header)
        is_not_in_other = not header_validator.is_column(comparable_b, header)
        is_empty_type = header[Field.column_type.value] == Field.empty_string.value
        is_not_mapped = not header_validator.is_mapped(comparable_a, header)

        is_disjunctive = all([is_not_index, is_not_in_other, is_empty_type, is_not_mapped])

        if is_disjunctive:
            comparable_a.header[index][Field.column_type.value] = Field.disjunctive.value
            comparable_a.header[index][Field.column_name.value] = change_value(comparable_a, index)


def change_value(comparable, index):
    return "{0}@{1}.{2}".format(comparable.header[index][Field.column_name.value],
                                  Field.disjunctive_column_tag.value,
                                  comparable.header[index][Field.column_location.value])
