from csv_comparison_package import Compare
from csv_comparison_package import Field
from operator import itemgetter


def get_duplicate_column_name(comparable: Compare, sort=True):
    result = [val for val in comparable.header if
              val[Field.column_type.value] == Field.duplicate.value]
    if sort:
        result.sort(key=itemgetter(Field.column_name.value))
    return result
