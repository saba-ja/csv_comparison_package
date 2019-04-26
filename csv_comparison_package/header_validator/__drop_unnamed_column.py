from csv_comparison_package import AppErrorHandler
from csv_comparison_package import Field


def drop_unnamed_column(comparable):
    """
    Unnamed columns must drop from the data frame
    To be dropped they must be flagged as unnamed
    Their location also must match the location in the data from column
    If these two match the drop the column
    To get started write something here
    """
    print("\n\n\n\n")

    for header in comparable.header:
        df_col_name = comparable.data_frame.columns.get_values()[header[Field.column_location.value] - 1]
        if df_col_name != header[Field.column_name.value]:
            raise AppErrorHandler(AppErrorHandler.incorrect_column_location)
        print("-- From header obj")
        print(header[Field.column_name.value])
        print(header[Field.column_location.value])
        print(header[Field.column_type.value])
        print("-- From data frame")
        print()

    print("\n\n\n\n")