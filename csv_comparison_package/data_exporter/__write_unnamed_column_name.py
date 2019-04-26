from csv_comparison_package import Compare
from csv_comparison_package import Field
from csv_comparison_package import header_validator
from csv_comparison_package.decorator import call_each
from csv_comparison_package import data_exporter


@call_each
def write_unnamed_column_name(comparable: Compare):
    current_column = comparable.unnamed_column_start
    unnamed_headers = header_validator.get_unnamed_column_name(comparable)

    for index, header_name in enumerate(unnamed_headers):
        Compare.worksheet_master.write(2, current_column,
                                       header_name[Field.column_name.value],
                                       data_exporter.select_format_left_or_bottom(comparable,
                                                                                  index))
        current_column += 1
