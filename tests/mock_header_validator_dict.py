####################################################
# input_validator.check_for_negative_header_row
####################################################


####################################################
# input_validator.check_for_header_row_location
####################################################
header_row_out_of_range = {'file_name': 'simple_csv_file.csv',
                           'encoding': 'UTF-8-SIG',
                           'header_row': 10}
header_row_in_range = {'file_name': 'simple_csv_file.csv',
                       'encoding': 'UTF-8-SIG',
                       'header_row': 1}

# ###########################
# header_validator.set_original_header
# ###########################

good_file_and_expected_header_1 = ({'file_name': 'simple_csv_file.csv',
                                    'encoding': 'UTF-8-SIG',
                                    'header_row': 1},
                                   ['first_name', 'last_name', 'telephone_number'])

good_file_and_expected_header_2 = ({'file_name': 'simple_csv_file.csv',
                                    'encoding': 'UTF-8-SIG',
                                    'header_row': 2},
                                   ['John', 'Doe', '123456789'])

good_file_and_expected_header_3 = ({'file_name': 'simple_csv_file.csv',
                                    'encoding': 'UTF-8-SIG',
                                    'header_row': 4},
                                   ['2/5/18', '25', "print('test')"])

failing_case_for_setting_original_header = {'file_name': 'simple_csv_file.csv',
                                            'encoding': 'UTF-8-SIG',
                                            'header_row': 20}

# ###########################
# header_validator.set_header
# ###########################

original_header_parameter_and_expected_header = (
    {'original_header': ['first_name', 'last_name', 'telephone_number']},
    [
        {'column_name': 'first_name',
         'column_location': 1,
         'column_type': ''
         },
        {'column_name': 'last_name',
         'column_location': 2,
         'column_type': ''},
        {'column_name': 'telephone_number',
         'column_location': 3,
         'column_type': ''}
    ])

# ###########################
# header_validator.strip_header
# ###########################

header_and_expected_strip_result = (
    {'header': [
        {'column_name': '   first_name   ',
         'column_location': 1,
         'column_type': ''},
        {'column_name': 'last\nname',
         'column_location': 2,
         'column_type': ''},
        {'column_name': '\n\n\ntelephone\t\tnumber',
         'column_location': 3,
         'column_type': ''}
    ]},
    [
        {'column_name': 'first_name',
         'column_location': 1,
         'column_type': ''},
        {'column_name': 'lastname',
         'column_location': 2,
         'column_type': ''},
        {'column_name': 'telephonenumber',
         'column_location': 3,
         'column_type': ''}
    ])

# ###########################
# header_validator.check_for_index_column
# ###########################

index_column_exist_in_header_1 = {
    'header': [
        {'column_name': 'id',
         'column_location': 1,
         'column_type': ''},
        {'column_name': 'first_name',
         'column_location': 2,
         'column_type': ''},
        {'column_name': 'last_name',
         'column_location': 3,
         'column_type': ''}
    ],
    'index_column_name': [{'column_name': 'id', 'column_location': 1}]
}

index_column_exist_in_header_2 = {
    'header': [
        {'column_name': 'id',
         'column_location': 3,
         'column_type': ''},
        {'column_name': 'first_name',
         'column_location': 2,
         'column_type': ''},
        {'column_name': 'last_name',
         'column_location': 1,
         'column_type': ''}
    ],
    'index_column_name': [{'column_name': 'id', 'column_location': 3}]
}

index_column_does_not_exist_in_header_1 = {
    'header': [
        {'column_name': 'id',
         'column_location': 4,
         'column_type': ''},
        {'column_name': 'first_name',
         'column_location': 2,
         'column_type': ''},
        {'column_name': 'last_name',
         'column_location': 3,
         'column_type': ''}
    ],
    'index_column_name': [{'column_name': 'id', 'column_location': 1}]
}

index_column_does_not_exist_in_header_2 = {
    'header': [
        {'column_name': 'id-wrong',
         'column_location': 1,
         'column_type': ''},
        {'column_name': 'first_name',
         'column_location': 2,
         'column_type': ''},
        {'column_name': 'last_name',
         'column_location': 1,
         'column_type': ''}
    ],
    'index_column_name': [{'column_name': 'id', 'column_location': 3}]
}

# ###########################
# header_validator.check_for_map_column
# ###########################

mapped_column_exist_in_header_1 = {
    'header': [
        {'column_name': 'id',
         'column_location': 4,
         'column_type': ''},
        {'column_name': 'first_name_1',
         'column_location': 2,
         'column_type': ''},
        {'column_name': 'last_name',
         'column_location': 3,
         'column_type': ''}
    ],
    'index_column_name': [{'column_name': 'id', 'column_location': 1}],
    'order': 0
}
mapped_column_exist_in_header_2 = {
    'header': [
        {'column_name': 'id',
         'column_location': 1,
         'column_type': ''},
        {'column_name': 'first_name_2',
         'column_location': 2,
         'column_type': ''},
        {'column_name': 'last_name',
         'column_location': 1,
         'column_type': ''}
    ],
    'index_column_name': [{'column_name': 'id', 'column_location': 3}],
    'order': 1
}

mapped_column_does_not_exist_in_header_1 = {
    'header': [
        {'column_name': 'id',
         'column_location': 4,
         'column_type': ''},
        {'column_name': 'first_name',
         'column_location': 2,
         'column_type': ''},
        {'column_name': 'last_name',
         'column_location': 3,
         'column_type': ''}
    ],
    'index_column_name': [{'column_name': 'id', 'column_location': 1}],
    'order': 0
}
mapped_column_does_not_exist_in_header_2 = {
    'header': [
        {'column_name': 'id',
         'column_location': 1,
         'column_type': ''},
        {'column_name': 'first_name',
         'column_location': 2,
         'column_type': ''},
        {'column_name': 'last_name',
         'column_location': 1,
         'column_type': ''}
    ],
    'index_column_name': [{'column_name': 'id', 'column_location': 3}],
    'order': 1
}

mapped_column_when_conflict_with_index = {
    'header': [
        {'column_name': 'id',
         'column_location': 1,
         'column_type': ''},
        {'column_name': 'first_name',
         'column_location': 2,
         'column_type': ''},
        {'column_name': 'last_name',
         'column_location': 1,
         'column_type': ''}
    ],
    'index_column_name': [{'column_name': 'id', 'column_location': 1}],
    'order': 1
}

# ###########################
# header_validator.format_map_column
# ###########################

map_column_different_names = [(
    {'column_name': 'first_name_1', 'column_location': 3, 'column_type': ''},
    {'column_name': 'first_name_2', 'column_location': 4, 'column_type': ''}
)]

header_for_map_column_and_expected_result_file_1 = (
    {
        'header': [
            {'column_name': 'first_name_1',
             'column_location': 3,
             'column_type': ''},
        ],
        'order': 0
    },
    {'column_name': '[first_name_1]-[first_name_2]', 'column_location': 3, 'column_type': 'mapped'}
)

header_for_map_column_and_expected_result_file_2 = (
    {
        'header': [
            {'column_name': 'first_name_2', 'column_location': 4, 'column_type': ''},
        ],
        'order': 1
    },
    {'column_name': '[first_name_1]-[first_name_2]', 'column_location': 4, 'column_type': 'mapped'}
)
# -----------------
map_column_identical_names = [(
    {'column_name': 'first_name', 'column_location': 3},
    {'column_name': 'first_name', 'column_location': 4}
)]

header_for_map_column_and_expected_result_file_1_identical_names = (
    {
        'header': [
            {'column_name': 'first_name', 'column_location': 3, 'column_type': ''},
        ],
        'order': 0
    },
    {'column_name': 'first_name', 'column_location': 3, 'column_type': 'mapped'}
)

header_for_map_column_and_expected_result_file_2_identical_names = (
    {
        'header': [
            {'column_name': 'first_name', 'column_location': 4, 'column_type': ''},
        ],
        'order': 1
    },
    {'column_name': 'first_name', 'column_location': 4, 'column_type': 'mapped'}
)
# -----------------
map_column_names_that_are_not_in_header = [(
    {'column_name': 'first_name_1', 'column_location': 3, 'column_type': ''},
    {'column_name': 'first_name_2', 'column_location': 4, 'column_type': ''}
)]

header_that_are_not_in_map_column_and_expected_result = (
    {
        'header': [
            {'column_name': 'some_other_first_name', 'column_location': 3, 'column_type': ''},
        ],
        'order': 0
    },
    {'column_name': 'some_other_first_name', 'column_location': 3, 'column_type': ''}
)

format_map_function_mapped_column_when_conflict_with_index = (
    {
        'header': [
            {'column_name': 'id',
             'column_location': 1,
             'column_type': ''},
            {'column_name': 'first_name',
             'column_location': 2,
             'column_type': ''},
            {'column_name': 'last_name',
             'column_location': 1,
             'column_type': ''}
        ],
        'index_column_name': [
            {'column_name': 'id', 'column_location': 1}],
        'order': 1
    },
    [
        {'column_name': 'id',
         'column_location': 1,
         'column_type': ''},
        {'column_name': 'first_name',
         'column_location': 2,
         'column_type': ''},
        {'column_name': 'last_name',
         'column_location': 1,
         'column_type': ''}
    ]
)

# ###########################
# header_validator.format_unnamed_column
# ###########################

header_with_unnamed_columns_and_expected_result = (
    {
        'header': [
            {'column_name': '', 'column_location': 3, 'column_type': ''},
        ],
        'order': 0,
        'index_column_name': [{'column_name': 'id', 'column_location': 3}]
    },
    [{'column_name': '@unnamed.3', 'column_location': 3, 'column_type': 'unnamed'}]
)

header_with_named_columns_and_expected_result = (
    {
        'header': [
            {'column_name': 'file_name', 'column_location': 3, 'column_type': ''},
        ],
        'order': 0,
        'index_column_name': [{'column_name': 'id', 'column_location': 3}]
    },
    [{'column_name': 'file_name', 'column_location': 3, 'column_type': ''}]
)

# ###########################
# header_validator.format_duplicate_column
# ###########################

header_with_duplicate_columns_and_expected_result = (
    {
        'header': [
            {'column_name': 'file_name', 'column_location': 3, 'column_type': ''},
            {'column_name': 'file_name', 'column_location': 4, 'column_type': ''},
        ],
        'order': 0
    },
    [{'column_name': 'file_name@duplicate.3', 'column_location': 3, 'column_type': 'duplicate'},
     {'column_name': 'file_name@duplicate.4', 'column_location': 4, 'column_type': 'duplicate'}]
)

header_with_mixed_dup_none_dup_col_and_expected_result = (
    {
        'header': [
            {'column_name': 'file_name', 'column_location': 3, 'column_type': ''},
            {'column_name': 'file_name', 'column_location': 4, 'column_type': ''},
            {'column_name': 'not_repeated_val', 'column_location': 5, 'column_type': ''},
            {'column_name': 'another_not_repeated_val', 'column_location': 6, 'column_type': ''},

        ],
        'order': 0
    },
    [{'column_name': 'file_name@duplicate.3', 'column_location': 3, 'column_type': 'duplicate'},
     {'column_name': 'file_name@duplicate.4', 'column_location': 4, 'column_type': 'duplicate'},
     {'column_name': 'not_repeated_val', 'column_location': 5, 'column_type': ''},
     {'column_name': 'another_not_repeated_val', 'column_location': 6, 'column_type': ''},
     ]
)

# ###########################
# header_validator.get_header_index
# ###########################

header_for_get_header_index = {
    'header': [
        {'column_name': 'file_name', 'column_location': 3, 'column_type': ''},
        {'column_name': 'file_name', 'column_location': 4, 'column_type': ''},
        {'column_name': 'not_repeated_val', 'column_location': 5, 'column_type': ''},
        {'column_name': 'another_not_repeated_val', 'column_location': 6, 'column_type': ''},

    ],
}

# ###########################
# header_validator.is_index
# ###########################

looking_for_is_index_function_when_index_exist = {
    'index_column_name': [{'column_name': 'id', 'column_location': 1}],
    'order': 0
}

looking_for_is_index_function_when_index_does_not_exist = {
    'index_column_name': [{'column_name': 'some value', 'column_location': 1}],
    'order': 0
}

# ###########################
# header_validator.is_mapped
# ###########################

looking_for_mapped_column_when_exist_1 = {
    'order': 0
}
looking_for_mapped_column_when_exist_2 = {
    'order': 1
}
###########################
# header_validator.format_disjunctive_column
###########################

header_for_disjunctive_check_and_not_index_file_1 = \
    {
        'header': [
            {'column_name': 'file_name_address_1', 'column_location': 4, 'column_type': ''},
        ],
        'order': 0,
        'index_column_name': [{'column_name': 'id', 'column_location': 1}],
    }
header_for_disjunctive_check_and_not_index_file_2 = \
    {
        'header': [
            {'column_name': 'file_name_address_2', 'column_location': 4,
             'column_type': ''},
        ],
        'order': 1,
        'index_column_name': [
            {'column_name': 'id', 'column_location': 1}],
    }

header_for_disjunctive_check_and_is_index_file_1 = \
    {
        'header': [
            {'column_name': 'id', 'column_location': 1, 'column_type': ''},
        ],
        'order': 0,
        'index_column_name': [{'column_name': 'id', 'column_location': 1}],
    }

header_for_disjunctive_check_and_column_is_in_other_file_1 = \
    {
        'header': [
            {'column_name': 'file_name', 'column_location': 3, 'column_type': ''},
        ],
        'order': 0,
        'index_column_name': [{'column_name': 'id', 'column_location': 1}],
    }

header_for_disjunctive_check_and_column_is_in_other_file_2 = \
    {
        'header': [
            {'column_name': 'file_name', 'column_location': 3, 'column_type': ''},
        ],
        'order': 1,
        'index_column_name': [{'column_name': 'id', 'column_location': 1}],
    }

###########################
# header_validator.format_not_checked_column
###########################
header_for_not_checked_columns = (
    {
        'header': [
            {'column_name': 'file_name', 'column_location': 3, 'column_type': ''},
        ],
        'order': 0,
        'index_column_name': [{'column_name': 'id', 'column_location': 1}],
        'compare_only_mapped_columns': True
    },
    [{'column_name': 'file_name@notChecked.3', 'column_location': 3,
      'column_type': 'not_checked'}]
)

header_for_not_checked_columns_when_mapped_column_is_empty = (
    {
        'header': [
            {'column_name': 'file_name', 'column_location': 3, 'column_type': ''},
        ],
        'order': 0,
        'index_column_name': [{'column_name': 'id', 'column_location': 1}],
        'compare_only_mapped_columns': True
    },
    [{'column_name': 'file_name', 'column_location': 3, 'column_type': ''}]
)

header_for_not_checked_columns_when_column_type_is_not_empty = (
    {
        'header': [
            {'column_name': 'file_name', 'column_location': 3, 'column_type': 'duplicate'},
        ],
        'order': 0,
        'index_column_name': [{'column_name': 'id', 'column_location': 1}],
        'compare_only_mapped_columns': True
    },
    [{'column_name': 'file_name', 'column_location': 3, 'column_type': 'duplicate'}]
)

###########################
# header_validator.drop_unnamed_column
###########################

parameter_for_drop_unnamed_column = {
    'header': [
        {'column_name': 'id', 'column_location': 1, 'column_type': ''},
        {'column_name': 'file_name', 'column_location': 2, 'column_type': 'unnamed'},
    ],
    'order': 0,
    'index_column_name': [{'column_name': 'id', 'column_location': 1}],
    'compare_only_mapped_columns': True
}
