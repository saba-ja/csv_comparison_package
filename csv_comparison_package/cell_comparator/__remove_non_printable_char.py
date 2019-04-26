import string
from csv_comparison_package import Compare
from csv_comparison_package import Field
from csv_comparison_package import header_validator
from csv_comparison_package.decorator import call_each


@call_each
def remove_non_printable_char(comparable: Compare):
    if comparable.ignore_non_printable_character:

        for header_index, header in enumerate(header_validator.get_checked_column_name(comparable)):
            header_name = header[Field.column_name.value]
            for index in list(comparable.data_frame.index.values):
                cell_val = comparable.data_frame.loc[index, header_name]
                cleaned_cell_val = ''.join(
                    filter(lambda x: x in set(string.printable), str(cell_val)))
                comparable.data_frame.loc[index, header_name] = cleaned_cell_val
