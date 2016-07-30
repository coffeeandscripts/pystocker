#!/usr/bin/env python

"""
Set of functions to correspond to user input
"""

## IMPORTS ##
import curses
import curses.textpad as textpad
from pystocker import stocks

## FUNCTIONS ##

def cursor_right(cursor):

    col_list = stocks.get_col_settings()

    cursor[0] = cursor[0] + 1

    if cursor[0] > len(col_list) - 1:
        cursor[0] = len(col_list) - 1

    return cursor

def cursor_left(cursor):
    
    if cursor[0] > 0:
        cursor[0] = cursor[0] - 1
    else:
        cursor[0] = 0

    return cursor

def cursor_down(cursor, max_stock_range, move_up):

    stock_list = stocks.open_stock_codes()

    if cursor[1] < max_stock_range and cursor[1] == cursor[2]:
        cursor[1] = cursor[1] + 1
        cursor[2] = cursor[1]
    elif move_up == True and cursor[1] >= max_stock_range:
        cursor[1] = cursor[1] - (max_stock_range - cursor[2]) + 1
        cursor[2] = cursor[2] + 1
    elif cursor[1] >= max_stock_range and max_stock_range < curses.LINES-6-1:
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

def input_n(cursor, scr_bottom, max_stock_range, stock_list):

    stock_input = None
    curses.start_color()
    curses.init_pair(5,curses.COLOR_WHITE,curses.COLOR_BLUE)
    stock_win = curses.newwin(1, 10, curses.LINES-1, 0)
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
        if total_stocks > curses.LINES - 6:
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
