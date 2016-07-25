#!/usr/bin/env python

"""
Set of functions to correspond to user input
"""

## IMPORTS ##
import curses
import ystockquote

import stocks

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

def cursor_down(cursor):

    stock_list = stocks.open_stock_codes()

    cursor[1] = cursor[1] + 1

    if cursor[1] > len(stock_list) + 1:
        cursor[1] = len(stock_list) + 1

    return cursor

def cursor_up(cursor):

    if cursor[1] > 0:
        cursor[1] = cursor[1] - 1
    else:
        cursor[1] = 0

    return cursor
