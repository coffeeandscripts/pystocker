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

    scr.refresh()

    if option_window_open == True:
        win.refresh()

    x = scr.getch()

#terminating the window
term_scr(scr)
