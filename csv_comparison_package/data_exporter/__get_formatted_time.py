import datetime


def get_formatted_time():
    now = datetime.datetime.now()
    return f"{now.year:04d}_{now.month:02d}_{now.day:02d}" \
           f"_{now.hour:02d}h_{now.minute:02d}m_{now.second:02d}s" \
           f"_{(now.microsecond/10000):04.0f}ms"
