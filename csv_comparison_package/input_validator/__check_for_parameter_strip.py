from csv_comparison_package.field import Field


def check_for_parameter_strip(comparator):
    """"Check for parameters that need to be stripped"""
    for key in comparator.default_schema:
        is_key_available = all([key[Field.prm_name.value] in comparator.parameters,
                                key[Field.prm_type.value] is str,
                                Field.prm_should_be_strip.value in key])

        if is_key_available:
            if isinstance(comparator.parameters[key[Field.prm_name.value]], str) and \
                    key[Field.prm_should_be_strip.value]:
                comparator.parameters[key[Field.prm_name.value]] = \
                    comparator.parameters[key[Field.prm_name.value]].strip()
