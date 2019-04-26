from csv_comparison_package import Compare
from csv_comparison_package import Field
from csv_comparison_package.decorator import call_each


@call_each
def apply_duplicate_column_hide_condition(comparable: Compare):
    if comparable.duplicate_column_start and comparable.hide_duplicate_columns:
        Compare.worksheet_master.set_column(comparable.duplicate_column_start,
                                            comparable.duplicate_column_end,
                                            Field.general_column_width.value,
                                            comparable.column_general_format,
                                            options={'hidden': True})