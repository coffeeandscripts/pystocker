#!/usr/bin/env python

## IMPORTS ##
import curses
import ystockquote

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

    left_scr = curses.newwin(scr_dim[0]-5, 10, 5, 0)

    return left_scr

def open_main(scr_dim):

    main_scr = curses.newwin(scr_dim[0]-5, scr_dim[1]-10, 5, 10)

    return main_scr

def open_strip(scr_dim):

    strip_scr = curses.newwin(1, scr_dim[1], 4, 0)

    return strip_scr

def window_colors(scr_top, scr_strip, scr_left, scr_main):

    curses.start_color()

    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_BLUE)
    curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_RED)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_GREEN)
    curses.init_pair(4,curses.COLOR_WHITE,curses.COLOR_MAGENTA)

    scr_top.bkgd(curses.color_pair(1))
    scr_strip.bkgd(curses.color_pair(4))
    scr_left.bkgd(curses.color_pair(2))
    scr_main.bkgd(curses.color_pair(3))

#refreshes the visible windows in order
def refresh_windows(scr_top, scr_strip, scr_left, scr_main):

    scr_top.refresh()
    scr_strip.refresh()
    scr_left.refresh()
    scr_main.refresh()


## WORKFLOW ##
scr = init_scr()
scr_dim = get_scr_dim(scr)

#main loop
while x != ord("0"):

    term_size_change = check_term_size_change(scr, scr_dim)

    if term_size_change == True:
        term_scr(scr)
        scr = init_scr()
        scr_dim = get_scr_dim(scr)
        win = open_option_window(scr_dim)
        term_size_change == False

    scr_dim = get_scr_dim(scr)
    scr.clear()

    if x == ord("9"):
        option_window_open = True
        win = open_option_window(scr_dim)

    if option_window_open == True:
        win.border(0)

    scr_top = open_top(scr_dim)
    scr_left = open_left(scr_dim)
    scr_main = open_main(scr_dim)
    scr_strip = open_strip(scr_dim)

    window_colors(scr_top, scr_strip, scr_left, scr_main)

    scr.refresh()
    refresh_windows(scr_top, scr_strip, scr_left, scr_main)

    if option_window_open == True:
        win.refresh()

    x = scr.getch()

#terminating the window
term_scr(scr)
