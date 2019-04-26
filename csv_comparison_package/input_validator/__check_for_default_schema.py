from csv_comparison_package.error_handler import AppErrorHandler
from csv_comparison_package.field import Field


def check_for_default_schema(comparator):
    """Check for submitted parameter keys to exist in default schema"""
    submitted_keys = list(comparator.parameters.keys())
    default_schema_keys = [key_val[Field.prm_name.value] for key_val in comparator.default_schema]
    is_any_key_missing = not all(user_submitted_key in default_schema_keys
                                 for user_submitted_key in submitted_keys)
    if is_any_key_missing:
        raise AppErrorHandler(AppErrorHandler.no_parameter)
