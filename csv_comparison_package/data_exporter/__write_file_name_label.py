from csv_comparison_package import Compare
from csv_comparison_package import Field


def write_file_name_label():
    Compare.worksheet_master.set_column(0, 0, 15)
    Compare.worksheet_master.write(0, 0, Field.file_name_label.value)
