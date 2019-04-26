from csv_comparison_package import Compare
from csv_comparison_package import Field
from csv_comparison_package.decorator import call_each


@call_each
def write_checked_column_type_title(comparable: Compare):
    if comparable.checked_column_start:
        Compare.worksheet_master.write(1,
                                       comparable.checked_column_start,
                                       f"[ {Field.checked_column_label.value} ]",
                                       comparable.header_format_left_border)
