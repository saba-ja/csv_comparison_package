from csv_comparison_package.error_handler import AppErrorHandler
from csv_comparison_package.field import Field


def check_for_required_key(comparator):
    """Check for required parameter key to exist"""
    for key_val in comparator.default_schema:
        is_required = key_val[Field.prm_required.value]
        is_missing = key_val[Field.prm_name.value] not in comparator.parameters
        if all([is_required, is_missing]):
            raise AppErrorHandler(AppErrorHandler.missing_required_key.
                                  format(key_val[Field.prm_name.value]))
