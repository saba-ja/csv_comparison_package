# ###########################
# index_validator.import_file
# ###########################
parameter_for_import_file_passing_case = \
    {
        "file_name": "simple_data_sheet.csv",
        "header": [
            {
                "column_name": "id",
                "column_location": "1",
                "column_type": ""
            },
            {
                "column_name": "first_name",
                "column_location": "2",
                "column_type": ""
            },
            {
                "column_name": "last_name",
                "column_location": "3",
                "column_type": ""
            },
            {
                "column_name": "telephone",
                "column_location": "4",
                "column_type": ""
            }
        ],
        "index_column_name": [{
            "column_name": "id",
            "column_location": "1",

        }],
        "data_type": "object",
        "encoding": "utf-8",
        "header_row": 1,

    }


parameter_for_import_file_no_file_case = \
    {
        "file_name": "wrong_path_simple_data_sheet.csv",
        "header": [
            {
                "column_name": "id",
                "column_location": "1",
                "column_type": ""
            },
            {
                "column_name": "first_name",
                "column_location": "2",
                "column_type": ""
            },
            {
                "column_name": "last_name",
                "column_location": "3",
                "column_type": ""
            },
            {
                "column_name": "telephone",
                "column_location": "4",
                "column_type": ""
            }
        ],
        "index_column_name": [{
            "column_name": "id",
            "column_location": "1",

        }],
        "data_type": "object",
        "encoding": "utf-8",
        "header_row": 1,

    }

parameter_for_import_file_failing_decoding_raising_unicode_error_case = \
    {
        "file_name": "cp500.csv",
        "header": [
            {
                "column_name": "first_name",
                "column_location": "1",
                "column_type": ""
            },
            {
                "column_name": "last_name",
                "column_location": "2",
                "column_type": ""
            },
            {
                "column_name": "telephone",
                "column_location": "3",
                "column_type": ""
            }
        ],
        "index_column_name": [{
            "column_name": "first_name",
            "column_location": "1",

        }],
        "data_type": "object",
        "encoding": None,
        "header_row": 0,
    }

parameter_for_import_file_failing_decoding_raising_lookup_error_case = \
    {
        "file_name": "cp500.csv",
        "header": [
            {
                "column_name": "first_name",
                "column_location": "1",
                "column_type": ""
            },
            {
                "column_name": "last_name",
                "column_location": "2",
                "column_type": ""
            },
            {
                "column_name": "telephone",
                "column_location": "3",
                "column_type": ""
            }
        ],
        "index_column_name": [{
            "column_name": "first_name",
            "column_location": "1",

        }],
        "data_type": "object",
        "encoding": "",
        "header_row": 0,
    }

parameter_for_import_file_failing_decoding_raising_empty_error_case = \
    {
        "file_name": "cp500.csv",
        "header": [
            {
                "column_name": "first_name",
                "column_location": "1",
                "column_type": ""
            },
            {
                "column_name": "last_name",
                "column_location": "2",
                "column_type": ""
            },
            {
                "column_name": "telephone",
                "column_location": "3",
                "column_type": ""
            }
        ],
        "index_column_name": [{
            "column_name": "first_name",
            "column_location": "1",

        }],
        "data_type": "object",
        "encoding": "utf-8",
        "header_row": 1,
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