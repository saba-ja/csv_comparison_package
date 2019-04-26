from csv_comparison_package import Compare


def set_start_column(comparable_a: Compare, comparable_b: Compare):
    comparable_a.start_column = 1  # not supporting multi index
    comparable_b.start_column = \
        comparable_a.number_of_index_column \
        + comparable_a.number_of_unnamed_columns \
        + comparable_a.number_of_duplicate_columns \
        + comparable_a.number_of_disjunctive_columns \
        + comparable_a.number_of_not_checked_columns \
        + comparable_a.number_of_mapped_columns \
        + comparable_a.number_of_regular_columns \
        + 1  # The first column is for labels and xlxwriter is 0 based
