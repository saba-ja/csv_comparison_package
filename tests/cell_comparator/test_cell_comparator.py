from csv_comparison_package import cell_comparator
from csv_comparison_package import Compare
import pandas as pd


class TestIndexValidator:
    mock_header = [
        {"column_name": "id", "column_location": 1, "column_type": "index"},
        {"column_name": "first_name", "column_location": 2, "column_type": ""},
        {"column_name": "last_name", "column_location": 3, "column_type": "not_checked"},
        {"column_name": "middle_name", "column_location": 3, "column_type": "not_checked"},
        {"column_name": "requirement", "column_location": 5, "column_type": "mapped"},
        {"column_name": "alternate_name", "column_location": 6, "column_type": ""}]
    mock_index = [{"column_name": "id", "column_location": 1}]

    mock_data_a = {
        'id': [1, 2, 3],
        'first_name': ['f1', 'f2', 'f3'],
        'last_name': ['l1', 'l2', 'l3'],
        'middle_name': ['m1', 'm2', 'm3'],
        'requirement': ['r1', 'r2', 'r3'],
        'alternate_name': ['a1', 'a2', 'a3']
    }

    mock_data_non_printable_char = {
        'id': [1, 2, 3],
        'first_name': ['f1µ', 'f2∫', 'f3√'],
        'last_name': ['l1', 'l2', 'l3'],
        'middle_name': ['m1', 'm2', 'm3'],
        'requirement': ['r1˙©ß∂ƒ©', 'r2ß∂ƒ´´´†', 'r3††††'],
        'alternate_name': ['a1¥¥', 'a2®®®', 'a3åßƒåß∂ƒƒ∂©˙¨']
    }

    mock_data_white_space_char = {
        'id': [1, 2, 3],
        'first_name': ['f1\n\n', 'f\n2', 'f3\n\n\t\n'],
        'last_name': ['l1', 'l2', 'l3'],
        'middle_name': ['m1', 'm2', 'm3'],
        'requirement': ['r1\n\t\t\n', '\nr\n2\n', '\t\tr\t\n3\n'],
        'alternate_name': ['\na\n1\n', '\ta\t2\t', '\t\na\t\n3\t\n']
    }

    def test_validate_index_identity(self):
        comparable_a = Compare()
        comparable_b = Compare()

        comparable_a.header = TestIndexValidator.mock_header
        comparable_a.index_column_name = TestIndexValidator.mock_index

        comparable_b.header = TestIndexValidator.mock_header
        comparable_b.index_column_name = TestIndexValidator.mock_index

        data = TestIndexValidator.mock_data_a

        comparable_a.data_frame = pd.DataFrame(data)
        comparable_b.data_frame = pd.DataFrame(data)

        assert cell_comparator.validate_index_identity(comparable_a, comparable_b) is None

    # ###########################
    # cell_validator.remove_non_printable_char
    # ###########################
    def test_remove_non_printable_char(self):
        comparable = Compare()
        comparable.header = TestIndexValidator.mock_header
        comparable.index_column_name = TestIndexValidator.mock_index
        comparable.data_frame = pd.DataFrame(TestIndexValidator.mock_data_non_printable_char)
        cell_comparator.remove_non_printable_char(comparable)
        expected = pd.DataFrame({
            'id': [1, 2, 3],
            'first_name': ['f1', 'f2', 'f3'],
            'last_name': ['l1', 'l2', 'l3'],
            'middle_name': ['m1', 'm2', 'm3'],
            'requirement': ['r1', 'r2', 'r3'],
            'alternate_name': ['a1', 'a2', 'a3']
        })

        assert (expected["id"].equals(comparable.data_frame["id"]))
        assert (expected["first_name"].equals(comparable.data_frame["first_name"]))
        assert (expected["last_name"].equals(comparable.data_frame["last_name"]))
        assert (expected["middle_name"].equals(comparable.data_frame["middle_name"]))
        assert (expected["requirement"].equals(comparable.data_frame["requirement"]))
        assert (expected["alternate_name"].equals(comparable.data_frame["alternate_name"]))

    # ###########################
    # cell_validator.remove_white_space_char
    # ###########################

    def test_remove_white_space_char(self):
        comparable = Compare()
        comparable.header = TestIndexValidator.mock_header
        comparable.index_column_name = TestIndexValidator.mock_index
        comparable.data_frame = pd.DataFrame(TestIndexValidator.mock_data_white_space_char)
        cell_comparator.remove_non_printable_char(comparable)
        expected = pd.DataFrame({
            'id': [1, 2, 3],
            'first_name': ['f1', 'f 2', 'f3'],
            'last_name': ['l1', 'l2', 'l3'],
            'middle_name': ['m1', 'm2', 'm3'],
            'requirement': ['r1', 'r 2', 'r 3'],
            'alternate_name': ['a 1', 'a 2', 'a 3']
        })

        cell_comparator.remove_white_space_char(comparable)
        assert expected.equals(comparable.data_frame)
