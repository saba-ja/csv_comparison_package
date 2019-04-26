import os
import pytest
import pandas as pd
import numpy as np
from csv_comparison_package import index_validator
from csv_comparison_package import Compare


class TestIndexValidator:
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

    @pytest.fixture(scope="function")
    def mock_df(self):
        d = {'id': [1, 2, ' str  ', 'abc\t\t', 'a\nbc'],
             'x': ['  a  ', 10, '\nearth\t\t', ' a bc  ', 1],
             'y': [4, 21, '  c  ', 5, '\ny\t']}
        return pd.DataFrame(data=d, dtype="object")

    @pytest.fixture(scope="function")
    def mock_index(self):
        return [{
            "column_name": "id",
            "column_location": "1",

        }]

    # ###########################
    # index_validator.stringify_index
    # ###########################
    def test_stringify_index(self, mock_df, mock_index):
        comparable = Compare()
        comparable.data_frame = mock_df
        comparable.index_column_name = mock_index
        index_validator.stringify_index(comparable)
        for val in comparable.data_frame['id']:
            assert isinstance(val, str)

    ###########################
    # index_validator.strip_index
    ###########################
    def test_strip_index(self, mock_df, mock_index):
        comparable = Compare()
        comparable.data_frame = mock_df
        comparable.index_column_name = mock_index

        index_validator.strip_index(comparable)
        expected = [1, 2, 'str', 'abc', 'abc']
        assert expected == list(comparable.data_frame["id"])

    def test_strip_index_2(self, mock_index):
        comparable = Compare()
        data1 = pd.DataFrame(
            {'id': ['        1 ', '2           ', '     a \n\n', '\t\t\t b        \n', ' c '],
             "fname": ['p1', 'q1', 'r1', 's1', 'j1']})
        expected = pd.DataFrame({'id': ['1', '2', 'a', 'b', 'c'],
                                 "fname": ['p1', 'q1', 'r1', 's1', 'j1']})
        comparable.index_column_name = mock_index
        comparable.data_frame = data1
        index_validator.strip_index(comparable)
        assert expected.equals(data1)


    ###########################
    # index_validator.sort_index
    ###########################
    def test_sort_index(self, mock_index):
        comparable = Compare()
        comparable.index_column_name = mock_index
        d = {'id': ['1', '2', 'str', 'abc', 'abc']}
        comparable.data_frame = pd.DataFrame(data=d, dtype="object")
        index_validator.sort_index(comparable)
        expected = ['1', '2', 'abc', 'abc', 'str']
        assert expected == list(comparable.data_frame['id'])

    ###########################
    # index_validator.check_for_empty_index
    ###########################
    def test_check_for_empty_index(self, mock_index):
        comparable = Compare()
        comparable.index_column_name = mock_index
        d = {'id': ['', '', 'str', 'abc', 'abc', '', None, np.nan]}
        comparable.data_frame = pd.DataFrame(data=d, dtype="object")
        index_validator.check_for_empty_index(comparable)
        expected = [0, 1, 5, 6, 7]
        actual = comparable.empty_index
        assert expected == actual

    ###########################
    # index_validator.drop_empty_index
    ###########################
    def test_drop_empty_index(self, mock_index):
        comparable = Compare()
        comparable.index_column_name = mock_index
        d = {'id': ['', '', 'str', 'abc', 'abc', '', None]}
        comparable.data_frame = pd.DataFrame(data=d, dtype="object")
        comparable.empty_index = [0, 1, 5, 6]
        index_validator.drop_empty_index(comparable)
        expected = ['str', 'abc', 'abc']
        actual = list(comparable.data_frame["id"])
        assert expected == actual

    ###########################
    # index_validator.check_for_duplicate_index
    ###########################
    def test_check_for_duplicate_index(self, mock_index):
        comparable = Compare()
        comparable.index_column_name = mock_index
        d = {'id': ['dup1', '1', '2', 'dup1', '3', '4']}
        comparable.data_frame = pd.DataFrame(data=d, dtype="object")
        index_validator.check_for_duplicate_index(comparable)
        actual = list(comparable.duplicate_index['id'].values)
        expected = ['dup1', 'dup1']
        assert expected == actual

    ###########################
    # index_validator.get_index_name
    ###########################
    def test_get_index_name(self, mock_index):
        comparable = Compare()
        comparable.index_column_name = mock_index
        assert index_validator.get_index_name(comparable) == 'id'

    ###########################
    # index_validator.drop_duplicate_index
    ###########################
    def test_drop_duplicate_index(self, mock_index):
        comparable = Compare()
        comparable.index_column_name = mock_index
        d = {'id': ['dup1', 'dup1', 'dup1', 'AAA', 'BBB']}
        dup = {'id': ['dup1', 'dup1', 'dup1']}
        comparable.data_frame = pd.DataFrame(data=d, dtype="object")
        comparable.duplicate_index = pd.DataFrame(data=dup, dtype="object")
        index_validator.drop_duplicate_index(comparable)
        expected = ['AAA', 'BBB']
        actual = list(comparable.data_frame['id'].values)
        assert expected == actual

    ###########################
    # index_validator.check_for_disjunctive_index
    ###########################
    def test_check_for_disjunctive_index(self, mock_index):
        comparable_1 = Compare()
        comparable_2 = Compare()
        comparable_1.index_column_name = mock_index
        comparable_2.index_column_name = mock_index
        data1 = {'id': ['a', 'b', '1', '2', 'c'], "fname": ['p1', 'q1', 'r1', 's1', 'j1']}
        data2 = {'id': ['a', 'b', '3', '4', 'c'], "fname": ['p2', 'q2', 'r2', 's2', 'j2']}
        comparable_1.data_frame = pd.DataFrame(data=data1, dtype="object")
        comparable_2.data_frame = pd.DataFrame(data=data2, dtype="object")
        index_validator.check_for_disjunctive_index(comparable_1, comparable_2)
        expected = ['1', '2']
        actual = list(comparable_1.disjunctive_index['id'].values)
        assert expected == actual

    ###########################
    # index_validator.drop_disjunctive_index
    ###########################
    def test_drop_disjunctive_index(self, mock_index):
        comparable = Compare()
        comparable.index_column_name = mock_index
        data1 = {'id': ['1', '2', 'a', 'b', 'c'], "fname": ['p1', 'q1', 'r1', 's1', 'j1']}
        comparable.data_frame = pd.DataFrame(data=data1, dtype="object")
        disjunctive = {'id': ['1', '2']}
        comparable.disjunctive_index = pd.DataFrame(data=disjunctive, dtype="object")
        index_validator.drop_disjunctive_index(comparable)
        expected = ['a', 'b', 'c']
        actual = list(comparable.data_frame['id'].values)
        assert expected == actual
