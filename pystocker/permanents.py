#!/usr/bin/env python

"""

"""

## IMPORTS ##
import curses
import os
from pystocker import ystockquote
from pystocker import stocks

root_path = os.path.expanduser("~")

## FUNCTIONS ##

def get_perm_list():

    perm_list = []
    row1_list = []
    row2_list = []
    row3_list = []

    with open(root_path + "/.pystocker/permanents/perm_l1", "r") as f:
        for line in f:
            row1_list.append(line.rstrip('\n'))
    f.close()
    perm_list.append(row1_list)

    with open(root_path + "/.pystocker/permanents/perm_l2", "r") as f:
        for line in f:
            row2_list.append(line.rstrip('\n'))
    f.close()
    perm_list.append(row2_list)

    with open(root_path + "/.pystocker/permanents/perm_l3", "r") as f:
        for line in f:
            row3_list.append(line.rstrip('\n'))
    f.close()
    perm_list.append(row3_list)

    return perm_list

def get_permanents(perm):

    got_data = False

    while got_data == False:
        try:
            data = ystockquote.get_all(str(perm))
            got_data = True
        except:
            got_data = False

    return data

def prep_perm_dict(perm, perm_data, perm_data_dict, row):

    perm_data_dict[row][str(perm)] = perm_data

    return perm_data_dict

def write_perm_data(perm_data_dict):

    with open(root_path + "/.pystocker/permanents/perm_data", "w") as f:
        f.write(str(perm_data_dict))
    f.close()


def read_perm_data():

    try:
        with open(root_path + "/.pystocker/permanents/perm_data", "r") as f:
            perm_data_dict = eval(f.read())
    except:
        perm_data_dict = []

    return perm_data_dict

def print_permanents(scr_top, perm, row, col, perm_data, scr_dim):

    if perm == "GC=F":
        perm = "Gold"
    elif perm == "SI=F":
        perm = "Silver"
    elif perm == "HG=F":
        perm = "Copper"
    elif perm == "CL=F":
        perm = "Crude"
    elif perm[-2:] == "=X":
        perm = perm[0:3] + "/" + perm[3:6]
    elif perm[0] == "^":
        perm = perm[1:]

    curses.start_color()

    curses.init_pair(20, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(21, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(22, curses.COLOR_RED, curses.COLOR_BLACK)

    printing_perm = str(perm) + "=" + str(perm_data["price"])

    perm_length = len(printing_perm) + 1
    
    if perm_length+col < scr_dim[1]:
        if perm_data["change"] != "N/A":
            if float(perm_data["change"]) >= 0.5:
                scr_top.addstr(1+row, col, str(printing_perm), curses.color_pair(20))
            if float(perm_data["change"]) <= -0.5:
                scr_top.addstr(1+row, col, str(printing_perm), curses.color_pair(22))
            else:
                scr_top.addstr(1+row, col, str(printing_perm), curses.color_pair(21))
        else:
            scr_top.addstr(1+row, col, str(printing_perm))

    return perm_length
