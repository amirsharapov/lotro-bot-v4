from datetime import datetime
from src.constants import *


def today(now: datetime=None):
    now = now if now else datetime.now()
    return now.strftime(TODAY_FORMAT)


def timestamp(now: datetime=None):
    now = now if now else datetime.now()
    return now.strftime(TIMESTAMP_FORMAT)