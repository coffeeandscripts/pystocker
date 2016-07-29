#!/usr/bin/env python

"""
Loop in the background to pull data.
"""

## IMPORTS ##
import ystockquote
import curses
import os

#user generated imports
import stocks
import permanents

## CLASSES ##

root_path = os.path.expanduser("~")

## FUNCTIONS ##
# open file to write the dictionary (may edit in future as JSON format)
def prepare_stock_dict(stock, data, stock_data_dict):
    
    stock_data_dict[str(stock)] = data

    return stock_data_dict

def write_stock_data(stock_data_dict):
    with open(root_path + "/.pystocker/stock_data", "w") as f:
        f.write(str(stock_data_dict))
    f.close()


## WORKFLOW ##

os.chdir(root_path)

x = 1

stock_data_dict = {}

row1 = {}
row2 = {}
row3 = {}

perm_data_dict = [row1, row2, row3]

while x == 1:
    stock_list = []
    stock_list = stocks.open_stock_codes()
    stock_data_dict.clear()

    for stock in stock_list:
        data = stocks.fetch_stock_data(str(stock))
        stock_data_dict = prepare_stock_dict(stock, data, stock_data_dict)

    write_stock_data(stock_data_dict)

    permanents_list = permanents.get_perm_list()
    
    counter = 0

    for row in permanents_list:
        for perm in row:
            perm_data = permanents.get_permanents(perm)
            perm_data_dict = permanents.prep_perm_dict(perm, perm_data, perm_data_dict, counter)
        counter = counter + 1

    permanents.write_perm_data(perm_data_dict)
