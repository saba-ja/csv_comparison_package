from csv_comparison_package.field import Field


def is_index(comparable, lookup):
    return any([True for index in comparable.index_column_name
                if lookup[Field.column_name.value] == index[Field.column_name.value] and
                lookup[Field.column_location.value] == index[Field.column_location.value]])
