from enum import Enum


class Field(Enum):
    file_1_name = "file_1_name"
    file_2_name = "file_2_name"
    file_1_header_row = "file_1_header_row"
    file_2_header_row = "file_2_header_row"
    file_1_index_column_name = "file_1_index_column_name"
    file_2_index_column_name = "file_2_index_column_name"
    file_1_data_type = "file_1_data_type"
    file_2_data_type = "file_2_data_type"
    file_1_2_map_columns = "file_1_2_map_columns"
    file_1_2_worksheet_name = "file_1_2_worksheet_name"
    file_1_2_compare_only_mapped_columns = "file_1_2_compare_only_mapped_columns"
    file_1_hide_modified_columns = "file_1_hide_modified_columns"
    file_2_hide_modified_columns = "file_2_hide_modified_columns"
    file_1_hide_not_checked_columns = "file_1_hide_not_checked_columns"
    file_2_hide_not_checked_columns = "file_2_hide_not_checked_columns"
    file_1_hide_disjunctive_columns = "file_1_hide_disjunctive_columns"
    file_2_hide_disjunctive_columns = "file_2_hide_disjunctive_columns"
    file_1_hide_duplicate_columns = "file_1_hide_duplicate_columns"
    file_2_hide_duplicate_columns = "file_2_hide_duplicate_columns"
    file_1_hide_unnamed_columns = "file_1_hide_unnamed_columns"
    file_2_hide_unnamed_columns = "file_2_hide_unnamed_columns"
    file_1_2_hide_not_modified_rows = "file_1_2_hide_not_modified_rows"
    file_1_2_output_path = "file_1_2_output_path"
    file_1_2_output_name = "file_1_2_output_name"
    file_1_encoding = "file_1_encoding"
    file_2_encoding = "file_2_encoding"
    file_1_delimiter = "file_1_delimiter"
    file_2_delimiter = "file_2_delimiter"

    file_1_flag = "_1_"
    file_2_flag = "_2_"
    file_1_2_flag = "_1_2_"

    prm_name = "prm_name"
    prm_required = "prm_required"
    prm_default_value = "prm_default_value"
    prm_type = "prm_type"
    prm_should_be_strip = "prm_should_be_strip"
    prm_can_have_special_char = "prm_can_have_special_char"

    column_name = "column_name"
    column_location = "column_location"
    column_type = "column_type"

    empty_string = ""

    index = "index"
    index_column_tag = "index"
    duplicate = "duplicate"
    mapped = "mapped"
    unnamed = "unnamed"
    disjunctive = "disjunctive"
    disjunctive_column_tag = "notFound"
    not_checked = "not_checked"
    not_checked_column_tag = "notChecked"

    excel_extension = "xlsx"
    general_column_width = 15

    # Definition (label) of each row
    file_name_label = "File Names:"
    column_type_label = "Column Types:"
    column_name_label = "Column Names:"

    # Column Types Title
    index_column_label = "Unique ID"
    checked_column_label = "Columns Checked for Modification"
    not_checked_column_label = "Columns NOT Checked for Modification"
    disjunctive_column_label = "Columns only in"
    duplicate_column_label = "Columns with duplicate names"
    unnamed_column_label = " Columns with no name "

    # Pandas
    pandas_original_index = "@original_row"

    CONST_LABEL_FOR_EMPTY_INDICES_FILE_1 = "F1 EMP ID:"
    CONST_LABEL_FOR_EMPTY_INDICES_FILE_2 = "F2 EMP ID:"
    CONST_LABEL_FOR_DUPLICATE_INDICES_FILE_1 = "F1 DUP ID:"
    CONST_LABEL_FOR_DUPLICATE_INDICES_FILE_2 = "F2 DUP ID:"
    CONST_LABEL_FOR_DISJUNCTIVE_INDICES_FILE_1 = "F1 ONLY:"
    CONST_LABEL_FOR_DISJUNCTIVE_INDICES_FILE_2 = "F2 ONLY:"
    CONST_LABEL_FOR_COMPARED_ROWS_FILE_1_2 = "F1 F2 WITH DIFF:"
    CONST_LABEL_FOR_IDENTICAL_ROWS_FILE_1_2 = "F1 F2 IDENTICAL:"
