from csv_comparison_package.error_handler import AppErrorHandler
from csv_comparison_package.field import Field


def check_for_type_string(comparator):
    """Check for parameter value with type string to be string"""
    for key_val in comparator.default_schema:
        is_key_available = all([key_val[Field.prm_name.value] in comparator.parameters,
                                key_val[Field.prm_type.value] is str])

        if is_key_available:
            if not isinstance(comparator.parameters[key_val[Field.prm_name.value]], str):
                raise AppErrorHandler(AppErrorHandler.invalid_value_type)
