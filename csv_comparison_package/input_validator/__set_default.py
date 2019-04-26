from csv_comparison_package import Field


def set_default(setting):
    for schema_key in setting.default_schema:
        if not schema_key[Field.prm_required.value]:
            key = schema_key[Field.prm_name.value]
            if key in setting.parameters:
                if setting.parameters[key] == Field.empty_string.value:
                    setting.parameters[key] = schema_key[Field.prm_default_value.value]
            else:
                setting.parameters[key] = schema_key[Field.prm_default_value.value]
