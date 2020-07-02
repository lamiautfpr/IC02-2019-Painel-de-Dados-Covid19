from datetime import datetime, timedelta


def now():
    now = datetime.now()
    return now


def format_date(date):
    date = date.strftime('%d_%m_%Y')
    return date


def previous_date(date):
    date -= timedelta(days=1)
    return date
