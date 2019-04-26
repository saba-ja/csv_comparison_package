from chardet.universaldetector import UniversalDetector
from csv_comparison_package.error_handler import AppErrorHandler
from csv_comparison_package.decorator import call_each
from csv_comparison_package import Compare


@call_each
def set_file_encoding(comparable: Compare):
    with open(comparable.file_name, 'rb') as file:
        detector = UniversalDetector()
        for line in file.readlines():
            detector.feed(line)
            if detector.done:
                break
        detector.close()

    if detector.result["confidence"] < 0.5 or \
            detector.result["encoding"] is None:
        raise AppErrorHandler(AppErrorHandler.unknown_encoding)
    else:
        comparable.encoding = detector.result['encoding'].lower()

