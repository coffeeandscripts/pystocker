#!/usr/bin/env python

"""
Gives general functionality of the curses application
"""

## IMPORTS ##
import curses
import ystockquote
import os
import subprocess

#user created imports
import stocks
import user_input

## GLOBALS ##
x = 1
term_size_change = False
option_window_open = False

## FUNCTIONS ##
#initialize the curses window and return scr
def init_scr():
    
    scr = curses.initscr()

    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    curses.halfdelay(5)
    scr.keypad(True)
    scr.clear()    

    return scr

#user scr to terminate the window and revert back to terminal
def term_scr(scr):

    curses.nocbreak()
    scr.keypad(False)
    curses.echo()
    curses.endwin()

#returns the number of columns or rows
def get_scr_dim(scr):
    return scr.getmaxyx()

#returns True if there has been a change in the window size, otherwise False
def check_term_size_change(scr, scr_dim):
    
    change = False

    if scr_dim != scr.getmaxyx():
        change = True

    return change

#opens a window that is 2/3 the size of the screen horizontally and vertically
def open_option_window(scr_dim):
    
    win = curses.newwin(int((int(scr_dim[0]) * 2 / 3)), int((int(scr_dim[1]) * 2 / 3)), int((int(scr_dim[0]) / 6) - 1), int((int(scr_dim[1]) / 6) - 1))

    return win

#creates the windows at the top, left and main segments
def open_top(scr_dim):
    
    top_scr = curses.newwin(4, scr_dim[1], 0, 0)

    return top_scr

def open_left(scr_dim):

    left_scr = curses.newwin(scr_dim[0]-5-1, 10, 5, 0)

    return left_scr

def open_main(scr_dim):

    main_scr = curses.newwin(scr_dim[0]-5-1, scr_dim[1]-10, 5, 10)

    return main_scr

def open_strip(scr_dim):

    strip_scr = curses.newwin(1, scr_dim[1], 4, 0)

    return strip_scr

def open_bottom(scr_dim):

    bottom_scr = curses.newwin(1, scr_dim[1], scr_dim[0]-1, 0)

    return bottom_scr

def window_colors(scr_top, scr_strip, scr_left, scr_main, scr_bottom):

    curses.start_color()

    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_BLUE)
    curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_RED)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_GREEN)
    curses.init_pair(4,curses.COLOR_WHITE,curses.COLOR_MAGENTA)

    scr_top.bkgd(curses.color_pair(1))
    scr_strip.bkgd(curses.color_pair(4))
    scr_left.bkgd(curses.color_pair(2))
    scr_main.bkgd(curses.color_pair(3))
    scr_bottom.bkgd(curses.color_pair(4))

#refreshes the visible windows in order
def refresh_windows(scr_top, scr_strip, scr_left, scr_main, scr_bottom):

    scr_top.refresh()
    scr_strip.refresh()
    scr_left.refresh()
    scr_main.refresh()
    scr_bottom.refresh()


## WORKFLOW ##
scr = init_scr()
scr_dim = get_scr_dim(scr)

cursor = [0, 0]
stock_data_dict = {}

subprocess.Popen(["python", "get_data.py"])

#main loop
while x != ord("0"):

    if x == 261:
        cursor = user_input.cursor_right(cursor)
    elif x == 260:
        cursor = user_input.cursor_left(cursor)
    elif x == 258:
        cursor = user_input.cursor_down(cursor)
    elif x == 259:
        cursor = user_input.cursor_up(cursor)

    term_size_change = check_term_size_change(scr, scr_dim)

    if term_size_change == True:
        term_scr(scr)
        scr = init_scr()
        scr_dim = get_scr_dim(scr)
        win = open_option_window(scr_dim)
        term_size_change == False

    scr_dim = get_scr_dim(scr)

    if x == ord("9"):
        option_window_open = True
        win = open_option_window(scr_dim)

    if option_window_open == True:
        win.border(0)

    scr_top = open_top(scr_dim)
    scr_left = open_left(scr_dim)
    scr_main = open_main(scr_dim)
    scr_strip = open_strip(scr_dim)
    scr_bottom = open_bottom(scr_dim)

    window_colors(scr_top, scr_strip, scr_left, scr_main, scr_bottom)

    if option_window_open == True:
        win.refresh()

    stock_list = stocks.open_stock_codes()

    total_stock_count = len(stock_list)
    
    all_stock_data_dict = stocks.get_all_data(stock_data_dict)

    counter = 0
    stock_data = {}

    for stock in stock_list:
        data = all_stock_data_dict[str(stock)]
        stock_data[str(stock)] = stocks.Stock(str(stock), data)
        stocks.print_data(counter, stock_data[str(stock)], scr_left, scr_main, scr_strip, x, cursor)
        counter = counter + 1

    refresh_windows(scr_top, scr_strip, scr_left, scr_main, scr_bottom)

    scr_top.addstr(1, 1, str(x))
    
    scr_top.refresh()

    x = scr.getch()

#terminating the window
term_scr(scr)
