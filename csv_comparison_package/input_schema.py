from csv_comparison_package.field import Field


class Schema:

    default_schema = [
        {
            Field.prm_name.value: Field.file_1_name.value,
            Field.prm_required.value: True,
            Field.prm_default_value.value: None,
            Field.prm_type.value: str,
            Field.prm_should_be_strip.value: True,
            Field.prm_can_have_special_char.value: False
        },
        {
            Field.prm_name.value: Field.file_2_name.value,
            Field.prm_required.value: True,
            Field.prm_default_value.value: None,
            Field.prm_type.value: str,
            Field.prm_should_be_strip.value: True,
            Field.prm_can_have_special_char.value: False
        },
        {
            Field.prm_name.value: Field.file_1_header_row.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: 0,
            Field.prm_type.value: int,
        },
        {
            Field.prm_name.value: Field.file_2_header_row.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: 0,
            Field.prm_type.value: int,
        },
        {
            Field.prm_name.value: Field.file_1_index_column_name.value,
            Field.prm_required.value: True,
            Field.prm_default_value.value: None,
            Field.prm_type.value: list,
        },
        {
            Field.prm_name.value: Field.file_2_index_column_name.value,
            Field.prm_required.value: True,
            Field.prm_default_value.value: None,
            Field.prm_type.value: list,
        },

        {
            Field.prm_name.value: Field.file_1_data_type.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: "object",
            Field.prm_type.value: str,
        },
        {
            Field.prm_name.value: Field.file_2_data_type.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: "object",
            Field.prm_type.value: str,
        },
        {
            Field.prm_name.value: Field.file_1_2_worksheet_name.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: "Master",
            Field.prm_type.value: str,
        },

        {
            Field.prm_name.value: Field.file_1_2_map_columns.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: [],
            Field.prm_type.value: list,
        },
        {
            Field.prm_name.value: Field.file_1_2_compare_only_mapped_columns.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: False,
            Field.prm_type.value: bool,
        },
        {
            Field.prm_name.value: Field.file_1_hide_modified_columns.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: False,
            Field.prm_type.value: bool,
        },
        {
            Field.prm_name.value: Field.file_2_hide_modified_columns.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: False,
            Field.prm_type.value: bool,
        },
        {
            Field.prm_name.value: Field.file_1_hide_not_checked_columns.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: False,
            Field.prm_type.value: bool,
        },
        {
            Field.prm_name.value: Field.file_2_hide_not_checked_columns.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: False,
            Field.prm_type.value: bool,
        },
        {
            Field.prm_name.value: Field.file_1_hide_disjunctive_columns.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: False,
            Field.prm_type.value: bool,
        },
        {
            Field.prm_name.value: Field.file_2_hide_disjunctive_columns.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: False,
            Field.prm_type.value: bool,
        },
        {
            Field.prm_name.value: Field.file_1_hide_duplicate_columns.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: False,
            Field.prm_type.value: bool,
        },
        {
            Field.prm_name.value: Field.file_2_hide_duplicate_columns.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: False,
            Field.prm_type.value: bool,
        },
        {
            Field.prm_name.value: Field.file_1_hide_unnamed_columns.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: False,
            Field.prm_type.value: bool,
        },
        {
            Field.prm_name.value: Field.file_2_hide_unnamed_columns.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: False,
            Field.prm_type.value: bool,
        },
        {
            Field.prm_name.value: Field.file_1_2_hide_not_modified_rows.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: False,
            Field.prm_type.value: bool,
        },
        {
            Field.prm_name.value: Field.file_1_2_output_path.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: "./",
            Field.prm_type.value: str,
            Field.prm_should_be_strip.value: True,
            Field.prm_can_have_special_char.value: False
        },
        {
            Field.prm_name.value: Field.file_1_2_output_name.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: "./",
            Field.prm_type.value: str,
            Field.prm_should_be_strip.value: True,
            Field.prm_can_have_special_char.value: False
        },

        {
            Field.prm_name.value: Field.file_1_encoding.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: None,
            Field.prm_type.value: str,
            Field.prm_should_be_strip.value: True,
            Field.prm_can_have_special_char.value: False
        },
        {
            Field.prm_name.value: Field.file_2_encoding.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: None,
            Field.prm_type.value: str,
            Field.prm_should_be_strip.value: True,
            Field.prm_can_have_special_char.value: False
        },

        {
            Field.prm_name.value: Field.file_1_delimiter.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: ',',
            Field.prm_type.value: str,
            Field.prm_should_be_strip.value: False,
            Field.prm_can_have_special_char.value: True
        },
        {
            Field.prm_name.value: Field.file_2_delimiter.value,
            Field.prm_required.value: False,
            Field.prm_default_value.value: ',',
            Field.prm_type.value: str,
            Field.prm_should_be_strip.value: False,
            Field.prm_can_have_special_char.value: True
        },
    ]
