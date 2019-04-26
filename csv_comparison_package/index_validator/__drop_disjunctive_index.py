from csv_comparison_package import index_validator as idx
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def drop_disjunctive_index(comparable: Compare):
    index_name = idx.get_index_name(comparable)
    index_of_disjunctive = comparable.disjunctive_index[index_name].index.values
    comparable.data_frame = comparable.data_frame.drop(index_of_disjunctive)
