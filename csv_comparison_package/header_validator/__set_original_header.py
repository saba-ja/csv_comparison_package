import csv
from csv_comparison_package.error_handler import AppErrorHandler
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def set_original_header(comparable: Compare):
    with open(comparable.file_name, encoding=comparable.encoding) as csv_file:
        reader = csv.DictReader(csv_file)
        skipped_line = 1
        while skipped_line < comparable.header_row:
            try:
                next(csv_file)
            except StopIteration:
                raise AppErrorHandler(AppErrorHandler.header_row_out_of_range)
            skipped_line += 1

        comparable.original_header = reader.fieldnames
