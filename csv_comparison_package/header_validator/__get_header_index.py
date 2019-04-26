from csv_comparison_package.field import Field


def get_header_index(comparable, lookup):
    """ Find the index of a column in header row based on column name and location
        If header not found will return none
    """
    return next((index for index, header in enumerate(comparable.header)
                 if lookup[Field.column_name.value] == header[Field.column_name.value] and
                 lookup[Field.column_location.value] == header[Field.column_location.value]), None)
