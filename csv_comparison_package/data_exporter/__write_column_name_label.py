from csv_comparison_package import Compare
from csv_comparison_package import Field


def write_column_name_label():
    Compare.worksheet_master.write(2, 0, Field.column_name_label.value)
