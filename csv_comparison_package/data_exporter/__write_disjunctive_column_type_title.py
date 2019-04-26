from csv_comparison_package import Compare
from csv_comparison_package import Field
from csv_comparison_package.decorator import call_each


@call_each
def write_disjunctive_column_type_title(comparable: Compare):
    if comparable.disjunctive_column_start:
        Compare.worksheet_master.write(
            1,
            comparable.disjunctive_column_start,
            f"[ {Field.disjunctive_column_label.value} F{comparable.order+1} ]",
            comparable.header_format_left_border)
