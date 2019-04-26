import csv
from csv_comparison_package import AppErrorHandler
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def check_for_delimiter(comparable: Compare):
    with open(comparable.file_name, newline='', encoding=comparable.encoding) as file:
        text = file.readline()
        dialect = csv.Sniffer().sniff(text)
        if dialect.delimiter != comparable.delimiter:
            raise AppErrorHandler(AppErrorHandler.invalid_delimiter)

