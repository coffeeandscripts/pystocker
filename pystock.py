#!/usr/bin/env python

## IMPORTS ##
import curses
import ystockquote

## GLOBALS ##
x = 1

## FUNCTIONS ##
#initialize the curses window and return scr
def init_scr():
    
    scr = curses.initscr()

    curses.noecho()
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

## WORKFLOW ##
scr = init_scr()

#main loop
while x != ord("0"):
    scr.refresh()
    x = scr.getch()

#terminating the window
term_scr(scr)
