from csv_comparison_package import Compare
from csv_comparison_package.decorator import call_each


@call_each
def copy_df_to_trimmed_df(comparable: Compare):
    comparable.data_frame_trimmed = comparable.data_frame.copy(deep=True)
