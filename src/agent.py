from datetime import datetime
from time import gmtime, sleep, time, strftime
from typing import Any
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


"""Non-VIP Agent"""


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


"""VIP Agent"""


def vip_cook_ingredient(total: int):
    batch_size: int = 999
    batch_count: int = math.floor(total / batch_size)
    leftovers: int = total % batch_size

    log("Stared cooking: Batch size = {} - Batch count = {} - Leftovers = {}".format(
        batch_size, batch_count, leftovers))

    for i in range(1, batch_count + 1):
        vip_make_batch(batch_size, i)
    vip_make_batch(batch_size, 'Leftovers')


def vip_process_crops(total: int):
    batch_size: int = 999
    batch_count: int = math.floor(total / batch_size)
    leftovers: int = total % batch_size

    log("Stared processing: Batch size = {} - Batch count = {} - Leftovers = {}".format(
        batch_size, batch_count, leftovers))

    for i in range(1, batch_count + 1):
        vip_make_batch(batch_size, i)
    vip_make_batch(batch_size, 'Leftovers')


def vip_make_batch(size: int, batch: Any = 'N/A'):

    click_make_all_button()
    minimize_lotro()

    for j in range(1, size + 1):
        log('Making item: (BATCH: {} - ITEM: {})'.format(batch, j))
        sleep(1.03)
    sleep(10)

    maximize_lotro()


def vip_farm(total: int, batch_size=5):
    log('VIP Farming started: Total: {} - Batch Size = {}'.format(total, batch_size))
    batches = math.floor(total / batch_size)
    leftover_batch_size = total % batch_size

    for i in range(1, batches + 1):
        log('Farming VIP batch: Batch: {}...'.format(i))
        vip_farm_batch(i, batch_size)
    log('Farming VIP Leftover batch...')
    vip_farm_batch(i, leftover_batch_size)


def vip_farm_batch(batch: int, batch_size: int):

    for _ in range(batch_size - 1):
        t = random_time(3, 1)
        click_quantity_increment_arrow(False)
        random_delay(t)

    t = random_time(batch_size * 1100, 250)
    click_make_button()

    log('Planting batch: {}'.format(batch))
    
    minimize_lotro()

    random_delay(t)

    maximize_lotro()

    for _ in range(batch_size):
        select_next_item()
        use_selection()
    
    log('Harvesting batch: {}'.format(batch))

    minimize_lotro()

    random_delay(random_time(batch_size * 2250))

    maximize_lotro()
