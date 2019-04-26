from csv_comparison_package import data_exporter
from csv_comparison_package import Compare
import datetime


class TestDataExporter:

    # ###########################
    # date_exporter.get_formatted_time
    # ###########################

    def test_get_formatted_time(self):
        actual = data_exporter.get_formatted_time()
        now = datetime.datetime.now()
        result = actual.split('_')
        assert f"{now.year:04d}" == result[0]
        assert f"{now.month:02d}" == result[1]
        assert f"{now.day:02d}" == result[2]
        assert len(result[3]) == 3
        assert len(result[4]) == 3
        assert len(result[5]) == 3
        assert len(result[6]) == 6

    # ###########################
    # date_exporter.extract_file_name_from_path
    # ###########################

    def test_extract_file_name_from_path(self):
        comparable = Compare()
        comparable.file_name = "/path/to/directory/my_file.csv"
        actual = data_exporter.extract_file_name_from_path(comparable)
        assert "my_file_csv" == actual

    def test_extract_file_name_from_path_long_name(self):
        comparable = Compare()
        comparable.file_name = "/path/to/directory/" \
                               "this_is_a_very_long_file_name_that_must_be_truncated.csv"
        actual = data_exporter.extract_file_name_from_path(comparable)
        assert "this_is_a_very_" == actual

    # ###########################
    # date_exporter.create_name_for_output_file
    # ###########################
    def test_create_name_for_output_file(self):
        comparable_a = Compare()
        comparable_b = Compare()
        comparable_a.file_name = "my_first_file"
        comparable_b.file_name = "my_second_file"
        Compare.output_path = "./"
        data_exporter.create_name_for_output_file(comparable_a, comparable_b)
        my_string = "F1_" + comparable_a.file_name + "_F2_" + comparable_a.file_name
        assert Compare.output_file_name.find(my_string)

    # ###########################
    # date_importer.
    # ###########################

    def test_create_the_entire_excel_file(self):
        comparable_1 = Compare()
        comparable_2 = Compare()

        comparable_1.order = 0

        comparable_1.start_column = 1
        comparable_1.end_column = 12
        comparable_1.index_column_start = 1
        comparable_1.index_column_end = 1
        comparable_1.checked_column_start = 2
        comparable_1.checked_column_end = 3
        comparable_1.not_checked_column_start = 4
        comparable_1.not_checked_column_end = 5
        comparable_1.disjunctive_column_start = 6
        comparable_1.disjunctive_column_end = 7
        comparable_1.duplicate_column_start = 8
        comparable_1.duplicate_column_end = 9
        comparable_1.unnamed_column_start = 10
        comparable_1.unnamed_column_end = 11

        comparable_1.file_name = "/path/to.my/file/my_first_file___1.csv"
        comparable_1.header = [
            {"column_name": "id", "column_location": 1, "column_type": "index"},
            {"column_name": "first_name", "column_location": 2, "column_type": "not_checked"},
            {"column_name": "last_name(@duplicate)", "column_location": 3, "column_type": "duplicate"},
            {"column_name": "last_name(@duplicate)", "column_location": 4, "column_type": "duplicate"},
            {"column_name": "requirement1", "column_location": 5, "column_type": "mapped"},
            {"column_name": "requirement2", "column_location": 6, "column_type": "mapped"},
            {"column_name": "alternate_name", "column_location": 7, "column_type": "not_checked"},
            {"column_name": "@unnamed", "column_location": 8, "column_type": "unnamed"},
            {"column_name": "@unnamed", "column_location": 9, "column_type": "unnamed"},
            {"column_name": "some_name(@NotFound)", "column_location": 10, "column_type": "disjunctive"},
            {"column_name": "some_name(@NotFound)", "column_location": 11, "column_type": "disjunctive"},
        ]
        comparable_1.index_column_name = [
            {"column_name": "id", "column_location": 1, "column_type": ""}]

        comparable_2.header = [
            {"column_name": "id", "column_location": 1, "column_type": "index"},
            {"column_name": "first_name", "column_location": 2, "column_type": "not_checked"},
            {"column_name": "last_name(@duplicate.4)", "column_location": 4, "column_type": "duplicate"},
            {"column_name": "last_name(@duplicate.3)", "column_location": 3, "column_type": "duplicate"},
            {"column_name": "requirement1", "column_location": 5, "column_type": "mapped"},
            {"column_name": "requirement2", "column_location": 6, "column_type": "mapped"},
            {"column_name": "alternate_name", "column_location": 7, "column_type": "not_checked"},
            {"column_name": "@unnamed.8", "column_location": 8, "column_type": "unnamed"},
            {"column_name": "@unnamed.9", "column_location": 9, "column_type": "unnamed"},
            {"column_name": "some_name(@NotFound.10)", "column_location": 10, "column_type": "disjunctive"},
            {"column_name": "some_name(@NotFound.11)", "column_location": 11, "column_type": "disjunctive"},
        ]

        comparable_2.index_column_name = [
            {"column_name": "id", "column_location": 1, "column_type": ""}]

        comparable_2.order = 1
        comparable_2.start_column = 12
        comparable_2.end_column = 22

        comparable_2.index_column_start = 12
        comparable_2.index_column_end = 12
        comparable_2.checked_column_start = 13
        comparable_2.checked_column_end = 14
        comparable_2.not_checked_column_start = 15
        comparable_2.not_checked_column_end = 16
        comparable_2.disjunctive_column_start = 17
        comparable_2.disjunctive_column_end = 18
        comparable_2.duplicate_column_start = 19
        comparable_2.duplicate_column_end = 20
        comparable_2.unnamed_column_start = 21
        comparable_2.unnamed_column_end = 22

        comparable_2.hide_duplicate_columns = True
        comparable_2.hide_unnamed_columns = True
        comparable_2.hide_disjunctive_columns = True

        comparable_2.file_name = "/path/to.my/file/my_second_file__2.csv"

        Compare.output_path = "./"
        Compare.worksheet_name = "Master"

        data_exporter.create_name_for_output_file(comparable_1, comparable_2)
        data_exporter.create_excel_workbook()
        data_exporter.create_excel_worksheet()
        data_exporter.add_local_excel_format([comparable_1, comparable_2])
        data_exporter.apply_column_general_format([comparable_1, comparable_2])
        data_exporter.write_file_name_label()
        data_exporter.write_file_name_title([comparable_1, comparable_2])
        data_exporter.write_column_type_label()
        data_exporter.write_index_column_type_title([comparable_1, comparable_2])
        data_exporter.write_checked_column_type_title([comparable_1, comparable_2])
        data_exporter.write_not_checked_column_type_title([comparable_1, comparable_2])
        data_exporter.write_disjunctive_column_type_title([comparable_1, comparable_2])
        data_exporter.write_duplicate_column_type_title([comparable_1, comparable_2])
        data_exporter.write_unnamed_column_type_title([comparable_1, comparable_2])

        data_exporter.apply_checked_column_hide_condition([comparable_1, comparable_2])
        data_exporter.apply_not_checked_column_hide_condition([comparable_1, comparable_2])
        data_exporter.apply_disjunctive_column_hide_condition([comparable_1, comparable_2])
        data_exporter.apply_duplicate_column_hide_condition([comparable_1, comparable_2])
        data_exporter.apply_unnamed_column_hide_condition([comparable_1, comparable_2])

        data_exporter.write_column_name_label()
        data_exporter.write_index_column_name([comparable_1, comparable_2])
        data_exporter.write_checked_column_name([comparable_1, comparable_2])
        data_exporter.write_not_checked_column_name([comparable_1, comparable_2])
        data_exporter.write_disjunctive_column_name([comparable_1, comparable_2])
        data_exporter.write_duplicate_column_name([comparable_1, comparable_2])
        data_exporter.write_unnamed_column_name([comparable_1, comparable_2])
        data_exporter.close_excel_workbook()
