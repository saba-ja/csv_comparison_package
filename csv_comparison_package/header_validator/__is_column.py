from csv_comparison_package.field import Field


def is_column(comparable, lookup):
    """ TODO need to add test """
    """ Check for column name existence """
    return any([True for header in comparable.header
                if lookup[Field.column_name.value] == header[Field.column_name.value]])
