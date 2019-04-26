from csv_comparison_package.error_handler import AppErrorHandler
from csv_comparison_package.field import Field


def check_for_parameter_type(comparator):
    for key in comparator.default_schema:
        is_key_available = key[Field.prm_name.value] in comparator.parameters

        if is_key_available:

            is_value_not_empty = comparator.parameters[
                                     key[Field.prm_name.value]] != Field.empty_string.value
            is_value_wrong_type = not isinstance(comparator.parameters[key[Field.prm_name.value]],
                                                 key[Field.prm_type.value])

            if is_value_not_empty and is_value_wrong_type:
                raise AppErrorHandler(AppErrorHandler.invalid_value_type)
