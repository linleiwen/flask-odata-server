import pandas as pd
from dateparser import parse
from datetime import datetime

def read_csv_to_df(filepath_or_buffer):
    return pd.read_csv(filepath_or_buffer=filepath_or_buffer)

def datetime_to_unix_time(date_time):
    if isinstance(date_time, str):
        date_time = parse(date_time)
    elif isinstance(date_time, datetime):
        pass
    else:
        raise TypeError(f"Unsupported type {type(date_time)}")
    return int(date_time.timestamp())