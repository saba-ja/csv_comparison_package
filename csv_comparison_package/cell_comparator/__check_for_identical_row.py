from csv_comparison_package import Compare
from csv_comparison_package import Field

# TODO LEFT HERE
def check_for_identical_row(comparable_a: Compare, comparable_b: Compare):

    """
    Sort both data frames
    Both data frames must have the same indices
    Get indices of one data frame
    for each all the indices


    """

    comparable_a_index_name = comparable_a.index_column_name[0][
        Field.column_name.value]  # not supporting multi index
    comparable_b_index_name = comparable_b.index_column_name[0][Field.column_name.value]

    f1_index_of_identical_row = []
    f2_index_of_identical_row = []

    for index_val in data_frame_1_index:
        identical_cells_in_the_row = True
        f1_pandas_index = df_1.loc[index_val, const.CONST_INDEX_NAME_FOR_DEFAULT_PANDAS_INDEX_COLUMN]
        f2_pandas_index = df_2.loc[index_val, const.CONST_INDEX_NAME_FOR_DEFAULT_PANDAS_INDEX_COLUMN]
        for header_val in data_frame_1_headers_with_index_column_removed_set:
            f1_str = df_1.loc[index_val, header_val]
            f2_str = df_2.loc[index_val, header_val]

            if f1_str != f2_str:
                identical_cells_in_the_row = False
                break
            pass

        if identical_cells_in_the_row:
            f1_index_of_identical_row.append((f1_pandas_index, index_val))
            f2_index_of_identical_row.append((f2_pandas_index, index_val))

