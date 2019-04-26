import os
import xlsxwriter
from csv_comparison_package import Compare


def create_excel_workbook():
    """
    See the following document for more information
    http://xlsxwriter.readthedocs.io/working_with_memory.html
    """
    excel_name = os.path.join(Compare.output_path, Compare.output_file_name)
    Compare.workbook = xlsxwriter.Workbook(
        excel_name, {'strings_to_urls': False,
                     'strings_to_numbers': True,
                     'constant_memory': False})
