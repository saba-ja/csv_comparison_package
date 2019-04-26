from csv_comparison_package import Setting
from csv_comparison_package import Compare
from csv_comparison_package import input_validator
from csv_comparison_package import header_validator
from csv_comparison_package import data_importer
from csv_comparison_package import index_validator
from csv_comparison_package import cell_comparator
from csv_comparison_package import data_exporter


def export_to_excel(user_parameters):
    setting = Setting(user_parameters)
    comparable = [Compare(order=0), Compare(order=1)]
    # #############################################################################################
    input_validator.check_for_type_dictionary(setting)
    input_validator.check_for_empty_dictionary(setting)
    input_validator.check_for_key_to_be_string_type(setting)
    input_validator.check_for_required_key(setting)
    input_validator.check_for_type_string(setting)
    input_validator.check_for_parameter_strip(setting)
    input_validator.check_for_special_character(setting)
    input_validator.check_for_empty_value(setting)
    input_validator.check_for_default_schema(setting)
    input_validator.check_for_parameter_type(setting)
    # TODO need to validation the map_columns
    # TODO need to validation the index_column
    input_validator.set_default(setting)
    input_validator.set_parameter(setting, comparable[0], comparable[1])
    input_validator.check_for_input_file_existence(comparable)
    input_validator.check_for_file_read_access(comparable)
    input_validator.check_for_file_write_access(comparable)
    input_validator.check_for_file_size(comparable)
    input_validator.set_file_encoding(comparable)
    input_validator.check_for_file_encoding(comparable)
    input_validator.check_for_delimiter(comparable)
    # #############################################################################################
    header_validator.check_for_negative_header_row(comparable)
    header_validator.check_for_header_row_location(comparable)
    header_validator.set_original_header(comparable)
    header_validator.set_header(comparable)
    header_validator.strip_header(comparable)
    header_validator.check_for_index_name_existence(comparable)
    header_validator.set_index_column_location(comparable)
    header_validator.check_for_index_column(comparable)
    header_validator.check_for_map_column_existence(comparable)
    header_validator.set_map_column_location(comparable)
    header_validator.check_for_map_column(comparable)

    header_validator.format_index_column(comparable)
    header_validator.format_map_column(comparable)
    header_validator.format_unnamed_column(comparable)
    header_validator.format_duplicate_column(comparable)
    header_validator.format_disjunctive_column(comparable[0], comparable[1])
    header_validator.format_disjunctive_column(comparable[1], comparable[0])
    header_validator.format_not_for_checked_column(comparable)
    header_validator.set_index_column_number(comparable)
    header_validator.set_regular_column_number(comparable)
    header_validator.set_not_checked_column_number(comparable)
    header_validator.set_map_column_number(comparable)
    header_validator.set_disjunctive_column_number(comparable)
    header_validator.set_duplicate_column_number(comparable)
    header_validator.set_unnamed_column_number(comparable)
    header_validator.set_start_column(comparable[0], comparable[1])
    header_validator.set_end_column(comparable)
    header_validator.set_start_end_index_column(comparable)
    header_validator.set_start_end_checked_column(comparable)
    header_validator.set_start_end_not_checked_column(comparable)
    header_validator.set_start_end_disjunctive_column(comparable)
    header_validator.set_start_end_duplicate_column(comparable)
    header_validator.set_start_end_unnamed_column(comparable)
    # #############################################################################################
    data_importer.import_file(comparable)
    data_importer.freeze_pandas_index(comparable)
    data_importer.set_data_frame(comparable)
    data_importer.extract_not_checked_column(comparable)
    data_importer.extract_disjunctive_column(comparable)
    data_importer.extract_duplicate_column(comparable)
    data_importer.extract_unnamed_column(comparable)
    data_importer.drop_not_checked_column(comparable)
    data_importer.drop_disjunctive_column(comparable)
    data_importer.drop_duplicate_column(comparable)
    data_importer.drop_unnamed_column(comparable)
    # #############################################################################################
    index_validator.stringify_index(comparable)
    index_validator.sort_index(comparable)
    index_validator.strip_index(comparable)
    index_validator.check_for_empty_index(comparable)
    index_validator.drop_empty_index(comparable)
    index_validator.check_for_duplicate_index(comparable)
    index_validator.drop_duplicate_index(comparable)
    index_validator.check_for_disjunctive_index(comparable[0], comparable[1])
    index_validator.check_for_disjunctive_index(comparable[1], comparable[0])
    index_validator.drop_disjunctive_index(comparable)
    # #############################################################################################
    cell_comparator.validate_index_identity(comparable[0], comparable[1])
    # TODO need to add validate column names identity ( all the columns in a must be in b except index column)
    cell_comparator.remove_nan(comparable)
    cell_comparator.remove_non_printable_char(comparable)
    cell_comparator.remove_white_space_char(comparable)
    cell_comparator.copy_df_to_trimmed_df(comparable)

    # TODO need to add check_for_identical_row
    # TODO need to add drop_identical_row
    # TODO add find differences
    # TODO generate final frame (index, checked, not checked, dis, dup, un, identical row, mod row)
    # #############################################################################################

    data_exporter.create_name_for_output_file(comparable[0], comparable[1])
    data_exporter.create_excel_workbook()
    data_exporter.create_excel_worksheet()
    data_exporter.add_local_excel_format(comparable)
    data_exporter.apply_column_general_format(comparable)
    data_exporter.write_file_name_label()
    data_exporter.write_file_name_title(comparable)
    data_exporter.write_column_type_label()
    data_exporter.write_index_column_type_title(comparable)
    data_exporter.write_checked_column_type_title(comparable)
    data_exporter.write_not_checked_column_type_title(comparable)
    data_exporter.write_disjunctive_column_type_title(comparable)
    data_exporter.write_duplicate_column_type_title(comparable)
    data_exporter.write_unnamed_column_type_title(comparable)

    data_exporter.apply_checked_column_hide_condition(comparable)
    data_exporter.apply_not_checked_column_hide_condition(comparable)
    data_exporter.apply_disjunctive_column_hide_condition(comparable)
    data_exporter.apply_duplicate_column_hide_condition(comparable)
    data_exporter.apply_unnamed_column_hide_condition(comparable)

    data_exporter.write_column_name_label()
    data_exporter.write_index_column_name(comparable)
    data_exporter.write_checked_column_name(comparable)
    data_exporter.write_not_checked_column_name(comparable)
    data_exporter.write_disjunctive_column_name(comparable)
    data_exporter.write_duplicate_column_name(comparable)
    data_exporter.write_unnamed_column_name(comparable)
    data_exporter.close_excel_workbook()


if __name__ == "__main__":
    parameters = {
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~ FILE SETUP ~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        "file_1_name":
            "/Users/janamian/Documents/workstation/csv_comparison_package/"
            "tests/mock_data/sheet_1.csv",
        "file_2_name":
            "/Users/janamian/Documents/workstation/csv_comparison_package/"
            "tests/mock_data/sheet_2.csv",

        "file_1_index_column_name": [{"column_name": "Social Security ID", }],
        "file_2_index_column_name": [{"column_name": "Social Security ID"}],

        "file_1_2_map_columns": [(
            {"column_name": "First Name"},
            {"column_name": "First Name"},
            {"column_name": "Last Name"},
            {"column_name": "Last Name"},
        )],

        "file_1_2_compare_only_mapped_columns": True,
        "file_1_header_row": 1,
        "file_2_header_row": 1,
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~ HIDE AND SHOW SETUP ~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        "file_1_hide_modified_columns": False,
        "file_2_hide_modified_columns": False,

        "file_1_hide_not_checked_columns": True,
        "file_2_hide_not_checked_columns": True,

        "file_1_hide_disjunctive_columns": True,
        "file_2_hide_disjunctive_columns": True,

        "file_1_hide_duplicate_columns": True,
        "file_2_hide_duplicate_columns": True,

        "file_1_hide_unnamed_columns": True,
        "file_2_hide_unnamed_columns": True,

        "file_1_2_hide_not_modified_rows": True,

        "file_1_2_output_path": '/Users/janamian/Documents/workstation/csv_comparison_package/'

    }

    export_to_excel(parameters)
