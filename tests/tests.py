from src.constants import *
from src.controls import *
from src.exceptions import *
import pyautogui


def run_tests():
    print('Testing buttons...')

    interaction_rects = [
        MAKE_ALL_BUTTON,
        REPAIR_ALL_BUTTON,
        REPAIR_TAB
    ]

    for rect in interaction_rects:
        test = [k for k, v in globals().items() if v == rect][0]
        print('Test: {}'.format(test))
        test_rect(rect, test)
    
    print('Testing complete! Have fun automating!')


def test_rect(rect: tuple[int], test: str):
    x, y, w, h = rect

    print('Testing x, y')
    pyautogui.moveTo(x, y, duration=random_time())
    assert_passing(test)

    print('Testing x + w, y + h')
    pyautogui.moveTo(x + w, y + h)
    assert_passing(test)


def assert_passing(test: str):
    x: str = input('Does this pass the test - {}? (y / n)\n'.format(test))
    if x.lower() == 'n':
        handle_failed_test()


def handle_failed_test():
    raise TestFailedException()