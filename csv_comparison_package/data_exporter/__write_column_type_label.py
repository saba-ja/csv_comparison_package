from csv_comparison_package import Compare
from csv_comparison_package import Field


def write_column_type_label():
    Compare.worksheet_master.write(1, 0, Field.column_type_label.value)
