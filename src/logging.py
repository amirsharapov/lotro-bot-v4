import os
from src.utils import timestamp, today
from src.constants import *


def log(message: str):
    path = build_log_file()
    content = format_message(DEFAULT_LOG_LEVEL, message)
    
    print(content)

    append_to_file(path, content)


def append_to_file(path: str, content: str):
    with open(path, 'a') as f:
        content += '\n'
        f.write(content)


def format_message(level: str, message: str):
    formatted = ''
    ts = timestamp()

    ts_padding = 20
    ts_padded = pad_string(ts, ts_padding)
    formatted += ts_padded

    level_padding = 10
    level_padded = pad_string(level, level_padding)
    formatted += level_padded
    
    message_padding = 110
    message_padded = pad_string(message, message_padding, pad_end_with_space=False)
    formatted += message_padded

    return formatted


def pad_string(string: str, num: int, char: str='.', pad_end_with_space=True):
    char = char[:1]

    if num < len(string):
        return truncate_string(string, num - 3, 3)

    padding_count = num - len(string)
    if pad_end_with_space: padding_count -= 1
    padding = padding_count * char
    if pad_end_with_space: padding += ' '

    return '{}{}'.format(string, padding)


def truncate_string(string: str, cutoff:int, num: int, char: str='.'):
    truncated = string[:cutoff]
    truncation = char * num

    return '{}{}'.format(truncated, truncation)


def build_log_file():
    if not os.path.isdir(DEFAULT_LOG_DIRECTORY):
        os.mkdir(DEFAULT_LOG_DIRECTORY)
    
    file_name = today()
    return 'logs/{}.log'.format(file_name)