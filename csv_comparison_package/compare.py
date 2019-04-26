class Compare:
    output_path = ""
    output_file_name = ""
    workbook = ""
    worksheet_name = ""  # Master
    worksheet_master = ""
    # ------------------------
    map_columns = ""
    """ 
    Columns needed to be compared with each other 
    [(
        {"column_name":"column name file 1", "column_location": 1}, 
        {"column_name":"column name file 2", "column_location": 1}
    )]
    or 
    [(
        {"column_name":"column name file 1", "column_location": 'A'}, 
        {"column_name":"column name file 2", "column_location": 'A'}
    )]

    """

    def __init__(self, order=0):
        self.file_name = ""
        """
        /path/to/file.csv
        """
        # ------------------------
        self.order = order
        """it will be 0 for file_1 and 1 for file_2"""
        # ------------------------

        self.header_row = 1
        """ 
        An integer number defining the location of header row. The default is 1
        """
        # ------------------------
        self.original_header = ""
        """
        List of original header names extracted from the file
        ['header_1','header_2',...]
        """
        # ------------------------

        self.header = []
        """
        Headers dictionary that will be used in the application. The format is the following
         [
            {"column_name":"column name 1", 
            "column_location": 1, 
            "column_type":"unnamed|duplicate|disjunctive|not-be-checked|"},
              
            {"column_name":"column name 2", "column_location": 2,
            "column_type":"unnamed|duplicate|disjunctive|not-be-checked|"}
         ]
        """

        # ------------------------

        self.index_column_name = []
        """ 
        The column name or column location of the primary key. 
        e.g 
        [{"column_name":"column name", "column_location": 1}]
        or
        [{"column_name":"column name", "column_location": 'A'}]
        """

        # ------------------------

        self.compare_only_mapped_columns = ""
        self.hide_modified_columns = ""
        self.hide_not_checked_columns = ""
        self.hide_disjunctive_columns = ""
        self.hide_duplicate_columns = ""
        self.hide_unnamed_columns = ""
        self.hide_not_modified_rows = ""
        self.encoding = ""
        self.delimiter = ""
        # ------------------------
        self.data_type = ""
        """ 
        Data type used in pandas. The default is 'object'
        """
        # ------------------------
        self.original_data_frame = ""
        self.data_frame = ""
        self.data_frame_trimmed = ""
        self.empty_index = ""  # list
        self.duplicate_index = ""  # dataframe
        self.disjunctive_index = ""  # dataframe
        self.not_checked_column = ""  # dataframe
        self.disjunctive_column = ""  # dataframe
        self.duplicate_column = ""  # dataframe
        self.unnamed_column = ""
        # ------------------------ Columns location `0` based
        self.start_column = ""
        self.end_column = ""

        self.index_column_start = ""
        self.index_column_end = ""

        self.checked_column_start = ""
        self.checked_column_end = ""

        self.not_checked_column_start = ""
        self.not_checked_column_end = ""

        self.disjunctive_column_start = ""
        self.disjunctive_column_end = ""

        self.duplicate_column_start = ""
        self.duplicate_column_end = ""

        self.unnamed_column_start = ""
        self.unnamed_column_end = ""

        # ------------------------ Excel local formats
        self.column_general_format = ""
        self.header_format_left_border = ""
        self.header_format_left_bottom_border = ""
        self.header_format_bottom_border = ""
        self.header_format = ""
        # ------------------------
        self.number_of_index_column = 0  # not supporting multi index
        self.number_of_unnamed_columns = 0
        self.number_of_duplicate_columns = 0
        self.number_of_disjunctive_columns = 0
        self.number_of_not_checked_columns = 0
        self.number_of_mapped_columns = 0
        self.number_of_regular_columns = 0
        # ------------------------
        self.ignore_non_printable_character = True
        self.ignore_trailing_white_space_character = True
        self.ignore_upper_and_lower_case = True
