def select_format_left_or_bottom(comparable, index):
    if index == 0:
        return comparable.header_format_left_bottom_border
    else:
        return comparable.header_format_bottom_border
