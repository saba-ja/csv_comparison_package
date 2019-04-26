import os


def extract_file_name_from_path(comparable, truncate=True):
    _, f1_name = os.path.split(comparable.file_name)
    invalid_chars = [".", "\\", "/", " ", "\n", "\t", ":", "*", "?", "\"", "'", "<", ">", "|"]
    if truncate:
        f1_name = f1_name[0:15]
    for char in invalid_chars:
        f1_name = f1_name.replace(char, "_")
    return f1_name
