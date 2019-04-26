from csv_comparison_package import excel_schema
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def add_local_excel_format(comparable: Compare):
    comparable.column_general_format = comparable.workbook.add_format(
        excel_schema.general_column_format[comparable.order])

    comparable.header_format_left_border = comparable.workbook.add_format(
        excel_schema.header_format_left_border[comparable.order])

    comparable.header_format_left_bottom_border = comparable.workbook.add_format(
        excel_schema.header_format_left_bottom_border[comparable.order])

    comparable.header_format_bottom_border = comparable.workbook.add_format(
        excel_schema.header_format_bottom_border[comparable.order])

    comparable.header_format = comparable.workbook.add_format(
        excel_schema.header_format[comparable.order])
