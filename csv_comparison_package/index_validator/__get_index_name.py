from csv_comparison_package import Field


def get_index_name(comparable):
    """ Return the name of the first value of index_column_name as index name.
    TODO: multi index support needs to be added"""
    return comparable.index_column_name[0][Field.column_name.value]
