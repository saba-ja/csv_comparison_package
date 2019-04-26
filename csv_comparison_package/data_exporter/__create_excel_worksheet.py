from csv_comparison_package import Compare


def create_excel_worksheet():
    Compare.worksheet_master = Compare.workbook.add_worksheet(Compare.worksheet_name)
