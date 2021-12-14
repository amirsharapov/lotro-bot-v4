from sys import argv
from src.exceptions import NoArgsException
from src.agent import cook_ingredient, farm_fields, switch_apps
from tests.tests import run_tests


def setup():
    run_tests()


def run(total: int, batch_count: int):
    switch_apps()
    farm_fields(total, batch_count)


if __name__ == '__main__':
    args = argv[1:]

    count = None
    batch_count = None

    for arg in args:
        if arg.startswith('--count='):
            value = arg.replace('--count=', '')
            value = int(value)
            count = value
        if arg.startswith('--batch_count='):
            value = arg.replace('--batch_count=', '')
            value = int(value)
            batch_count = value
    if batch_count is None:
        print('No \'batch_count\' argument passed. Defaulting to 50')
        batch_count = 200
    
    if count is None:
        raise Exception('You must specify a \'count\' arg (ie: \'python main.py --count=4000\').')

    run(count, batch_count)