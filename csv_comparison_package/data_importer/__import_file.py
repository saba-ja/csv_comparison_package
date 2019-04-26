import pandas as pd
from csv_comparison_package.field import Field
from csv_comparison_package import AppErrorHandler
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def import_file(comparable: Compare):
    try:
        comparable.original_data_frame = \
            pd.read_csv(filepath_or_buffer=comparable.file_name,
                        names=[name[Field.column_name.value] for name in comparable.header],
                        dtype=comparable.data_type,
                        encoding=comparable.encoding,
                        skiprows=comparable.header_row,
                        index_col=False,
                        skipinitialspace=True,
                        na_filter=True,
                        skip_blank_lines=True)

        if comparable.original_data_frame.empty:
            raise AppErrorHandler(AppErrorHandler.import_error)

    except FileNotFoundError:
        raise AppErrorHandler(AppErrorHandler.no_file)
    except UnicodeDecodeError:
        raise AppErrorHandler(AppErrorHandler.unknown_encoding)
    except LookupError:
        raise AppErrorHandler(AppErrorHandler.unknown_encoding)
