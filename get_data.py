#!/usr/bin/env python

"""
Loop in the background to pull data.
"""

## IMPORTS ##
import ystockquote
import curses

#user generated imports
import stocks

## CLASSES ##

## FUNCTIONS ##
# open file to write the dictionary (may edit in future as JSON format)
def prepare_stock_dict(stock, data, stock_data_dict):
    
    stock_data_dict[str(stock)] = data

    return stock_data_dict

def write_stock_data(stock_data_dict):
    with open("stock_data", "w") as f:
        f.write(str(stock_data_dict))
    f.close()


## WORKFLOW ##

x = 1

while x == 1:
    stock_list = []
    stock_list = stocks.open_stock_codes()
    stock_data_dict = {}

    for stock in stock_list:
        data = stocks.fetch_stock_data(str(stock))
        prepare_stock_dict(stock, data, stock_data_dict)

    write_stock_data(stock_data_dict)
