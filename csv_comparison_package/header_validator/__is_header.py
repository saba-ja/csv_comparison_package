from csv_comparison_package.field import Field


def is_header(comparable, lookup):
    """ TODO need to add test """
    """ Check for column name and column key """
    return any([True for header in comparable.header
                if lookup[Field.column_name.value] == header[Field.column_name.value] and
                lookup[Field.column_location.value] == header[Field.column_location.value]])
