from csv_comparison_package import Field
from csv_comparison_package import Compare
from csv_comparison_package import data_exporter


def create_name_for_output_file(comparable_a, comparable_b):
    now = data_exporter.get_formatted_time()
    name_a = data_exporter.extract_file_name_from_path(comparable_a)
    name_b = data_exporter.extract_file_name_from_path(comparable_b)
    excel_name = f"F1_{name_a}_F2_{name_b}_{now}.{Field.excel_extension.value}"
    Compare.output_file_name = excel_name
