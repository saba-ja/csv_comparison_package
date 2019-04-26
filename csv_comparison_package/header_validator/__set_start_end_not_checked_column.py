from csv_comparison_package import Compare
from csv_comparison_package.decorator import call_each


@call_each
def set_start_end_not_checked_column(comparable: Compare):
    if comparable.number_of_not_checked_columns > 0:
        comparable.not_checked_column_start = \
            comparable.start_column \
            + comparable.number_of_index_column \
            + comparable.number_of_regular_columns \
            + comparable.number_of_mapped_columns \
            + 1 - 1

        comparable.not_checked_column_end = \
            comparable.not_checked_column_start \
            + comparable.number_of_not_checked_columns \
            - 1
