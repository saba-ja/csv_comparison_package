from csv_comparison_package import Compare
from csv_comparison_package import data_exporter
from csv_comparison_package.decorator import call_each


@call_each
def write_file_name_title(comparable: Compare):
    Compare.worksheet_master.write(
        0,
        comparable.start_column,
        f"F{comparable.order + 1}: "
        f"{data_exporter.extract_file_name_from_path(comparable, truncate=False)}",
        comparable.header_format_left_border)
