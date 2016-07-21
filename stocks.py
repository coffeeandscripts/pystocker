#!/usr/bin/env python

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

#opens a file called stock_codes and returns each line into an array
def open_stock_codes():
    
    stock_list = []

    with open("stock_codes", "r") as f:
        for line in f:
            stock_list.append(line.rstrip('\n'))

        f.close()

    return stock_list

def generate_stock_objects(code):

    data_array = ystockquote.get_all(str(code))

    return data_array

def print_data(n, data, scr_left, scr_main, scr_strip):

    scr_left.addstr(n, 0, data.code)
    scr_strip.addstr(0, 10, "Open")
    scr_main.addstr(n, 0, data.open)
    scr_strip.addstr(0, 18, "Price")
    scr_main.addstr(n, 8, data.price)
