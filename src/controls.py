from random import Random
from time import sleep
from src.logging import log
from src.constants import *
import pydirectinput
import pyautogui
import win32gui
import win32con


random = Random()

"""Random controls
"""


def random_coords(rect: tuple[int], padding: int = 5) -> tuple[int]:
    x, y, w, h = rect

    x_lower = x + padding
    x_upper = x - padding + w
    y_lower = y + padding
    y_upper = y - padding + h

    rx = random.randint(x_lower, x_upper)
    ry = random.randint(y_lower, y_upper)

    return (rx, ry)


def random_time(target_ms: int = 300, margin_ms: int = 250) -> float:
    t_lower = target_ms - margin_ms
    t_upper = target_ms + margin_ms

    time = random.randint(t_lower, t_upper) / 1000

    return time


def random_delay(delay: float = None) -> float:
    delay = random_time() if not delay else delay
    sleep(delay)
    return delay


"""Mouse controls
"""


def click_rect(rect, delay: bool = True):
    x, y = random_coords(rect)
    duration = random_time()

    click_coords(x, y, duration, delay)


def click_coords(x, y, duration, delay: bool = True):
    pyautogui.moveTo(x, y, duration)
    pydirectinput.click()
    if delay:
        random_delay()


"""Keyboard controls
"""


def press(key, delay: bool = True):
    pydirectinput.press(key)
    if delay:
        random_delay()


def keyUp(key, delay: bool = True):
    pydirectinput.keyUp(key)
    if delay:
        random_delay()


def keyDown(key, delay: bool = True):
    pydirectinput.keyDown(key)
    if delay:
        random_delay()


def hotkey(keys: list[str], delay: bool = True):
    for key in keys:
        keyDown(key)
        sleep(.05)

    for key in reversed(keys):
        keyUp(key)
        sleep(.05)

    if delay:
        random_delay()


"""System controls
"""


def get_lotro_hwnd():
    hwnd = win32gui.FindWindow(None, LOTRO_WINDOW_NAME)
    print(hwnd)


def minimize_lotro():
    hwnd = get_lotro_hwnd()
    win32gui.ShowWindow(hwnd, win32con.SW_FORCEMINIMIZE)


def maximize_lotro():
    hwnd = get_lotro_hwnd()
    win32gui.ShowWindow(hwnd, win32con.SW_SHOWMAXIMIZED)


"""Character controls
"""


def move_forward(time: float):
    log('Moving forward for {} seconds'.format(time))
    keyDown(MOVE_FORWARD_KEY, False)
    sleep(time)
    keyUp(MOVE_FORWARD_KEY)


def move_backward(time: int):
    log('Moving backward for {} seconds'.format(time))
    keyDown(MOVE_BACKWARD_KEY, False)
    sleep(time)
    keyUp(MOVE_BACKWARD_KEY)


def turn_left(time: int):
    log('Turning left for {} seconds'.format(time))
    keyDown(TURN_LEFT_KEY, False)
    sleep(time)
    keyUp(TURN_LEFT_KEY)


def turn_right(time: int):
    log('Turning right for {} seconds'.format(time))
    keyDown(TURN_RIGHT_KEY, False)
    sleep(time)
    keyUp(TURN_RIGHT_KEY)


def jump():
    press('space')
    t = random_time(1250, 500)
    random_delay(t)
    log('Jumped!')


def select_nearest_item(delay: bool = True):
    log('Selecting nearest item')
    hotkey(SELECT_NEAREST_ITEM_HOTKEY, delay)


def select_next_item(delay: bool = True):
    log('Selecting next item')
    hotkey(SELECT_NEXT_ITEM_HOTKEY, delay)


def select_nearest_npc(delay: bool = True):
    log('Selecting nearest NPC')
    hotkey(SELECT_NEAREST_NPC_HOTKEY, delay)


def select_next_npc(delay: bool = True):
    log('Selecting next NPC')
    hotkey(SELECT_NEXT_NPC_HOTKEY, delay)


def use_selection(delay: bool = True):
    log('Using selection')
    press(USE_SELECTION_KEY, delay)


def click_browse_the_shop_interaction(delay: bool = True):
    log('Clicking the browse the shop interaction')
    click_rect(BROWSE_THE_SHOP_RECT, delay)


def click_make_button(delay: bool = True):
    log('Clicking make button')
    click_rect(MAKE_BUTTON, delay)


def click_make_all_button(delay: bool = True):
    log('Clicking make all button')
    click_rect(MAKE_ALL_BUTTON, delay)


def click_repair_tab(delay: bool = True):
    log('Clicking repair tab')
    click_rect(REPAIR_TAB, delay)


def click_repair_all_button(delay: bool = True):
    log('Clicking repair all button')
    click_rect(REPAIR_ALL_BUTTON, delay)


"""Util controls
"""


def switch_apps(delay: bool=True):
    keyDown('alt', False)
    press('tab', False)
    keyUp('alt', False)
    
    if delay:
        t = random_time(100, 50)
        random_delay(t)
