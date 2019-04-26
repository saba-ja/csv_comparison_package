BORDER_COLOR = "#BFBFBF"
BOLD_BORDER_SIZE = 2
BOLD_BORDER_COLOR = "#808080"
HEADER_ROW_FONT_SIZE = 12

COLOR_FILE_1 = "#203857"
BG_COLOR_FILE_1 = "#D7E2EF"

COLOR_FILE_2 = "#8C3E07"
BG_COLOR_FILE_2 = "#FDe6D4"
# ##################################
# General style for checked columns
# ##################################
# General color for all cells that have been checked in 1 and 2
general_column_format = ({
                             'bold': False,
                             'color': COLOR_FILE_1,
                             'bg_color': BG_COLOR_FILE_1,
                             'border': 1,
                             'border_color': BORDER_COLOR,
                             'text_wrap': False,
                             'align': 'left',
                             'valign': 'top'
                         },
                         {
                             'bold': False,
                             'color': COLOR_FILE_2,
                             'bg_color': BG_COLOR_FILE_2,
                             'border': 1,
                             'border_color': BORDER_COLOR,
                             'text_wrap': False,
                             'align': 'left',
                             'valign': 'top'
                         })
# ##################################
# Style for header columns
# ##################################
header_format_left_border = ({
                                 'font_size': HEADER_ROW_FONT_SIZE,
                                 'bold': True,
                                 'color': COLOR_FILE_1,
                                 'bg_color': BG_COLOR_FILE_1,
                                 'border': 1,
                                 'border_color': BORDER_COLOR,
                                 'left': BOLD_BORDER_SIZE,
                                 'left_color': BOLD_BORDER_COLOR,
                                 'text_wrap': False,
                                 'align': 'left',
                                 'valign': 'vcenter'
                             },

                             {
                                 'font_size': HEADER_ROW_FONT_SIZE,
                                 'bold': True,
                                 'color': COLOR_FILE_2,
                                 'bg_color': BG_COLOR_FILE_2,
                                 'border': 1,
                                 'border_color': BORDER_COLOR,
                                 'left': BOLD_BORDER_SIZE,
                                 'left_color': BOLD_BORDER_COLOR,
                                 'text_wrap': False,
                                 'align': 'left',
                                 'valign': 'vcenter'
                             })

header_format_left_bottom_border = ({
                                        'font_size': HEADER_ROW_FONT_SIZE,
                                        'bold': True,
                                        'color': COLOR_FILE_1,
                                        'bg_color': BG_COLOR_FILE_1,
                                        'border': 1,
                                        'border_color': BORDER_COLOR,
                                        'left': BOLD_BORDER_SIZE,
                                        'left_color': BOLD_BORDER_COLOR,
                                        'text_wrap': False,
                                        'align': 'left',
                                        'valign': 'vcenter',
                                        'bottom': BOLD_BORDER_SIZE,
                                        'bottom_color': BOLD_BORDER_COLOR,

                                    },
                                    {
                                        'font_size': HEADER_ROW_FONT_SIZE,
                                        'bold': True,
                                        'color': COLOR_FILE_2,
                                        'bg_color': BG_COLOR_FILE_2,
                                        'border': 1,
                                        'border_color': BORDER_COLOR,
                                        'left': BOLD_BORDER_SIZE,
                                        'left_color': BOLD_BORDER_COLOR,
                                        'text_wrap': False,
                                        'align': 'left',
                                        'valign': 'vcenter',
                                        'bottom': BOLD_BORDER_SIZE,
                                        'bottom_color': BOLD_BORDER_COLOR,
                                    })

header_format_bottom_border = ({
                                   'font_size': HEADER_ROW_FONT_SIZE,
                                   'bold': True,
                                   'color': COLOR_FILE_1,
                                   'bg_color': BG_COLOR_FILE_1,
                                   'border': 1,
                                   'border_color': BORDER_COLOR,
                                   'text_wrap': False,
                                   'align': 'left',
                                   'valign': 'vcenter',
                                   'bottom': BOLD_BORDER_SIZE,
                                   'bottom_color': BOLD_BORDER_COLOR,

                               },
                               {
                                   'font_size': HEADER_ROW_FONT_SIZE,
                                   'bold': True,
                                   'color': COLOR_FILE_2,
                                   'bg_color': BG_COLOR_FILE_2,
                                   'border': 1,
                                   'border_color': BORDER_COLOR,
                                   'text_wrap': False,
                                   'align': 'left',
                                   'valign': 'vcenter',
                                   'bottom': BOLD_BORDER_SIZE,
                                   'bottom_color': BOLD_BORDER_COLOR,
                               })

header_format = ({
                     'font_size': HEADER_ROW_FONT_SIZE,
                     'bold': True,
                     'color': COLOR_FILE_1,
                     'bg_color': BG_COLOR_FILE_1,
                     'border': 1,
                     'border_color': BORDER_COLOR,
                     'text_wrap': False,
                     'align': 'left',
                     'valign': 'vcenter'
                 },

                 {
                     'font_size': HEADER_ROW_FONT_SIZE,
                     'bold': True,
                     'color': COLOR_FILE_2,
                     'bg_color': BG_COLOR_FILE_2,
                     'border': 1,
                     'border_color': BORDER_COLOR,
                     'text_wrap': False,
                     'align': 'left',
                     'valign': 'vcenter'
                 })
