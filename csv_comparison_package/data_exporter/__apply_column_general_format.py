from csv_comparison_package import Compare
from csv_comparison_package import Field
from csv_comparison_package.decorator import call_each


@call_each
def apply_column_general_format(comparable: Compare):
    Compare.worksheet_master.set_column(comparable.start_column,
                                        comparable.end_column,
                                        Field.general_column_width.value,
                                        comparable.column_general_format)
