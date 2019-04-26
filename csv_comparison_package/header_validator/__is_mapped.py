from csv_comparison_package import Field
from csv_comparison_package import Compare


def is_mapped(comparable, lookup):
    """ Check for the existence of given dict object in the Compare.map_columns """
    return any([True for val in Compare.map_columns if
                all([lookup[Field.column_name.value] ==
                     val[comparable.order][Field.column_name.value],
                     lookup[Field.column_location.value] ==
                     val[comparable.order][Field.column_location.value]])])
