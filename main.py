from src.agent import cook_ingredient, farm_fields, switch_apps
from tests.tests import run_tests


def setup():
    run_tests()


def run():
    switch_apps()
    farm_fields(3841, 50)


if __name__ == '__main__':
    run()