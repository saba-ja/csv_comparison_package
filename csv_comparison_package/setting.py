from csv_comparison_package.input_schema import Schema


class Setting(Schema):

    def __init__(self, parameters):
        self.parameters = parameters
