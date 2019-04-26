import os
import pytest
import pandas as pd
from csv_comparison_package import Field
from csv_comparison_package import Compare
from csv_comparison_package import AppErrorHandler
from csv_comparison_package import data_importer
import tests.mock_data_importer_dict as mock_importer_dict


class TestDataImporter:
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
    # object order setup test
    # ###########################
    def test_for_object_order(self):
        c0 = Compare(order=0)
        c1 = Compare(order=1)
        assert 0 == c0.order
        assert 1 == c1.order

    # ###########################
    # data_importer.import_file
    # ###########################
    @pytest.mark.parametrize('comparable',
                             [mock_importer_dict.parameter_for_import_file_passing_case],
                             indirect=['comparable'])
    def test_import_file(self, comparable):
        data_importer.import_file(comparable)
        columns = list(comparable.original_data_frame.columns.values)
        expected_columns = ["id", "first_name", "last_name", "telephone"]
        assert columns == expected_columns

    @pytest.mark.parametrize('comparable',
                             [mock_importer_dict.parameter_for_import_file_no_file_case],
                             indirect=['comparable'])
    def test_import_file_failing_to_open(self, comparable):
        with pytest.raises(AppErrorHandler):
            data_importer.import_file(comparable)

    @pytest.mark.parametrize(
        'comparable',
        [mock_importer_dict.parameter_for_import_file_failing_decoding_raising_unicode_error_case,
         mock_importer_dict.parameter_for_import_file_failing_decoding_raising_lookup_error_case,
         mock_importer_dict.parameter_for_import_file_failing_decoding_raising_empty_error_case],
        indirect=['comparable'])
    def test_import_file_failing_to_decode_unicode_error(self, comparable):
        with pytest.raises(AppErrorHandler):
            data_importer.import_file(comparable)

    # ###########################
    # data_importer.set_data_frame
    # ###########################
    def test_set_data_frame(self):
        comparable = Compare()
        comparable.original_data_frame = pd.DataFrame({'x': [1, 2]})
        data_importer.set_data_frame(comparable)
        comparable.data_frame.x[0] = -1
        assert not list(comparable.original_data_frame.x) == list(comparable.data_frame.x)

    # ###########################
    # data_importer.extract_not_checked_column
    # ###########################
    def test_extract_not_checked_column(self):
        comparable = Compare()
        comparable.header = [
            {"column_name": "id", "column_location": 1, "column_type": ""},
            {"column_name": "first_name", "column_location": 2, "column_type": ""},
            {"column_name": "last_name", "column_location": 3, "column_type": "not_checked"},
            {"column_name": "middle_name", "column_location": 3, "column_type": "not_checked"},
            {"column_name": "requirement", "column_location": 5, "column_type": "mapped"},
            {"column_name": "alternate_name", "column_location": 6, "column_type": ""}]
        comparable.index_column_name = [
            {"column_name": "id", "column_location": 1}]
        data = {
            'id': [1, 2, 3],
            'first_name': ['f1', 'f2', 'f3'],
            'last_name': ['l1', 'l2', 'l3'],
            'middle_name': ['m1', 'm2', 'm3'],
            'requirement': ['r1', 'r2', 'r3'],
            'alternate_name': ['a1', 'a2', 'a3']
        }
        expected = pd.DataFrame({'last_name': ['l1', 'l2', 'l3'],
                                 'middle_name': ['m1', 'm2', 'm3']})

        comparable.data_frame = pd.DataFrame(data)
        data_importer.extract_not_checked_column(comparable)
        assert expected.equals(comparable.not_checked_column)

    def test_drop_not_checked_column(self):
        comparable = Compare()
        comparable.header = [
            {"column_name": "id", "column_location": 1, "column_type": ""},
            {"column_name": "first_name", "column_location": 2, "column_type": ""},
            {"column_name": "last_name", "column_location": 3, "column_type": "not_checked"},
            {"column_name": "middle_name", "column_location": 3, "column_type": "not_checked"},
            {"column_name": "requirement", "column_location": 5, "column_type": "mapped"},
            {"column_name": "alternate_name", "column_location": 6, "column_type": ""}]
        comparable.index_column_name = [
            {"column_name": "id", "column_location": 1}]
        data = {
            'id': [1, 2, 3],
            'first_name': ['f1', 'f2', 'f3'],
            'last_name': ['l1', 'l2', 'l3'],
            'middle_name': ['m1', 'm2', 'm3'],
            'requirement': ['r1', 'r2', 'r3'],
            'alternate_name': ['a1', 'a2', 'a3']
        }
        expected = pd.DataFrame({
            'id': [1, 2, 3],
            'first_name': ['f1', 'f2', 'f3'],
            'requirement': ['r1', 'r2', 'r3'],
            'alternate_name': ['a1', 'a2', 'a3']
        })

        comparable.data_frame = pd.DataFrame(data)
        data_importer.drop_not_checked_column(comparable)
        assert expected.equals(comparable.data_frame)

    # ###########################
    # data_importer.freeze_pandas_index
    # ###########################
    def test_freeze_pandas_index(self):
        comparable = Compare()
        df = pd.DataFrame({'a': ['x', 'y', 'z']})
        expected = pd.DataFrame(
            {'a': ['x', 'y', 'z'], Field.pandas_original_index.value: [0, 1, 2]})
        comparable.original_data_frame = df
        data_importer.freeze_pandas_index(comparable)
        assert df.equals(expected)

