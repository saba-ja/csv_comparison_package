from csv_comparison_package import Compare
from csv_comparison_package.decorator import call_each


@call_each
def convert_to_lower_case(comparable: Compare):
    if comparable.ignore_upper_and_lower_case:
        comparable.data_frame_trimmed = comparable.data_frame_trimmed.apply(
            lambda x: x.astype(str).str.lower())
