from csv_comparison_package.field import Field
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def strip_header(comparable: Compare):
    for index, dict_obj in enumerate(comparable.header):
        comparable.header[index][Field.column_name.value] = dict_obj[Field.column_name.value]. \
            replace('\n', ""). \
            replace('\r', ""). \
            replace('\t', ""). \
            strip()
