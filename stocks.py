#!/usr/bin/env python

"""
Functions for management of the data and stock information. General classes.
"""

## IMPORTS ##
import curses
import ystockquote

## GLOBALS ##


## CLASSES ##
#custom class for each stock
class Stock:

    historical_prices = []

    def __init__(self, code, data):
        self.code = code
        self.stock_exchange = data['stock_exchange']
        self.price = data['price']
        self.change = data['change']
        self.volume = data['volume']
        self.avg_daily_volume = data['avg_daily_volume']
        self.market_cap = data['market_cap']
        self.book_value = data['book_value']
        self.ebitda = data['ebitda']
        self.dividend_per_share = data['dividend_per_share']
        self.dividend_yield = data['dividend_yield']
        self.earnings_per_share = data['earnings_per_share']
        self.fifty_two_week_high = data['fifty_two_week_high']
        self.fifty_two_week_low = data['fifty_two_week_low']
        self.fifty_day_moving_avg = data['fifty_day_moving_avg']
        self.two_hundred_day_moving_avg = data['two_hundred_day_moving_avg']
        self.price_earnings_ratio = data['price_earnings_ratio']
        self.price_earnings_growth_ratio = data['price_earnings_growth_ratio']
        self.price_sales_ratio = data['price_sales_ratio']
        self.price_book_ratio = data['price_book_ratio']
        self.short_ratio = data['short_ratio']
        self.open = data['open_price']

## FUNCTIONS ##
def add_stock_code(stock_input):

    with open("stock_codes", "a") as f:
        f.write("\n" + str(stock_input))
    f.close()

#opens a file called stock_codes and returns each line into an array
def open_stock_codes():
    
    stock_list = []

    with open("stock_codes", "r") as f:
        for line in f:
            stock_list.append(line.rstrip('\n'))

        f.close()

    return stock_list

def fetch_stock_data(code):
    
    got_data = False

    while got_data == False:
        try:
            got_data = True
            data_array = ystockquote.get_all(str(code))
        except:
            got_data = False

    return data_array

def get_all_data(stock_data_dict):

    try:
        stock_data_dict.clear()
        with open("stock_data", "r") as f:
            stock_data_dict = eval(f.read())
    except:
        pass

    return stock_data_dict

def get_col_settings():

    col_list = []

    with open("info_settings", "r") as f:
        for line in f:
            col_list.append(line.rstrip('\n'))

        f.close()
    
    remove_col_list = []

    for info in col_list:
        if info[0] == "#":
            remove_col_list.append(info)

    for info in remove_col_list:
        col_list.remove(info)

    return col_list


def print_stock_data(col, row, data, title, scr_main, scr_strip, cursor_row):

    scr_strip.addstr(0, col+10, title)

    data_length = len(str(data))
    spaces_length = 9 - data_length
    n = 0

    if col+10+18 > curses.COLS:
        spaces_length = spaces_length + curses.COLS - col-10-9

    while n < spaces_length:
        data = data + " "
        n = n + 1
    if cursor_row == 1:
        scr_main.addstr(row, col, data, curses.A_REVERSE)
    else:
        scr_main.addstr(row, col, data)

def print_data(n, data, scr_left, scr_main, scr_strip, x, cursor):

    col_list = get_col_settings()
    remove_col_list = []

    w = 9

    counter = 0

    cursor_row = 0

    count = cursor[0]
    
    scr_main.addstr(10, 10, str(cursor))

    stock_code = data.code

    stock_code_width_less = 10 - len(stock_code)

    for x in range(stock_code_width_less):
        stock_code = stock_code + " "
    
    if cursor[1] == (n + 1):
        scr_left.addstr(n, 0, stock_code, curses.A_REVERSE)
    else:
        scr_left.addstr(n, 0, stock_code)

    for info in col_list[cursor[0]:]:
        if counter*w+10+w > curses.COLS:
            break

        if cursor[1] == (n + 1):
            cursor_row = 1

        if info == "price":
            print_stock_data(counter*w, n, data.price, "Price", scr_main, scr_strip, cursor_row)
        elif info == "open":
            print_stock_data(counter*w, n, data.open, "Open", scr_main, scr_strip, cursor_row)
        elif info == "change":
            print_stock_data(counter*w, n, data.change, "Change", scr_main, scr_strip, cursor_row)
        elif info == "volume":
            print_stock_data(counter*w, n, data.volume, "Volume", scr_main, scr_strip, cursor_row)
        elif info == "average_daily_volume":
            print_stock_data(counter*w, n, data.avg_daily_volume, "AvgVol", scr_main, scr_strip, cursor_row)
        elif info == "ebitda":
            print_stock_data(counter*w, n, data.ebitda, "ebitda", scr_main, scr_strip, cursor_row)
        elif info == "market_cap":
            print_stock_data(counter*w, n, data.market_cap, "MktCap", scr_main, scr_strip, cursor_row)
        elif info == "book_value":
            print_stock_data(counter*w, n, data.book_value, "BookVal", scr_main, scr_strip, cursor_row)
        elif info == "dividend_per_share":
            print_stock_data(counter*w, n, data.dividend_per_share, "Div/Sh", scr_main, scr_strip, cursor_row)
        elif info == "dividend_yield":
            print_stock_data(counter*w, n, data.dividend_yield, "DivYld", scr_main, scr_strip, cursor_row)
        elif info == "earnings_per_share":
            print_stock_data(counter*w, n, data.earnings_per_share, "Earn/Sh", scr_main, scr_strip, cursor_row)
        elif info == "52_week_high":
            print_stock_data(counter*w, n, data.fifty_two_week_high, "52wHigh", scr_main, scr_strip, cursor_row)
        elif info == "52_week_low":
            print_stock_data(counter*w, n, data.fifty_two_week_low, "52wLow", scr_main, scr_strip, cursor_row)
        elif info == "50_day_moving_average":
            print_stock_data(counter*w, n, data.fifty_day_moving_avg, "50dMAvg", scr_main, scr_strip, cursor_row)
        elif info == "200_day_moving_average":
            print_stock_data(counter*w, n, data.two_hundred_day_moving_avg, "200dMAvg", scr_main, scr_strip, cursor_row)
        elif info == "price_earnings_ratio":
            print_stock_data(counter*w, n, data.price_earnings_ratio, "P/E", scr_main, scr_strip, cursor_row)
        elif info == "price_earnings_growth_ratio":
            print_stock_data(counter*w, n, data.price_earnings_growth_ratio, "P/EGth", scr_main, scr_strip, cursor_row)
        elif info == "price_sales_ratio":
            print_stock_data(counter*w, n, data.price_sales_ratio, "P/Sale", scr_main, scr_strip, cursor_row)
        elif info == "price_book_ratio":
            print_stock_data(counter*w, n, data.price_book_ratio, "P/Book", scr_main, scr_strip, cursor_row)
        elif info == "short_ratio":
            print_stock_data(counter*w, n, data.short_ratio, "Short", scr_main, scr_strip, cursor_row)
        
        else:
            counter = counter - 1

        cursor_row = 0
        counter = counter + 1

    return cursor
