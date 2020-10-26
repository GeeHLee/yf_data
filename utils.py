import datetime

def diff_seconds(date_now):
    date_init = datetime.date(1970, 1, 1)
    return int((date_now - date_init).total_seconds())