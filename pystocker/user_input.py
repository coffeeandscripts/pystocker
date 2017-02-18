#!/usr/bin/env python

"""
Set of functions to correspond to user input
"""

## IMPORTS ##
import curses
import curses.textpad as textpad
import operator
from pystocker import stocks

## FUNCTIONS ##

def cursor_right(cursor, historicals, scr_dim):

    col_list = stocks.get_col_settings()

    stock_list = stocks.open_stock_codes()

    date_list = stocks.generate_date_list(stock_list)

    if cursor[3] == -1 and historicals != 1:
        cursor[3] = 0
    else:
        if cursor[0] < len(date_list) - int(((scr_dim[1] - 10)/12)+1) :
            cursor[0] = cursor[0] + 1

    if historicals != 1:
        if cursor[0] > len(col_list) - 1:
            cursor[0] = len(col_list) - 1

    return cursor

def cursor_left(cursor):
    
    if cursor[0] > 0:
        cursor[0] = cursor[0] - 1
    elif cursor[0] == 0:
        cursor[3] = -1
    else:
        cursor[0] = 0

    return cursor

def cursor_down(cursor, max_stock_range, move_up, scr_dim):

    stock_list = stocks.open_stock_codes()

    if cursor[1] < max_stock_range and cursor[1] == cursor[2]:
        cursor[1] = cursor[1] + 1
        cursor[2] = cursor[1]
    elif move_up == True and cursor[1] >= max_stock_range:
        cursor[1] = cursor[1] - (max_stock_range - cursor[2]) + 1
        cursor[2] = cursor[2] + 1
    elif cursor[1] >= max_stock_range and max_stock_range < scr_dim[0]-6-1:
        cursor[2] = max_stock_range
        cursor[1] = max_stock_range
    elif cursor[1] == len(stock_list):
        pass
    elif cursor[1] >= max_stock_range and cursor[2] == max_stock_range:
        cursor[1] = cursor[1] + 1
    elif cursor[1] > cursor[2]:
        cursor[1] = cursor[1] + 1
        cursor[2] = cursor[2] + 1
    else:
        cursor[1] = 0
        cursor[2] = 0

    return cursor

def cursor_up(cursor, max_stock_range):

    if cursor[1] > max_stock_range and cursor[2] != 1:
        cursor[2] = cursor[2] - 1
    elif cursor[2] == 1 and cursor[1] == max_stock_range + 1:
        cursor[1] = 1
    elif cursor[2] == 1 and cursor[1] > cursor[2] and cursor[1] >= max_stock_range:
        cursor[1] = cursor[1] - (max_stock_range)
    elif cursor[2] == 1 and cursor[1] > cursor[2] and cursor[1] < max_stock_range:
        cursor[1] = cursor[1] - 1
    elif cursor[2] == 1 and cursor[1] == 1:
        cursor[1] = cursor[1] - 1
        cursor[2] = cursor[2] - 1
    else:
        if cursor[1] > 0 and cursor[2] > 0:
            cursor[1] = cursor[1] - 1
            cursor[2] = cursor[2] - 1

    return cursor

def input_n(cursor, scr_bottom, max_stock_range, stock_list, scr_dim):

    stock_input = None
    curses.start_color()
    curses.init_pair(5,curses.COLOR_WHITE,curses.COLOR_BLUE)
    stock_win = curses.newwin(1, 10, scr_dim[0]-1, 0)
    stock_win.bkgd(curses.color_pair(5))
    stock_box = textpad.Textbox(stock_win)
    stock_win.refresh()
    scr_bottom.addstr(0, curses.COLS-20, "   [Enter]Save/Exit")
    scr_bottom.refresh()
    stock_input = stock_box.edit()
    stock_input = stock_input.upper()

    if str(stock_input) != "" and str(stock_input) not in stock_list:
        stocks.add_stock_code(str(stock_input))
        total_stocks = len(stock_list) + 1
        if total_stocks > scr_dim[0] - 6:
            cursor[1] = total_stocks
            cursor[2] = max_stock_range
        else:
            cursor[1] = max_stock_range + 1
            cursor[2] = cursor[1]
    elif str(stock_input) or ((str(stock_input)[0:(len(str(stock_input)) - 2)] and str(stock_input)[len(str(stock_input))])) in stock_list:
        total_stocks = len(stock_list)
        stock_pos = stock_list.index(str(stock_input)) + 1
        cursor[1] = stock_pos
        if total_stocks > max_stock_range:
            cursor[2] = 1
        else:
            cursor[2] = cursor[1]

    return cursor

def sort_data(stock_data_dict, sort_by, sort_order):

    set_up_dict = {}

    for stock in stock_data_dict:
        value_used = stock_data_dict[stock][sort_by]
        if value_used == "N/A":
            value_used == -999999999999
        if sort_by == "ebitda" or sort_by == "market_cap":
            if value_used[-1:] == "B":
                value_used = float(value_used[:-1]) * 1000000000
            elif value_used[-1:] == "M":
                value_used = float(value_used[:-1]) * 1000000
            else:
                value_used = float(value_used[:-1]) * 1000
        try:
            set_up_dict[stock] = float(value_used)
        except:
            set_up_dict[stock] = float(-999999999999)

    sorted_stock_list = []

    if sort_order[2] == 0:
        for key in sorted(set_up_dict, key=set_up_dict.__getitem__):
            sorted_stock_list.append(key)
    elif sort_order[2] == 1:
        for key in sorted(set_up_dict, key=set_up_dict.__getitem__, reverse=True):
            sorted_stock_list.append(key)

    return sorted_stock_list

def sort_stocks(cursor, stock_list, stock_data_dict, sort_order):

    col_list = stocks.get_col_settings()

    original_stock_list = stock_list

    if cursor[3] == -1:
        if sort_order[2] == 0:
            sorted_stock_list = sorted(original_stock_list)
        elif sort_order[2] == 1:
            sorted_stock_list = sorted(original_stock_list, reverse=True)
    else:
        sort_by = col_list[cursor[0]]
        if sort_by == "open":
            sort_by = "open_price"
        if sort_by == "average_daily_volume":
            sort_by = "avg_daily_volume"
        if sort_by == "52_week_high":
            sort_by = "fifty_two_week_high"
        if sort_by == "52_week_low":
            sort_by = "fifty_two_week_low"
        if sort_by ==  "50_day_moving_average":
            sort_by = "fifty_day_moving_avg"
        if sort_by == "200_day_moving_average":
            sort_by = "two_hundred_day_moving_avg"

        sorted_stock_list = sort_data(stock_data_dict, sort_by, sort_order)

    return sorted_stock_list



