from csv_comparison_package import index_validator as idx
from csv_comparison_package import Compare


def check_for_disjunctive_index(comparable_a: Compare, comparable_b: Compare):
    index_name_a = idx.get_index_name(comparable_a)
    index_name_b = idx.get_index_name(comparable_b)
    comparable_a.disjunctive_index = comparable_a.data_frame[
        ~comparable_a.data_frame[index_name_a].isin(
            comparable_b.data_frame[index_name_b])]
