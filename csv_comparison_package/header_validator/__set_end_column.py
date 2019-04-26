from csv_comparison_package import Compare
from csv_comparison_package.decorator import call_each


@call_each
def set_end_column(comparable: Compare):
    comparable.end_column = \
        comparable.number_of_index_column \
        + comparable.number_of_unnamed_columns \
        + comparable.number_of_duplicate_columns \
        + comparable.number_of_disjunctive_columns \
        + comparable.number_of_not_checked_columns \
        + comparable.number_of_mapped_columns \
        + comparable.number_of_regular_columns \
        + comparable.start_column \
        - 1  # explicitly including the end column
