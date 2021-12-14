from datetime import datetime
from time import gmtime, sleep, time, strftime
from src.logging import log
from src.controls import *
from src.constants import *
import math

time_started = None

total_farmed = 0
total_to_farm = None

total_made = 0
total_to_make = None

total_processed = 0
total_to_process = None


def cook_ingredient(total: int, batch_count: int = 200):
    message = 'Cooking ingredients. Total: {} - Batch count: {}'.format(
        total, batch_count)
    log(message)

    batches = math.floor(total / batch_count)
    leftover = total % batch_count

    for _ in range(batches):
        make_batch_all(batch_count, COOKING_INGREDIENT_INDUCTION)
    make_batch_all(leftover, COOKING_INGREDIENT_INDUCTION)


def process_crops(total: int, batch_count: int = 200):
    message = 'Processing crops. Total: {} - Batch count: {}'.format(
        total, batch_count)
    log(message)

    batches = math.floor(total / batch_count)
    leftover = total % batch_count

    for _ in range(batches):
        make_batch_all(batch_count, COOKING_INGREDIENT_INDUCTION)
    make_batch_all(leftover, COOKING_INGREDIENT_INDUCTION)


def farm_fields(total: int, batch_count: int = 45):
    global total_to_farm, time_started
    total_to_farm = total
    time_started = time()

    message = 'Farming fields. Total: {} - Batch count: {}'.format(
        total, batch_count)
    log(message)

    batches = math.floor(total / batch_count)
    leftover = total % batch_count

    for _ in range(batches):
        farm_batch(batch_count)
    farm_batch(leftover)


def farm_batch(batch_count: int):
    global total_farmed
    global total_to_farm
    global time_started

    for i in range(1, batch_count + 1):
        click_make_button()
        log('Planting crop in batch: ({} / {})'.format(i, batch_count))

        switch_apps()

        delay = random_time(PLANTING_CROP_INDUCTION * 1000 + 400, 200)
        log('Random delay for planting crops: {}'.format(delay))
        random_delay(delay)

        switch_apps()

        select_nearest_item(False)
        delay = random_time(50, 25)
        log('Random delay after selecting nearest item: {}'.format(delay))
        random_delay(delay)

        use_selection(False)
        log('Harvesting crop in batch: ({} / {})'.format(i, batch_count))

        switch_apps()

        delay = random_time(HARVESTING_CROP_INDUCTION * 1000 + 200, 200)
        log('Random delay for harvesting crops: {}'.format(delay))
        random_delay(delay)

        switch_apps()

        current_time = time()
        time_elapsed = gmtime(current_time - time_started)
        time_elapsed = strftime('%T', time_elapsed)
        total_farmed += 1
        log('Total crops farmed: ({} / {}). Time elapsed since start: {}'.format(
            total_farmed, total_to_farm, time_elapsed))

    select_nearest_npc()
    use_selection()

    delay = random_time(2000, 250)
    random_delay(delay)

    click_browse_the_shop_interaction()
    click_repair_tab()
    click_repair_all_button()

    press('esc', False)
    press('esc', False)
    press('t')

    delay = random_time(1500, 250)
    move_backward(delay)


def make_batch_all(batch_count: int, induction: int):
    click_make_all_button()
    switch_apps()
    for i in range(1, batch_count + 1):
        sleep(induction)
        log('Another one: {}'.format(i))
    switch_apps()
    jump()
    click_repair_all_button()


def make_batch_one(batch_count: int, induction: int):
    for i in range(1, batch_count + 1):
        click_make_button()
        sleep(induction)
        log('Another one: {}'.format(i))


def switch_apps():
    keyDown('alt', False)
    press('tab', False)
    keyUp('alt', False)
