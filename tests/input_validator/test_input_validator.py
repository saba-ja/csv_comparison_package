import os
import pytest
import unittest.mock

from csv_comparison_package import Setting
from csv_comparison_package import Compare
from csv_comparison_package import input_validator

from csv_comparison_package.error_handler import AppErrorHandler
import tests.mock_input_validator_dict as mock_input_dict


class TestInputValidator:
    f_path, f_name = os.path.split(os.path.abspath(__file__))
    MOCK_DATA_DIR = os.path.join(f_path, os.pardir, 'mock_data')

    ####################################################
    # input_validator.check_for_type_dictionary
    ####################################################
    @pytest.mark.parametrize('mock_dictionary_object', [
        mock_input_dict.parameter_with_type_string,
        mock_input_dict.parameter_with_type_integer,
        mock_input_dict.parameter_with_type_tuple,
        mock_input_dict.parameter_with_type_set,
    ])
    def test_when_user_submits_parameter_that_is_not_of_type_dictionary(self,
                                                                        mock_dictionary_object):
        comparator_obj = Setting(mock_dictionary_object)
        with pytest.raises(AppErrorHandler):
            input_validator.check_for_type_dictionary(comparator_obj)

    def test_when_user_submits_parameter_that_is_a_dictionary(self):
        comparator_obj = Setting(mock_input_dict.parameter_with_type_dict)
        assert input_validator.check_for_type_dictionary(comparator_obj) is None

    ####################################################
    # input_validator.check_for_empty_dictionary
    ####################################################

    def test_when_the_parameter_list_is_empty(self):
        comparator_obj = Setting(mock_input_dict.parameter_with_no_value)
        with pytest.raises(AppErrorHandler):
            input_validator.check_for_empty_dictionary(comparator_obj)

    def test_when_the_parameter_list_is_not_empty(self):
        comparator_obj = Setting(mock_input_dict.parameter_with_some_key_value_pair)
        assert input_validator.check_for_empty_dictionary(comparator_obj) is None

    ####################################################
    # input_validator.check_for_key_to_be_string_type
    ####################################################

    @pytest.mark.parametrize('mock_dictionary_object', [
        mock_input_dict.parameter_with_integer_in_the_key,
        mock_input_dict.parameter_with_function_in_key,
    ])
    def test_parameter_keys_to_be_string_while_user_has_submitted_wrong_key_type(self,
                                                                                 mock_dictionary_object):
        comparator_obj = Setting(mock_dictionary_object)
        with pytest.raises(AppErrorHandler):
            input_validator.check_for_key_to_be_string_type(comparator_obj)

    @pytest.mark.parametrize('mock_dictionary_object', [
        mock_input_dict.parameter_with_string_type_key,
        mock_input_dict.parameter_with_blank_in_key
    ])
    def test_parameter_keys_to_be_string_while_user_has_submitted_right_key_type(self,
                                                                                 mock_dictionary_object):
        comparator_obj = Setting(mock_dictionary_object)
        assert input_validator.check_for_key_to_be_string_type(comparator_obj) is None

    ####################################################
    # input_validator.check_for_required_key
    ####################################################

    def test_when_the_file_name_parameter_key_is_missing(self):
        comparator_obj = Setting(mock_input_dict.parameter_with_wrong_file_name_key)
        with pytest.raises(AppErrorHandler):
            input_validator.check_for_required_key(comparator_obj)

    def test_when_required_parameter_key_is_missing(self):
        comparator_obj = Setting(mock_input_dict.parameter_with_missing_required_key)
        with pytest.raises(AppErrorHandler):
            input_validator.check_for_required_key(comparator_obj)

    def test_when_the_file_has_all_the_required_keys(self):
        comparator_obj = Setting(mock_input_dict.parameter_with_all_required_key)
        assert input_validator.check_for_required_key(comparator_obj) is None

    ####################################################
    # input_validator.check_for_type_string
    ####################################################
    @pytest.mark.parametrize('mock_dictionary_object', [
        mock_input_dict.parameter_with_required_string_value_but_submitted_integer_value_type,
        mock_input_dict.parameter_with_required_string_value_but_submitted_function_value_type,
        mock_input_dict.parameter_with_required_string_value_but_submitted_list_value_type,
        mock_input_dict.parameter_with_required_string_value_but_submitted_dict_value_type,
        mock_input_dict.parameter_with_not_required_and_type_string_but_int_type_submission
    ])
    def test_to_check_any_parameters_of_type_string_to_have_value_of_string_type_while_user_submitted_other_types(
            self, mock_dictionary_object):
        comparator_obj = Setting(mock_dictionary_object)
        with pytest.raises(AppErrorHandler):
            input_validator.check_for_type_string(comparator_obj)

    @pytest.mark.parametrize('mock_dictionary_object', [
        mock_input_dict.parameter_with_blank_required_value,
        mock_input_dict.parameter_with_blank_space_required_value,
        mock_input_dict.parameter_with_special_character
    ])
    def test_to_check_any_parameters_of_type_string_to_have_value_of_string_type(self,
                                                                                 mock_dictionary_object):
        comparator_obj = Setting(mock_dictionary_object)
        assert input_validator.check_for_type_string(comparator_obj) is None

    ####################################################
    # input_validator.check_for_parameter_strip
    ####################################################
    @pytest.mark.parametrize('mock_dictionary_object, expected_result', [
        (mock_input_dict.parameter_with_blank_required_value_for_stripping_test,
         mock_input_dict.expected_parameter_with_blank_required_value_for_stripping_test),
        (mock_input_dict.parameter_with_blank_space_required_value_for_stripping_test,
         mock_input_dict.expected_parameter_with_blank_space_required_value_for_stripping_test),
        (mock_input_dict.parameter_with_special_character_for_stripping_test,
         mock_input_dict.expected_parameter_with_special_character_for_stripping_test)
    ])
    def test_strip_any_parameter_with_type_string_that_needs_to_be_stripped(
            self, mock_dictionary_object, expected_result):
        comparator_obj = Setting(mock_dictionary_object)
        input_validator.check_for_parameter_strip(comparator_obj)
        processed_result = comparator_obj.parameters

        assert expected_result == processed_result

    @pytest.mark.parametrize('mock_dictionary_object, expected_result', [
        (mock_input_dict.parameter_with_type_string_but_wrong_submitted_type,
         mock_input_dict.expected_parameter_with_type_string_but_wrong_submitted_type)
    ])
    def test_to_check_if_none_string_types_are_escaped_for_any_parameter_with_string_type_and_requiring_stripping(
            self,
            mock_dictionary_object,
            expected_result):
        comparator_obj = Setting(mock_dictionary_object)
        input_validator.check_for_parameter_strip(comparator_obj)
        processed_result = comparator_obj.parameters
        assert expected_result == processed_result

    ####################################################
    # input_validator.check_for_special_character
    ####################################################
    @pytest.mark.parametrize('mock_dictionary_object', [
        mock_input_dict.parameter_with_forbidden_character,
        mock_input_dict.parameter_with_forbidden_character_but_not_required_key,
    ])
    def test_exception_raise_when_special_characters_are_in_parameter_that_can_not_have_any_special_char(
            self,
            mock_dictionary_object):
        comparator_obj = Setting(mock_dictionary_object)
        with pytest.raises(AppErrorHandler):
            input_validator.check_for_special_character(comparator_obj)

    @pytest.mark.parametrize('mock_dictionary_object', [
        mock_input_dict.parameter_with_no_forbidden_character
    ])
    def test_should_not_raise_error_if_parameter_can_have_special_character(self,
                                                                            mock_dictionary_object):
        comparator_obj = Setting(mock_dictionary_object)
        assert input_validator.check_for_special_character(comparator_obj) is None

    @pytest.mark.parametrize('mock_dictionary_object', [
        mock_input_dict.parameter_with_no_forbidden_character_but_not_string_type
    ])
    def test_should_not_raise_error_if_submitted_parameter_does_not_have_string_value(self,
                                                                                      mock_dictionary_object):
        comparator_obj = Setting(mock_dictionary_object)
        assert input_validator.check_for_special_character(comparator_obj) is None

    ####################################################
    # input_validator.check_for_empty_value
    ####################################################
    @pytest.mark.parametrize('mock_dictionary_object', [
        mock_input_dict.parameter_with_blank_required_value
    ])
    def test_when_required_parameter_value_is_empty(self, mock_dictionary_object):
        comparator_obj = Setting(mock_dictionary_object)

        with pytest.raises(AppErrorHandler):
            input_validator.check_for_empty_value(comparator_obj)

    @pytest.mark.parametrize('mock_dictionary_object', [
        mock_input_dict.parameter_with_blank_but_not_required_value,
        mock_input_dict.parameter_with_all_required_key
    ])
    def test_should_not_raise_error_if_key_is_not_required_but_value_is_empty(self,
                                                                              mock_dictionary_object):
        comparator_obj = Setting(mock_dictionary_object)
        assert input_validator.check_for_empty_value(comparator_obj) is None

    ####################################################
    # input_validator.check_for_default_schema
    ####################################################

    @pytest.mark.parametrize('mock_dictionary_object', [
        mock_input_dict.parameter_with_non_existing_keys,
        mock_input_dict.parameter_with_both_existing_and_non_existing_keys
    ])
    def test_check_exception_raise_when_user_submits_a_key_that_does_not_exist_in_default_schema(
            self,
            mock_dictionary_object):
        comparator_obj = Setting(mock_dictionary_object)
        with pytest.raises(AppErrorHandler):
            input_validator.check_for_default_schema(comparator_obj)

    def test_exception_raise_when_user_submits_keys_that_do_exist_in_default_schema(self):
        comparator_obj = Setting(mock_input_dict.parameter_with_existing_keys)
        assert input_validator.check_for_default_schema(comparator_obj) is None

    ####################################################
    # input_validator.check_for_parameter_type
    ####################################################
    @pytest.mark.parametrize('mock_dictionary_object', [
        mock_input_dict.parameter_is_string_but_integer_is_submitted,
        mock_input_dict.parameter_is_string_but_boolean_is_submitted,
        mock_input_dict.parameter_is_string_but_python_syntax_is_submitted,
    ])
    def test_when_user_submits_wrong_parameter_values_type(self, mock_dictionary_object):
        comparator_obj = Setting(mock_dictionary_object)

        with pytest.raises(AppErrorHandler):
            input_validator.check_for_parameter_type(comparator_obj)

    def test_when_submitted_parameter_key_is_not_available_for_checking_parameter_value_type(self):
        comparator_obj = Setting(mock_input_dict.parameter_with_existing_keys)
        assert input_validator.check_for_parameter_type(comparator_obj) is None

    def test_when_submitted_parameter_for_checking_value_type_has_empty_string(self):
        comparator_obj = Setting(mock_input_dict.parameter_is_boolean_but_empty_string_is_submitted)
        assert input_validator.check_for_parameter_type(comparator_obj) is None

    def test_when_parameter_is_of_type_list_but_boolean_has_been_submitted(self):
        comparator_obj = Setting(mock_input_dict.parameter_is_list_but_boolean_is_submitted)
        with pytest.raises(AppErrorHandler):
            input_validator.check_for_parameter_type(comparator_obj)

    def test_parameter_value_type_checking_when_everything_is_correct(self):
        comparator_obj = Setting(mock_input_dict.parameter_with_existing_keys_for_type_checking)
        assert input_validator.check_for_parameter_type(comparator_obj) is None

    # #####################################
    # TODO Need to write test for file_2_index_column_name, and  file_1_2_map_columns parameters
    # TODO Need to assign verified values to Comparison object
    # #####################################

    ####################################################
    # input_validator.check_for_input_file_existence
    ####################################################

    @unittest.mock.patch('os.path.isfile')
    def test_check_for_input_file_existence_when_file_does_not_exist(self, mock_isfile):
        comparator_obj = Compare()
        comparator_obj.file_name = mock_input_dict.parameter_for_input_file_existence["file_1_name"]
        mock_isfile.return_value = False
        with pytest.raises(AppErrorHandler):
            input_validator.check_for_input_file_existence(comparator_obj)
            mock_isfile.assert_called_once_with(f'os.path.isfile({comparator_obj})')

    @unittest.mock.patch('os.path.isfile')
    def test_check_for_input_file_existence_when_file_exist(self, mock_isfile):
        comparator_obj = Compare()
        comparator_obj.file_name = mock_input_dict.parameter_for_input_file_existence["file_1_name"]
        mock_isfile.return_value = True
        assert input_validator.check_for_input_file_existence(comparator_obj) is None

    ####################################################
    # input_validator.check_for_file_read_access
    ####################################################
    @unittest.mock.patch('os.access')
    def test_check_for_input_file_readability_when_file_is_not_readable(self, mock_os_access):
        comparator_obj = Compare()
        comparator_obj.file_name = mock_input_dict.parameter_for_input_file_existence["file_1_name"]
        mock_os_access.return_value = False
        with pytest.raises(AppErrorHandler):
            input_validator.check_for_file_read_access(comparator_obj)
            mock_os_access.assert_called_once_with(f'os.access({comparator_obj}, os.R_OK)')

    @unittest.mock.patch('os.access')
    def test_check_for_input_file_readability_when_file_is_readable(self, mock_isfile):
        comparator_obj = Compare()
        comparator_obj.file_name = mock_input_dict.parameter_for_input_file_existence["file_1_name"]
        mock_isfile.return_value = True
        assert input_validator.check_for_file_read_access(comparator_obj) is None

    ####################################################
    # input_validator.check_for_file_write_access
    ####################################################
    @unittest.mock.patch('os.access')
    def test_check_for_output_file_write_access_when_file_is_not_writeable(self, mock_os_access):
        comparator_obj = Compare()
        comparator_obj.file_name = mock_input_dict.parameter_for_input_file_existence["file_1_name"]
        mock_os_access.return_value = False
        with pytest.raises(AppErrorHandler):
            input_validator.check_for_file_write_access(comparator_obj)
            mock_os_access.assert_called_once_with(f'os.access({comparator_obj}, os.W_OK)')

    @unittest.mock.patch('os.access')
    def test_check_for_output_file_write_access_when_file_is_writeable(self, mock_isfile):
        comparator_obj = Compare()
        comparator_obj.file_name = mock_input_dict.parameter_for_input_file_existence["file_1_name"]
        mock_isfile.return_value = True
        assert input_validator.check_for_file_write_access(comparator_obj) is None

    # ####################################################
    # # input_validator.set_file_encoding
    # ####################################################
    MOCK_DATA = u'first_name,last_name,telephone\n1,2,3\n1,2,3\nt,y,u\no,p,t\n*,#,@\n'

    def create_mock_data_file_for_encoding_types(self, file_name):
        import codecs
        import pandas as pd
        encoding_name_path = os.path.join(self.MOCK_DATA_DIR, file_name)
        df = pd.read_csv(encoding_name_path, header=None)
        passing_encoding_names = list(df[0].values)

        data = self.MOCK_DATA

        for encoding_val in passing_encoding_names:
            mock_file_path = os.path.join(self.MOCK_DATA_DIR, f'{encoding_val}.csv')
            with codecs.open(mock_file_path, 'w', encoding=encoding_val) as f:
                f.write(data)
        return passing_encoding_names

    @pytest.mark.parametrize('file_name', [
        'empty_csv_file.csv',
    ])
    def test_get_file_encoding_when_file_is_empty(self, file_name):
        my_data_path = os.path.join(self.MOCK_DATA_DIR, file_name)
        comparator_obj = Compare()
        comparator_obj.file_name = my_data_path
        with pytest.raises(AppErrorHandler):
            assert input_validator.set_file_encoding(comparator_obj)

    @pytest.mark.parametrize('file_name, expected_encoding', [
        ('simple_csv_file_with_blank_space_in_header.csv', 'UTF-8-SIG'),
        ('large_mock_data_with_unix_lf_format_and_header.csv', 'ISO-8859-1'),
        ('large_mock_data_with_unix_lf_format_and_header_and_bom.csv', 'UTF-8-SIG'),
        ('large_mock_data_with_windows_crlf_format_and_header.csv', 'ascii'),
        ('large_mock_data_with_windows_crlf_format_and_header_and_bom.csv', 'UTF-8-SIG'),
        ('simple_csv_file.csv', 'UTF-8-SIG'),
        ('simple_csv_file_with_header_at_nth_different_row.csv', 'UTF-8-SIG'),
    ])
    def test_get_file_encoding(self, file_name, expected_encoding):
        my_data_path = os.path.join(self.MOCK_DATA_DIR, file_name)
        comparator_obj = Compare()
        comparator_obj.file_name = my_data_path
        input_validator.set_file_encoding(comparator_obj)
        assert comparator_obj.encoding == expected_encoding.lower()

    def test_get_file_encoding_for_most_of_the_cases(self):
        import codecs
        passing_encoding_names = self.create_mock_data_file_for_encoding_types("encoding_names.csv")
        rows = self.MOCK_DATA.split('\n')
        comparator_obj = Compare()

        for encoding_val in passing_encoding_names:
            mock_file_path = os.path.join(self.MOCK_DATA_DIR, f'{encoding_val}.csv')
            comparator_obj.file_name = mock_file_path
            input_validator.set_file_encoding(comparator_obj)
            with codecs.open(mock_file_path, 'r', encoding=comparator_obj.encoding) as f:
                for line in f:
                    assert line.strip() in rows

    def test_get_file_encoding_for_failing_encoding_cases(self):
        failing_encoding_names = self.create_mock_data_file_for_encoding_types(
            "failing_encoding_names.csv")
        comparator_obj = Compare()
        for encoding_val in failing_encoding_names:
            with pytest.raises(AppErrorHandler):
                mock_file_path = os.path.join(self.MOCK_DATA_DIR, f'{encoding_val}.csv')
                comparator_obj.file_name = mock_file_path
                input_validator.set_file_encoding(comparator_obj)

    ####################################################
    # input_validator.check_for_file_encoding
    ####################################################

    def test_verify_file_encoding_when_can_not_detect_encoding(self):
        not_able_to_detect_encoding_names = self.create_mock_data_file_for_encoding_types(
            "failing_encoding_names.csv")
        comparator_obj = Compare()
        for encoding_val in not_able_to_detect_encoding_names:
            with pytest.raises(AppErrorHandler):
                mock_file_path = os.path.join(self.MOCK_DATA_DIR, f'{encoding_val}.csv')
                comparator_obj.file_name = mock_file_path
                comparator_obj.encoding = 'ascii'
                input_validator.check_for_file_encoding(comparator_obj)

    def test_verify_file_encoding_when_can_detect_encoding(self):
        not_able_to_detect_encoding_names = self.create_mock_data_file_for_encoding_types(
            "failing_encoding_names.csv")
        comparator_obj = Compare()
        for encoding_val in not_able_to_detect_encoding_names:
            mock_file_path = os.path.join(self.MOCK_DATA_DIR, f'{encoding_val}.csv')
            comparator_obj.file_name = mock_file_path
            comparator_obj.encoding = encoding_val
            assert input_validator.check_for_file_encoding(comparator_obj) is None

    ####################################################
    # input_validator.check_for_file_size
    ####################################################
    @pytest.mark.parametrize('file_name', [
        'empty_csv_file.csv'])
    def test_check_for_file_size_to_not_be_zero_for_empty_file(self, file_name):
        comparable = Compare()
        comparable.file_name = os.path.join(self.MOCK_DATA_DIR, f'{file_name}')
        with pytest.raises(AppErrorHandler):
            input_validator.check_for_file_size(comparable)

    @pytest.mark.parametrize('file_name', [
        'simple_csv_file.csv'])
    def test_check_for_file_size_to_not_be_zero_for_small_file(self, file_name):
        comparable = Compare()
        comparable.file_name = os.path.join(self.MOCK_DATA_DIR, f'{file_name}')
        assert input_validator.check_for_file_size(comparable) is None

    ####################################################
    # input_validator.check_for_delimiter
    ####################################################
    def test_check_for_delimiter(self):
        comparable = Compare()
        comparable.file_name = os.path.join(self.MOCK_DATA_DIR,
                                            "simple_csv_file.csv")
        comparable.encoding = "utf-8"
        comparable.delimiter = ","
        assert input_validator.check_for_delimiter(comparable) is None

    def test_check_for_non_comma_delimiter(self):
        comparable = Compare()
        comparable.file_name = os.path.join(self.MOCK_DATA_DIR,
                                            "none_csv_file.txt")
        comparable.encoding = "utf-8"
        comparable.delimiter = ","
        with pytest.raises(AppErrorHandler):
            input_validator.check_for_delimiter(comparable)

    # ###########################
    # set_parameter
    # ###########################
    def test_set_parameter(self):
        parameters = mock_input_dict.parameter_with_all_required_key
        setting = Setting(parameters)
        comparable_1 = Compare(order=0)
        comparable_2 = Compare(order=1)
        input_validator.set_parameter(setting, comparable_1, comparable_2)

        for prm_key in parameters:
            if "_1_2_" in prm_key:
                assert getattr(Compare, format_parameter(prm_key, "_1_2_")) == parameters[prm_key]
            elif "_1_" in prm_key:
                assert getattr(comparable_1, format_parameter(prm_key, "_1_")) == parameters[
                    prm_key]
            elif "_2_" in prm_key:
                assert getattr(comparable_2, format_parameter(prm_key, "_2_")) == parameters[
                    prm_key]
            else:
                assert False

    # ###########################
    # set_default
    # ###########################
    def test_set_default(self):
        parameters = mock_input_dict.parameter_with_all_required_key
        setting = Setting(parameters)
        input_validator.set_default(setting)


def format_parameter(prm_key, flag):
    key = prm_key.replace(flag, "_")
    if "file_name" not in key:
        key = key.replace("file_", "")
    return key