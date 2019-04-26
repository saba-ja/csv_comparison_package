from csv_comparison_package.error_handler import AppErrorHandler
from csv_comparison_package.field import Field


def check_for_special_character(comparator):
    forbidden_characters = ['*', '?', ':', '"', '<', '>', '|', ']', '[', "'"]
    for key in comparator.default_schema:
        is_key_available = all([key[Field.prm_name.value] in comparator.parameters,
                                Field.prm_can_have_special_char.value in key])

        if is_key_available:
            submitted_value = comparator.parameters[key[Field.prm_name.value]]
            is_submitted_value_str = isinstance(submitted_value, str)

            if is_submitted_value_str:
                is_containing_forbidden_char = any(
                    [x in forbidden_characters
                     for x in list(comparator.parameters[key[Field.prm_name.value]])])

                if is_containing_forbidden_char:
                    raise AppErrorHandler(AppErrorHandler.invalid_value)
