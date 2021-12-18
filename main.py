from sys import argv
from time import sleep
from src.logging import log
from src.controls import maximize_lotro, minimize_lotro

from src.exceptions import NoArgsException
from src.agent import cook_ingredient, farm_fields, switch_apps, vip_cook_ingredient, vip_farm, vip_process_crops
from tests.tests import run_tests


def setup():
    run_tests()

def main():
    log('Running command: {}'.format(argv))
    args = argv[1:]

    total = None
    batch_count = None

    for arg in args:
        if arg.startswith('--total='):
            value = arg.replace('--total=', '')
            value = int(value)
            total = value
        if arg.startswith('--batch_count='):
            value = arg.replace('--batch_count=', '')
            value = int(value)
            batch_count = value
    if batch_count is None:
        print('No \'batch_count\' argument passed. Defaulting to 50')
        batch_count = 200
    
    if total is None:
        raise Exception('You must specify a \'total\' arg (ie: \'python main.py --total=4000\').')

    maximize_lotro()
    vip_farm(total, batch_count or 5)
    minimize_lotro()
    

if __name__ == '__main__':
    main()
