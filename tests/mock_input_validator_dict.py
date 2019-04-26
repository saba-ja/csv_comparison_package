####################################################
# input_validator.check_for_type_dictionary
####################################################
parameter_with_type_list = []
parameter_with_type_string = "my string"
parameter_with_type_integer = 1
parameter_with_type_tuple = ('a', 'b')
parameter_with_type_set = {1, 2, 3}
parameter_with_type_dict = {'a': 1, 'b': 2}

####################################################
# input_validator.check_for_empty_dictionary
####################################################

parameter_with_no_value = {}
parameter_with_some_key_value_pair = {"file_1_name": "/PATH/TO/FIRST/FILE"}

####################################################
# input_validator.check_for_key_to_be_string_type
####################################################

parameter_with_integer_in_the_key = {1: "some text"}
parameter_with_function_in_key = {print: "some text"}
parameter_with_blank_in_key = {" ": "some text"}
parameter_with_string_type_key = {"file_1_name": "some text"}

####################################################
# input_validator.check_for_required_key
####################################################

parameter_with_wrong_file_name_key = {"file_n_name": "myfile.csv"}
parameter_with_missing_required_key = {
    "file_1_name": "/PATH/TO/FIRST/FILE",
    # "file_2_name": "/PATH/TO/SECOND/FILE",
}

parameter_with_all_required_key = {
    "file_1_name": "./sheet_1.csv",
    "file_2_name": "./sheet_2.csv",

    "file_1_index_column_name": [{"column_name": "Social Security ID"}],
    "file_2_index_column_name": [{"column_name": "Social Security ID"}],

    "file_1_2_map_columns": [({"column_name": "First Name"}, {"column_name": "First Name"})],

    "file_1_2_compare_only_mapped_columns": True,
    "file_1_header_row": 1,
    "file_2_header_row": 1,
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

    "file_1_2_output_path": './'

}
####################################################
# input_validator.check_for_type_string
# input_validator.parameter_with_blank_required_value
####################################################
parameter_with_required_string_value_but_submitted_integer_value_type = {
    "file_1_name": 1,
}

parameter_with_required_string_value_but_submitted_function_value_type = {
    "file_1_name": print,
}

parameter_with_required_string_value_but_submitted_list_value_type = {
    "file_1_name": [1, 2, 3],
}

parameter_with_required_string_value_but_submitted_dict_value_type = {
    "file_1_name": {1, 2, 3},
}

parameter_with_blank_required_value = {
    "file_1_name": "",
}

parameter_with_not_required_and_type_string_but_int_type_submission = {
    "file_1_2_output_path": 1
}

parameter_with_blank_but_not_required_value = {
    "file_1_2_output_path": "",
}

parameter_with_blank_space_required_value = {
    "file_1_name": "  ",
}

parameter_with_special_character = {
    "file_1_name": "<file#name.csv",
}

####################################################
# check_for_parameter_strip
####################################################
parameter_with_blank_required_value_for_stripping_test = {
    "file_1_name": " 8888 ",
    "not_existing_key": " some text  "
}

expected_parameter_with_blank_required_value_for_stripping_test = {
    "file_1_name": "8888",
    "not_existing_key": " some text  "
}

parameter_with_blank_space_required_value_for_stripping_test = {
    "file_1_name": "      ",
}

expected_parameter_with_blank_space_required_value_for_stripping_test = {
    "file_1_name": "",
}

parameter_with_special_character_for_stripping_test = {
    "file_1_name": "<file#name.csv",
}

expected_parameter_with_special_character_for_stripping_test = {
    "file_1_name": "<file#name.csv",
}

parameter_with_type_string_but_wrong_submitted_type = {
    "file_1_name": 1,
    "file_2_name": print
}

expected_parameter_with_type_string_but_wrong_submitted_type = {
    "file_1_name": 1,
    "file_2_name": print
}

####################################################
# input_validator.check_for_special_character
####################################################
parameter_with_forbidden_character = {
    "file_1_name": "<file#name.csv"
}

parameter_with_forbidden_character_but_not_required_key = {
    "file_1_2_output_path": "<file#name.csv"
}

parameter_with_no_forbidden_character = {
    "file_1_name": "file#name.csv"
}

parameter_with_no_forbidden_character_but_not_string_type = {
    "file_1_2_output_path": 1
}
####################################################
# input_validator.check_for_default_schema
####################################################

parameter_with_non_existing_keys = {
    "file_n_name": "some name"
}

parameter_with_both_existing_and_non_existing_keys = {
    "file_1_name": "some name",
    "file_n_name": "some name"
}

parameter_with_existing_keys = {
    "file_1_name": "some name"
}

####################################################
# input_validator.check_submitted_keys_to_be_string_type
####################################################
parameter_of_with_int_type_key = {
    1: "some text"
}

parameter_of_with_function_type_key = {
    print: "some text"
}

####################################################
# input_validator.check_for_parameter_type
####################################################
parameter_is_string_but_integer_is_submitted = {
    "file_1_2_output_path": 8,
}

parameter_is_string_but_boolean_is_submitted = {
    "file_1_2_output_path": True,
}

parameter_is_boolean_but_empty_string_is_submitted = {
    "file_1_hide_modified_columns": "",
}

parameter_is_string_but_list_is_submitted = {
    "file_1_2_output_path": ['Some text'],
}

parameter_with_existing_keys_for_type_checking = {
    "file_1_2_output_path": "some name"
}

parameter_is_string_but_python_syntax_is_submitted = {
    "file_1_2_output_path": print('2*4'),
}

parameter_is_list_but_boolean_is_submitted = {
    "file_1_2_map_columns": True
}

# #####################################
# input_validator.check_for_required_parameter_value_with_any_type_to_not_be_empty
# ######################################
parameter_is_required_and_must_be_string_but_empty_value_is_given = {
    "file_1_name": ""
}

parameter_is_required_and_must_be_list_but_empty_value_is_given = {
    "file_1_index_column_name": ""
}

parameter_is_not_required_but_is_submitted_for_empty_checking = {
    "file_1_2_output_path": ""
}

parameter_is_required_and_correct_val_is_given_empty_checking = {
    "file_1_name": "some name"
}
####################################################
# input_validator.check_for_input_file_existence
# input_validator.check_for_file_read_access
####################################################

parameter_for_input_file_existence = {
    "file_1_name": "/PATH/TO/FIRST/FILE"
}

####################################################
# input_validator.check_file_type_to_be_csv
####################################################
