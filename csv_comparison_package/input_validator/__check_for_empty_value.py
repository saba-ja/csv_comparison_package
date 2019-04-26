from csv_comparison_package.error_handler import AppErrorHandler
from csv_comparison_package.field import Field


def check_for_empty_value(comparator):
    """ Check for parameters that can not have empty value"""
    for key_val in comparator.default_schema:
        is_key_available = all([key_val[Field.prm_required.value],
                                key_val[Field.prm_name.value] in comparator.parameters,
                                key_val[Field.prm_default_value.value] is None])

        if is_key_available:
            is_value_blank = comparator.parameters[key_val[Field.prm_name.value]] == \
                             Field.empty_string.value
            if is_value_blank:
                raise AppErrorHandler(AppErrorHandler.invalid_value)
