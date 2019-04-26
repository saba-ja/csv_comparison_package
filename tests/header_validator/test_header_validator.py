import os
import pytest
from csv_comparison_package import header_validator
from csv_comparison_package import Compare
from csv_comparison_package import AppErrorHandler
import tests.mock_header_validator_dict as mock_header_dict


class TestHeaderValidator:
    @pytest.fixture
    def comparable(self, request):
        f_path, f_name = os.path.split(os.path.abspath(__file__))
        mock_data_dir = os.path.join(f_path, os.pardir, 'mock_data')
        comparable_obj = Compare()
        for name in request.param:
            setattr(comparable_obj, name, request.param[name])

        if "file_name" in request.param:
            comparable_obj.file_name = os.path.join(mock_data_dir, f'{request.param["file_name"]}')

        return comparable_obj

    # ###########################
    # header_validator.check_for_negative_header_row
    # ###########################

    @pytest.mark.parametrize('comparable', [{'header_row': 1}, {'header_row': 2}],
                             indirect=['comparable'])
    def test_when_header_row_is_valid(self, comparable):
        assert header_validator.check_for_negative_header_row(comparable) is None

    @pytest.mark.parametrize('comparable', [{'header_row': 0}, {'header_row': -1}],
                             indirect=['comparable'])
    def test_when_header_row_is_invalid(self, comparable):
        with pytest.raises(AppErrorHandler):
            header_validator.check_for_negative_header_row(comparable)

    # ###########################
    # header_validator.check_for_header_row_location
    # ###########################
    @pytest.mark.parametrize('comparable', [mock_header_dict.header_row_out_of_range],
                             indirect=['comparable'])
    def test_when_header_row_is_more_than_number_of_rows_in_the_file(self, comparable):
        with pytest.raises(AppErrorHandler):
            header_validator.check_for_header_row_location(comparable)

    @pytest.mark.parametrize('comparable', [mock_header_dict.header_row_in_range],
                             indirect=['comparable'])
    def test_when_header_row_is_less_than_number_of_rows_in_the_file(self, comparable):
        assert header_validator.check_for_header_row_location(comparable) is None

    # ###########################
    # header_validator.set_original_header
    # ###########################

    @pytest.mark.parametrize('comparable, expected',
                             [mock_header_dict.good_file_and_expected_header_1,
                              mock_header_dict.good_file_and_expected_header_2,
                              mock_header_dict.good_file_and_expected_header_3
                              ],
                             indirect=['comparable'])
    def test_set_header_row_when_file_has_right_format_and_header_row_number(self, comparable,
                                                                             expected):
        header_validator.set_original_header(comparable)
        assert expected == comparable.original_header

    @pytest.mark.parametrize('comparable',
                             [mock_header_dict.failing_case_for_setting_original_header,
                              ],
                             indirect=['comparable'])
    def test_set_header_row_when_header_row_is_out_of_range(self, comparable):
        with pytest.raises(AppErrorHandler):
            header_validator.set_original_header(comparable)

    # ###########################
    # header_validator.set_header
    # ###########################

    @pytest.mark.parametrize('comparable, expected',
                             [mock_header_dict.original_header_parameter_and_expected_header],
                             indirect=['comparable'])
    def test_set_header(self, comparable, expected):
        header_validator.set_header(comparable)
        assert expected == comparable.header

    @pytest.mark.parametrize('comparable, expected',
                             [({'original_header': []},
                               []
                               )], indirect=['comparable'])
    def test_set_header_for_empty_original_header(self, comparable, expected):
        header_validator.set_header(comparable)
        assert expected == comparable.header

    # ###########################
    # header_validator.strip_header
    # ###########################
    @pytest.mark.parametrize('comparable, expected',
                             [mock_header_dict.header_and_expected_strip_result],
                             indirect=['comparable'])
    def test_strip_header(self, comparable, expected):
        header_validator.strip_header(comparable)
        assert expected == comparable.header

    # ###########################
    # header_validator.check_for_index_column
    # ###########################

    @pytest.mark.parametrize('comparable', [
        mock_header_dict.index_column_exist_in_header_1,
        mock_header_dict.index_column_exist_in_header_2,
    ], indirect=['comparable'])
    def test_check_for_index_column_when_it_exists_at_the_given_location(self, comparable):
        assert header_validator.check_for_index_column(comparable) is None

    @pytest.mark.parametrize('comparable', [
        mock_header_dict.index_column_does_not_exist_in_header_1,
        mock_header_dict.index_column_does_not_exist_in_header_2,
    ], indirect=['comparable'])
    def test_check_for_index_column_when_it_does_not_exists_at_the_given_location(self, comparable):
        with pytest.raises(AppErrorHandler):
            header_validator.check_for_index_column(comparable)

    # ###########################
    # header_validator.check_for_map_column
    # ###########################
    @pytest.mark.parametrize('comparable', [
        mock_header_dict.mapped_column_exist_in_header_1,
        mock_header_dict.mapped_column_exist_in_header_2,
    ], indirect=['comparable'])
    def test_check_for_map_column_when_they_exist(self, comparable):
        Compare.map_columns = [(
            {'column_name': 'first_name_1', 'column_location': 2},
            {'column_name': 'first_name_2', 'column_location': 2}
        )]
        assert header_validator.check_for_map_column(comparable) is None

    @pytest.mark.parametrize('comparable', [
        mock_header_dict.mapped_column_does_not_exist_in_header_1,
        mock_header_dict.mapped_column_does_not_exist_in_header_2,
    ], indirect=['comparable'])
    def test_check_for_map_column_when_they_do_not_exist(self, comparable):
        Compare.map_columns = [(
            {'column_name': 'first_name_1', 'column_location': 3},
            {'column_name': 'first_name_2', 'column_location': 4}
        )]
        with pytest.raises(AppErrorHandler):
            header_validator.check_for_map_column(comparable)

    def test_check_for_map_column_when_it_is_empty(self):
        Compare.map_columns = []
        comparable = Compare()
        assert header_validator.check_for_map_column(comparable) is None

    @pytest.mark.parametrize('comparable', [
        mock_header_dict.mapped_column_when_conflict_with_index
    ], indirect=['comparable'])
    def test_check_for_map_column_when_they_conflict_with_index(self, comparable):
        Compare.map_columns = [(
            {'column_name': 'id', 'column_location': 1},
            {'column_name': 'id', 'column_location': 1}
        )]
        with pytest.raises(AppErrorHandler):
            header_validator.check_for_map_column(comparable)

    ###########################
    # header_validator.format_map_column
    ###########################
    @pytest.mark.parametrize('comparable, expected', [
        mock_header_dict.header_for_map_column_and_expected_result_file_1,
        mock_header_dict.header_for_map_column_and_expected_result_file_2
    ], indirect=['comparable'])
    def test_format_map_column(self, comparable, expected):
        Compare.map_columns = mock_header_dict.map_column_different_names
        header_validator.format_map_column(comparable)
        header_index = header_validator.get_header_index(comparable, expected)
        is_passing = all([header_validator.is_header(comparable, expected),
                          comparable.header[header_index]["column_type"] == expected[
                              "column_type"]])
        assert is_passing

    @pytest.mark.parametrize('comparable, expected', [
        mock_header_dict.header_for_map_column_and_expected_result_file_1_identical_names,
        mock_header_dict.header_for_map_column_and_expected_result_file_2_identical_names
    ], indirect=['comparable'])
    def test_format_map_column_when_columns_have_identical_names(self, comparable, expected):
        Compare.map_columns = mock_header_dict.map_column_identical_names
        header_validator.format_map_column(comparable)
        header_index = header_validator.get_header_index(comparable, expected)
        assert \
            header_validator.is_header(comparable, expected) and \
            comparable.header[header_index]["column_type"] == expected["column_type"]

    @pytest.mark.parametrize('comparable, expected', [
        mock_header_dict.header_that_are_not_in_map_column_and_expected_result
    ], indirect=['comparable'])
    def test_format_map_column_when_columns_are_not_in_header(self, comparable, expected):
        Compare.map_columns = mock_header_dict.map_column_identical_names
        header_validator.format_map_column(comparable)
        header_index = header_validator.get_header_index(comparable, expected)
        assert \
            header_validator.is_header(comparable, expected) and \
            comparable.header[header_index]["column_type"] == expected["column_type"]

    @pytest.mark.parametrize('comparable, expected', [
        mock_header_dict.format_map_function_mapped_column_when_conflict_with_index
    ], indirect=['comparable'])
    def test_format_map_column_when_conflict_with_index(self, comparable, expected):
        Compare.map_columns = Compare.map_columns = [(
            {'column_name': 'id', 'column_location': 1},
            {'column_name': 'id', 'column_location': 1}
        )]
        header_validator.format_map_column(comparable)
        for val1, val2 in zip(expected, comparable.header):
            assert val1["column_name"] == val2["column_name"]
            assert val1["column_location"] == val2["column_location"]
            assert val1["column_type"] == val2["column_type"]

    # ###########################
    # header_validator.format_unnamed_column
    # ###########################
    @pytest.mark.parametrize('comparable, expected', [
        mock_header_dict.header_with_unnamed_columns_and_expected_result
    ], indirect=['comparable'])
    def test_format_unnamed_column(self, comparable, expected):
        header_validator.format_unnamed_column(comparable)
        for val1, val2 in zip(expected, comparable.header):
            assert val1["column_name"] == val2["column_name"]
            assert val1["column_location"] == val2["column_location"]
            assert val1["column_type"] == val2["column_type"]

    @pytest.mark.parametrize('comparable, expected', [
        mock_header_dict.header_with_named_columns_and_expected_result
    ], indirect=['comparable'])
    def test_format_unnamed_column_function_for_header_without_empty_column(self, comparable,
                                                                            expected):
        header_validator.format_unnamed_column(comparable)
        for val1, val2 in zip(expected, comparable.header):
            assert val1["column_name"] == val2["column_name"]
            assert val1["column_location"] == val2["column_location"]
            assert val1["column_type"] == val2["column_type"]

    # ###########################
    # header_validator.format_duplicate_column
    # ###########################
    @pytest.mark.parametrize('comparable, expected',
                             [mock_header_dict.header_with_duplicate_columns_and_expected_result],
                             indirect=['comparable'])
    def test_format_duplicate_column(self, comparable, expected):
        header_validator.format_duplicate_column(comparable)
        for val1, val2 in zip(expected, comparable.header):
            assert val1["column_name"] == val2["column_name"]
            assert val1["column_location"] == val2["column_location"]
            assert val1["column_type"] == val2["column_type"]

    @pytest.mark.parametrize('comparable, expected',
                             [
                                 mock_header_dict.header_with_mixed_dup_none_dup_col_and_expected_result],
                             indirect=['comparable'])
    def test_format_duplicate_column_with_mixed_values(self, comparable, expected):
        header_validator.format_duplicate_column(comparable)
        for val1, val2 in zip(expected, comparable.header):
            assert val1["column_name"] == val2["column_name"]
            assert val1["column_location"] == val2["column_location"]
            assert val1["column_type"] == val2["column_type"]

    # ###########################
    # header_validator.is_index
    # ###########################
    @pytest.mark.parametrize('comparable',
                             [mock_header_dict.looking_for_is_index_function_when_index_exist],
                             indirect=['comparable'])
    def test_is_index_function_when_exist(self, comparable):
        assert header_validator.is_index(comparable, {"column_name": "id", "column_location": 1})

    @pytest.mark.parametrize('comparable',
                             [
                                 mock_header_dict.looking_for_is_index_function_when_index_does_not_exist],
                             indirect=['comparable'])
    def test_is_index_function_when_does_not_exist(self, comparable):
        assert not header_validator.is_index(comparable,
                                             {"column_name": "id", "column_location": 1})

    # ###########################
    # header_validator.is_mapped
    # ###########################
    @pytest.mark.parametrize('comparable',
                             [mock_header_dict.looking_for_mapped_column_when_exist_1,
                              mock_header_dict.looking_for_mapped_column_when_exist_2],
                             indirect=['comparable'])
    def test_is_index_function(self, comparable):
        Compare.map_columns = [(
            {'column_name': 'id', 'column_location': 1},
            {'column_name': 'id', 'column_location': 1}
        )]

        assert header_validator.is_mapped(comparable, {"column_name": "id", "column_location": 1})

    @pytest.mark.parametrize('comparable',
                             [mock_header_dict.looking_for_mapped_column_when_exist_1,
                              mock_header_dict.looking_for_mapped_column_when_exist_2],
                             indirect=['comparable'])
    def test_is_index_function(self, comparable):
        Compare.map_columns = [(
            {'column_name': 'id', 'column_location': 2},
            {'column_name': 'id1', 'column_location': 1}
        )]

        assert not header_validator.is_mapped(comparable,
                                              {"column_name": "id", "column_location": 1})

    # ###########################
    # header_validator.get_header_index
    # ###########################
    @pytest.mark.parametrize('comparable', [mock_header_dict.header_for_get_header_index],
                             indirect=['comparable'])
    def test_get_header_index_when_header_exists(self, comparable):
        lookup = {'column_name': 'file_name', 'column_location': 3, 'column_type': ''}
        assert 0 == header_validator.get_header_index(comparable, lookup)

    @pytest.mark.parametrize('comparable', [mock_header_dict.header_for_get_header_index],
                             indirect=['comparable'])
    def test_get_header_index_when_header_does_not_exists(self, comparable):
        lookup = {'column_name': 'file_name_not_there', 'column_location': 3, 'column_type': ''}
        assert header_validator.get_header_index(comparable, lookup) is None

    ##########################
    # header_validator.format_disjunctive_column
    ##########################

    def test_format_disjunctive_column_when_exist(self):
        comparable_1 = Compare()
        comparable_2 = Compare()

        for key, value in mock_header_dict.header_for_disjunctive_check_and_not_index_file_1.items():
            setattr(comparable_1, key, value)
        for key, value in mock_header_dict.header_for_disjunctive_check_and_not_index_file_2.items():
            setattr(comparable_2, key, value)

        header_validator.format_disjunctive_column(comparable_1, comparable_2)
        expected = [{'column_name': 'file_name_address_1@notFound.4',
                     'column_location': 4, 'column_type': 'disjunctive'}]

        for val1, val2 in zip(expected, comparable_1.header):
            assert val1["column_name"] == val2["column_name"]
            assert val1["column_location"] == val2["column_location"]
            assert val1["column_type"] == val2["column_type"]

    def test_format_disjunctive_column_when_column_is_index(self):
        comparable_1 = Compare()
        comparable_2 = Compare()

        for key, value in mock_header_dict.header_for_disjunctive_check_and_is_index_file_1.items():
            setattr(comparable_1, key, value)
        for key, value in mock_header_dict.header_for_disjunctive_check_and_not_index_file_2.items():
            setattr(comparable_2, key, value)

        header_validator.format_disjunctive_column(comparable_1, comparable_2)
        expected = [{'column_name': 'id',
                     'column_location': 1, 'column_type': ''}]

        for val1, val2 in zip(expected, comparable_1.header):
            assert val1["column_name"] == val2["column_name"]
            assert val1["column_location"] == val2["column_location"]
            assert val1["column_type"] == val2["column_type"]

    def test_format_disjunctive_column_when_column_column_exists_in_both(self):
        comparable_1 = Compare()
        comparable_2 = Compare()

        for key, value in mock_header_dict.header_for_disjunctive_check_and_column_is_in_other_file_1.items():
            setattr(comparable_1, key, value)
        for key, value in mock_header_dict.header_for_disjunctive_check_and_column_is_in_other_file_2.items():
            setattr(comparable_2, key, value)

        header_validator.format_disjunctive_column(comparable_1, comparable_2)
        expected = [{'column_name': 'file_name',
                     'column_location': 3, 'column_type': ''}]

        for val1, val2 in zip(expected, comparable_1.header):
            assert val1["column_name"] == val2["column_name"]
            assert val1["column_location"] == val2["column_location"]
            assert val1["column_type"] == val2["column_type"]

    ###########################
    # header_validator.format_not_checked_column
    ###########################

    @pytest.mark.parametrize('comparable, expected',
                             [mock_header_dict.header_for_not_checked_columns],
                             indirect=['comparable'])
    def test_for_format_not_checked_column(self, comparable, expected):
        Compare.map_columns = [(
            {'column_name': 'id', 'column_location': 3},
            {'column_name': 'id', 'column_location': 4}
        )]
        header_validator.format_not_for_checked_column(comparable)
        for val1, val2 in zip(expected, comparable.header):
            assert val1["column_name"] == val2["column_name"]
            assert val1["column_location"] == val2["column_location"]
            assert val1["column_type"] == val2["column_type"]

    @pytest.mark.parametrize('comparable, expected', [
        mock_header_dict.header_for_not_checked_columns_when_mapped_column_is_empty],
                             indirect=['comparable'])
    def test_for_format_not_checked_column_when_mapped_column_is_empty(self, comparable, expected):
        Compare.map_columns = []
        header_validator.format_not_for_checked_column(comparable)
        for val1, val2 in zip(expected, comparable.header):
            assert val1["column_name"] == val2["column_name"]
            assert val1["column_location"] == val2["column_location"]
            assert val1["column_type"] == val2["column_type"]

    @pytest.mark.parametrize('comparable, expected', [
        mock_header_dict.header_for_not_checked_columns_when_column_type_is_not_empty],
                             indirect=['comparable'])
    def test_for_format_not_checked_column_when_column_type_is_not_empty(self, comparable,
                                                                         expected):
        Compare.map_columns = [(
            {'column_name': 'id', 'column_location': 3},
            {'column_name': 'id', 'column_location': 4}
        )]
        header_validator.format_not_for_checked_column(comparable)
        for val1, val2 in zip(expected, comparable.header):
            assert val1["column_name"] == val2["column_name"]
            assert val1["column_location"] == val2["column_location"]
            assert val1["column_type"] == val2["column_type"]

    ###########################
    # header_validator.check_for_index_name_existence
    ###########################
    def test_check_for_index_name_existence(self):
        comparable = Compare()
        comparable.index_column_name = [{"column_name": "id"}]
        comparable.header = [{"column_name": "id", "column_location": 1}]
        assert header_validator.check_for_index_name_existence(comparable) is None

    def test_check_for_index_name_existence_when_index_does_not_exist(self):
        comparable = Compare()
        comparable.index_column_name = [{"column_name": "id"}]
        comparable.header = [{"column_name": "id1", "column_location": 1}]
        with pytest.raises(AppErrorHandler):
            header_validator.check_for_index_name_existence(comparable)

    ###########################
    # header_validator.set_index_column_location
    ###########################
    def test_set_index_column_location(self):
        comparable = Compare()
        comparable.index_column_name = [{"column_name": "id"}]
        comparable.header = [{"column_name": "id", "column_location": 1}]
        assert header_validator.set_index_column_location(comparable) is None

    def test_set_index_column_location_when_multiple_index_exist(self):
        comparable = Compare()
        comparable.index_column_name = [{"column_name": "id"}]
        comparable.header = [{"column_name": "id", "column_location": 1},
                             {"column_name": "id", "column_location": 2}]
        with pytest.raises(AppErrorHandler):
            header_validator.set_index_column_location(comparable)

    def test_set_index_column_location_when_index_does_not_exist(self):
        comparable = Compare()
        comparable.index_column_name = [{"column_name": "id"}]
        comparable.header = [{"column_name": "id1", "column_location": 1}]
        with pytest.raises(AppErrorHandler):
            header_validator.set_index_column_location(comparable)

    ###########################
    # header_validator.check_for_map_name_existence
    ###########################
    def test_check_for_map_column_name_existence(self):
        Compare.map_columns = [(
            {"column_name": "first_name"},
            {"column_name": "first_name"},
        )]
        comparable = Compare(order=0)
        comparable.header = [{"column_name": "first_name", "column_location": 2}]
        assert header_validator.check_for_map_column_existence(comparable) is None

    def test_check_for_map_column_name_existence_when_map_name_does_not_exist(self):
        Compare.map_columns = [(
            {"column_name": "first_name1"},
            {"column_name": "first_name"},
        )]
        comparable = Compare(order=0)
        comparable.header = [{"column_name": "first_name", "column_location": 2}]
        with pytest.raises(AppErrorHandler):
            header_validator.check_for_map_column_existence(comparable)

    ###########################
    # header_validator.set_map_column_location
    ###########################
    def test_set_map_column_location(self):
        Compare.map_columns = [
            (
                {"column_name": "first_name"},
                {"column_name": "first_name"},
            ),
            (
                {"column_name": "last_name"},
                {"column_name": "last_name"},
            )
        ]
        comparable = Compare(order=0)
        comparable.header = [{"column_name": "first_name", "column_location": 2},
                             {"column_name": "last_name", "column_location": 3}]
        header_validator.set_map_column_location(comparable)
        assert comparable.header[0] == Compare.map_columns[0][0]
        assert comparable.header[1] == Compare.map_columns[1][0]

    def test_set_map_column_location_when_not_exist(self):
        Compare.map_columns = [
            (
                {"column_name": "first_name"},
                {"column_name": "first_name"},
            ),
            (
                {"column_name": "last_name"},
                {"column_name": "last_name"},
            )
        ]
        comparable = Compare(order=0)
        comparable.header = [{"column_name": "first_name1", "column_location": 2},
                             {"column_name": "last_name1", "column_location": 3}]
        with pytest.raises(AppErrorHandler):
            header_validator.set_map_column_location(comparable)

    ###########################
    # header_validator.set_regular_column_number
    ###########################
    def test_set_regular_column_number(self):
        comparable = Compare(order=1)
        comparable.header = [
            {"column_name": "id", "column_location": 1, "column_type": ""},
            {"column_name": "first_name", "column_location": 2, "column_type": ""},
            {"column_name": "last_name", "column_location": 3, "column_type": "duplicate"},
            {"column_name": "last_name", "column_location": 4, "column_type": "duplicate"},
            {"column_name": "requirement", "column_location": 5, "column_type": "mapped"},
            {"column_name": "alternate_name", "column_location": 6, "column_type": ""}]
        comparable.index_column_name = [
            {"column_name": "id", "column_location": 1, "column_type": ""}]

        header_validator.set_regular_column_number(comparable)
        assert 2 == comparable.number_of_regular_columns

    ###########################
    # header_validator.set_amp_column_number
    ###########################
    def test_set_map_column_number(self):
        comparable = Compare(order=1)
        comparable.header = [
            {"column_name": "id", "column_location": 1, "column_type": ""},
            {"column_name": "first_name", "column_location": 2, "column_type": "mapped"},
            {"column_name": "last_name", "column_location": 3, "column_type": "duplicate"},
            {"column_name": "last_name", "column_location": 4, "column_type": "duplicate"},
            {"column_name": "requirement", "column_location": 5, "column_type": "mapped"},
            {"column_name": "alternate_name", "column_location": 6, "column_type": ""}]
        comparable.index_column_name = [
            {"column_name": "id", "column_location": 1, "column_type": ""}]

        header_validator.set_map_column_number(comparable)
        assert 2 == comparable.number_of_mapped_columns

    ###########################
    # header_validator.set_start_column
    ###########################
    def test_set_start_column(self):
        comparable_a = Compare(order=0)
        comparable_b = Compare(order=1)
        comparable_a.number_of_index_column = 1  # not supporting multi index
        comparable_a.number_of_unnamed_columns = 2
        comparable_a.number_of_duplicate_columns = 2
        comparable_a.number_of_disjunctive_columns = 2
        comparable_a.number_of_not_checked_columns = 2
        comparable_a.number_of_mapped_columns = 2
        comparable_a.number_of_regular_columns = 2
        header_validator.set_start_column(comparable_a, comparable_b)
        assert 14 == comparable_b.start_column
        assert 1 == comparable_a.start_column

    ###########################
    # header_validator.set_start_end_index_column
    ###########################
    def test_set_start_end_index_column(self):
        comparable = Compare(order=0)
        comparable.start_column = 1
        comparable.number_of_index_column = 1
        header_validator.set_start_end_index_column(comparable)
        assert 1 == comparable.index_column_start
        assert 1 == comparable.index_column_end

    ###########################
    # header_validator.set_start_end_checked_column
    ###########################
    def test_set_start_end_checked_column(self):
        comparable = Compare(order=0)

        comparable.start_column = 1
        comparable.number_of_index_column = 1

        comparable.number_of_mapped_columns = 2
        comparable.number_of_regular_columns = 2

        header_validator.set_start_end_checked_column(comparable)
        assert 2 == comparable.checked_column_start
        assert 5 == comparable.checked_column_end

    def test_set_start_end_checked_column_2(self):
        comparable = Compare(order=1)

        comparable.start_column = 14
        comparable.number_of_index_column = 1

        comparable.number_of_mapped_columns = 2
        comparable.number_of_regular_columns = 2

        header_validator.set_start_end_checked_column(comparable)
        assert 15 == comparable.checked_column_start
        assert 18 == comparable.checked_column_end

    ###########################
    # header_validator.set_start_end_not_checked_column
    ###########################
    def test_start_end_not_checked_column(self):
        comparable = Compare(order=0)
        comparable.start_column = 1
        comparable.number_of_index_column = 1

        comparable.number_of_mapped_columns = 2
        comparable.number_of_regular_columns = 2
        comparable.number_of_not_checked_columns = 2

        header_validator.set_start_end_not_checked_column(comparable)
        assert 6 == comparable.not_checked_column_start
        assert 7 == comparable.not_checked_column_end

    def test_start_end_not_checked_column_2(self):
        comparable = Compare(order=1)
        comparable.start_column = 14
        comparable.number_of_index_column = 1

        comparable.number_of_mapped_columns = 2
        comparable.number_of_regular_columns = 2
        comparable.number_of_not_checked_columns = 2

        header_validator.set_start_end_not_checked_column(comparable)
        assert 19 == comparable.not_checked_column_start
        assert 20 == comparable.not_checked_column_end

    ###########################
    # header_validator.set_start_end_disjunctive_column
    ###########################
    def test_set_start_end_disjunctive_column(self):
        comparable = Compare(order=0)
        comparable.start_column = 1
        comparable.number_of_index_column = 1

        comparable.number_of_mapped_columns = 2
        comparable.number_of_regular_columns = 2
        comparable.number_of_not_checked_columns = 2
        comparable.number_of_disjunctive_columns = 2
        header_validator.set_start_end_disjunctive_column(comparable)
        assert 8 == comparable.disjunctive_column_start
        assert 9 == comparable.disjunctive_column_end

    ###########################
    # header_validator.set_start_end_duplicate_column
    ###########################
    def test_set_start_end_duplicate_column(self):
        comparable = Compare(order=0)
        comparable.start_column = 1
        comparable.number_of_index_column = 1

        comparable.number_of_mapped_columns = 2
        comparable.number_of_regular_columns = 2
        comparable.number_of_not_checked_columns = 2
        comparable.number_of_disjunctive_columns = 2
        comparable.number_of_duplicate_columns = 2
        header_validator.set_start_end_duplicate_column(comparable)
        assert 10 == comparable.duplicate_column_start
        assert 11 == comparable.duplicate_column_end

    ###########################
    # header_validator.set_start_end_unnamed_column
    ###########################
    def test_set_start_end_unnamed_column(self):
        comparable = Compare(order=0)
        comparable.start_column = 1
        comparable.number_of_index_column = 1

        comparable.number_of_mapped_columns = 2
        comparable.number_of_regular_columns = 2
        comparable.number_of_not_checked_columns = 2
        comparable.number_of_disjunctive_columns = 2
        comparable.number_of_duplicate_columns = 2
        comparable.number_of_unnamed_columns = 2
        header_validator.set_start_end_unnamed_column(comparable)
        assert 12 == comparable.unnamed_column_start
        assert 13 == comparable.unnamed_column_end

    def test_set_start_end_unnamed_column_2(self):
        comparable = Compare(order=0)
        comparable.start_column = 14
        comparable.number_of_index_column = 1

        comparable.number_of_mapped_columns = 2
        comparable.number_of_regular_columns = 2
        comparable.number_of_not_checked_columns = 2
        comparable.number_of_disjunctive_columns = 2
        comparable.number_of_duplicate_columns = 2
        comparable.number_of_unnamed_columns = 2
        header_validator.set_start_end_unnamed_column(comparable)
        assert 25 == comparable.unnamed_column_start
        assert 26 == comparable.unnamed_column_end

    ###########################
    # header_validator.format_index_column
    ############################

    def test_format_index_column(self):
        comparable = Compare(order=0)
        comparable.header = [
            {"column_name": "id", "column_location": 1, "column_type": ""},
            {"column_name": "first_name", "column_location": 2, "column_type": "mapped"},
            {"column_name": "last_name", "column_location": 3, "column_type": "duplicate"},
            {"column_name": "last_name", "column_location": 4, "column_type": "duplicate"},
            {"column_name": "requirement", "column_location": 5, "column_type": "mapped"},
            {"column_name": "alternate_name", "column_location": 6, "column_type": ""}]
        comparable.index_column_name = [
            {"column_name": "id", "column_location": 1, "column_type": ""}]

        header_validator.format_index_column(comparable)
        assert comparable.header[0]['column_type'] == "index"
