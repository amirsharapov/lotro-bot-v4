import sys
from sys import argv
from src.logging import log
from src.controls import maximize_lotro, minimize_lotro

from src.agent import cook_ingredient, farm_fields, process_crops, vip_cook_ingredient, vip_farm_fields, vip_process_crops
from tests.tests import run_tests


def setup():
    run_tests()


def try_find_action_arg(args: list[str]):
    if '--farm' in args or '-f' in args:
        return farm
    if '--cook' in args or '-c' in args:
        return cook
    if '--process' in args or '-p' in args:
        return process
    
    log('Action not defined. Exiting program...')
    sys.exit(1)


def try_find_vip_arg(args: list[str]):
    vip_status = '-v' in args or '--vip' in args
    if not vip_status:
        log('Vip status not defined. Defaulting to false')
    return vip_status


def try_find_total_arg(args: list[str]):
    if '-t' in args:
        i = args.index('-t')
        v = args[i + 1]
        return int(v)
    
    if '--total' in args:
        i = args.index('--total')
        v = args[i + 1]
        return int(v)
    
    log('Total not specified. Exiting program...')
    sys.exit(1)


def try_find_batch_size_arg(args: list[str]):
    if '-bs' in args:
        i = args.index('-bs')
        v = args[i + 1]
        return int(v)
    
    if '--batch-size' in args:
        i = args.index('--batch-size')
        v = args[i + 1]
        return int(v)
    
    log('Batch size not specified. Defaulting to action specific')
    return None


def farm(vip: bool, total: int, batch_size: int = None):
    if vip: vip_farm_fields(total, batch_size or 5)
    else: farm_fields(total, batch_size or 45)


def cook(vip: bool, total: int, batch_size: int = None):
    if vip: vip_cook_ingredient(total, batch_size or 999)
    else: cook_ingredient(total, batch_size or 200)


def process(vip: bool, total: int, batch_size: int = None):
    if vip: vip_process_crops(total, batch_size or 999)
    else: process_crops(total, batch_size or 200)


def main():
    log('Running command: python {}'.format(' '.join(argv)))
    args = argv[1:]

    action = None
    vip = None
    total = None
    batch_size = None

    action = try_find_action_arg(args)
    vip = try_find_vip_arg(args)
    total = try_find_total_arg(args)
    batch_size = try_find_batch_size_arg(args)

    maximize_lotro()
    action(vip, total, batch_size)
    minimize_lotro()
    

if __name__ == '__main__':
    main()
