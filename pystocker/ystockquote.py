#
#  ystockquote : Python module - retrieve stock quote data from Yahoo Finance
#
#  Copyright (c) 2007,2008,2013,2016 Corey Goldberg (cgoldberg@gmail.com)
#
#  license: GNU LGPL
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
#
#  Requires: Python 2.7/3.3+


__version__ = '0.2.6dev'  # NOQA


try:
    # py3
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
except ImportError:
    # py2
    from urllib2 import Request, urlopen
    from urllib import urlencode


def _request(symbol, stat):
    url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbol, stat)
    req = Request(url)
    resp = urlopen(req)
    content = resp.read().decode().strip()
    return content


def get_all(symbol):
    """
    Get all available quote data for the given ticker symbol.

    Returns a dictionary.
    """
    ids = 'l1c1va2xj1b4j4dyekjm3m4rr5p5p6s7o'
    values = _request(symbol, ids).split(',')
    return dict(
        price=values[0],
        change=values[1],
        volume=values[2],
        avg_daily_volume=values[3],
        stock_exchange=values[4],
        market_cap=values[5],
        book_value=values[6],
        ebitda=values[7],
        dividend_per_share=values[8],
        dividend_yield=values[9],
        earnings_per_share=values[10],
        fifty_two_week_high=values[11],
        fifty_two_week_low=values[12],
        fifty_day_moving_avg=values[13],
        two_hundred_day_moving_avg=values[14],
        price_earnings_ratio=values[15],
        price_earnings_growth_ratio=values[16],
        price_sales_ratio=values[17],
        price_book_ratio=values[18],
        short_ratio=values[19],
        open_price=values[20])


def get_dividend_yield(symbol):
    return _request(symbol, 'y')


def get_dividend_per_share(symbol):
    return _request(symbol, 'd')


def get_ask_realtime(symbol):
    return _request(symbol, 'b2')


def get_dividend_pay_date(symbol):
    return _request(symbol, 'r1')


def get_bid_realtime(symbol):
    return _request(symbol, 'b3')


def get_ex_dividend_date(symbol):
    return _request(symbol, 'q')


def get_previous_close(symbol):
    return _request(symbol, 'p')


def get_today_open(symbol):
    return _request(symbol, 'o')


def get_change(symbol):
    return _request(symbol, 'c1')


def get_last_trade_date(symbol):
    return _request(symbol, 'd1')


def get_change_percent_change(symbol):
    return _request(symbol, 'c')


def get_trade_date(symbol):
    return _request(symbol, 'd2')


def get_change_realtime(symbol):
    return _request(symbol, 'c6')


def get_last_trade_time(symbol):
    return _request(symbol, 't1')


def get_change_percent_realtime(symbol):
    return _request(symbol, 'k2')


def get_change_percent(symbol):
    return _request(symbol, 'p2')


def get_after_hours_change(symbol):
    return _request(symbol, 'c8')


def get_change_200_sma(symbol):
    return _request(symbol, 'm5')


def get_commission(symbol):
    return _request(symbol, 'c3')


def get_percent_change_200_sma(symbol):
    return _request(symbol, 'm6')


def get_todays_low(symbol):
    return _request(symbol, 'g')


def get_change_50_sma(symbol):
    return _request(symbol, 'm7')


def get_todays_high(symbol):
    return _request(symbol, 'h')


def get_percent_change_50_sma(symbol):
    return _request(symbol, 'm8')


def get_last_trade_realtime_time(symbol):
    return _request(symbol, 'k1')


def get_50_sma(symbol):
    return _request(symbol, 'm3')


def get_last_trade_time_plus(symbol):
    return _request(symbol, 'l')


def get_200_sma(symbol):
    return _request(symbol, 'm4')


def get_last_trade_price(symbol):
    return _request(symbol, 'l1')


def get_1_year_target(symbol):
    return _request(symbol, 't8')


def get_todays_value_change(symbol):
    return _request(symbol, 'w1')


def get_holdings_gain_percent(symbol):
    return _request(symbol, 'g1')


def get_todays_value_change_realtime(symbol):
    return _request(symbol, 'w4')


def get_annualized_gain(symbol):
    return _request(symbol, 'g3')


def get_price_paid(symbol):
    return _request(symbol, 'p1')


def get_holdings_gain(symbol):
    return _request(symbol, 'g4')


def get_todays_range(symbol):
    return _request(symbol, 'm')


def get_holdings_gain_percent_realtime(symbol):
    return _request(symbol, 'g5')


def get_todays_range_realtime(symbol):
    return _request(symbol, 'm2')


def get_holdings_gain_realtime(symbol):
    return _request(symbol, 'g6')


def get_52_week_high(symbol):
    return _request(symbol, 'k')


def get_more_info(symbol):
    return _request(symbol, 'v')


def get_52_week_low(symbol):
    return _request(symbol, 'j')


def get_market_cap(symbol):
    return _request(symbol, 'j1')


def get_change_from_52_week_low(symbol):
    return _request(symbol, 'j5')


def get_market_cap_realtime(symbol):
    return _request(symbol, 'j3')


def get_change_from_52_week_high(symbol):
    return _request(symbol, 'k4')


def get_float_shares(symbol):
    return _request(symbol, 'f6')


def get_percent_change_from_52_week_low(symbol):
    return _request(symbol, 'j6')


def get_company_name(symbol):
    return _request(symbol, 'n')


def get_percent_change_from_52_week_high(symbol):
    return _request(symbol, 'k5')


def get_notes(symbol):
    return _request(symbol, 'n4')


def get_52_week_range(symbol):
    return _request(symbol, 'w')


def get_shares_owned(symbol):
    return _request(symbol, 's1')


def get_stock_exchange(symbol):
    return _request(symbol, 'x')


def get_shares_outstanding(symbol):
    return _request(symbol, 'j2')


def get_volume(symbol):
    return _request(symbol, 'v')


def get_ask_size(symbol):
    return _request(symbol, 'a5')


def get_bid_size(symbol):
    return _request(symbol, 'b6')


def get_last_trade_size(symbol):
    return _request(symbol, 'k3')


def get_ticker_trend(symbol):
    return _request(symbol, 't7')


def get_average_daily_volume(symbol):
    return _request(symbol, 'a2')


def get_trade_links(symbol):
    return _request(symbol, 't6')


def get_order_book_realtime(symbol):
    return _request(symbol, 'i5')


def get_high_limit(symbol):
    return _request(symbol, 'l2')


def get_eps(symbol):
    return _request(symbol, 'e')


def get_low_limit(symbol):
    return _request(symbol, 'l3')


def get_eps_estimate_current_year(symbol):
    return _request(symbol, 'e7')


def get_holdings_value(symbol):
    return _request(symbol, 'v1')


def get_eps_estimate_next_year(symbol):
    return _request(symbol, 'e8')


def get_holdings_value_realtime(symbol):
    return _request(symbol, 'v7')


def get_eps_estimate_next_quarter(symbol):
    return _request(symbol, 'e9')


def get_revenue(symbol):
    return _request(symbol, 's6')


def get_book_value(symbol):
    return _request(symbol, 'b4')


def get_ebitda(symbol):
    return _request(symbol, 'j4')


def get_price_sales(symbol):
    return _request(symbol, 'p5')


def get_price_book(symbol):
    return _request(symbol, 'p6')


def get_pe(symbol):
    return _request(symbol, 'r')


def get_pe_realtime(symbol):
    return _request(symbol, 'r2')


def get_peg(symbol):
    return _request(symbol, 'r5')


def get_price_eps_estimate_current_year(symbol):
    return _request(symbol, 'r6')


def get_price_eps_estimate_next_year(symbol):
    return _request(symbol, 'r7')


def get_short_ratio(symbol):
    return _request(symbol, 's7')


def get_historical_prices(symbol, start_date, end_date):
    """
    Get historical prices for the given ticker symbol.
    Date format is 'YYYY-MM-DD'

    Returns a nested dictionary (dict of dicts).
    outer dict keys are dates ('YYYY-MM-DD')
    """
    params = urlencode({
        's': symbol,
        'a': int(start_date[5:7]) - 1,
        'b': int(start_date[8:10]),
        'c': int(start_date[0:4]),
        'd': int(end_date[5:7]) - 1,
        'e': int(end_date[8:10]),
        'f': int(end_date[0:4]),
        'g': 'd',
        'ignore': '.csv',
    })
    url = 'http://real-chart.finance.yahoo.com/table.csv?%s' % params
    req = Request(url)
    resp = urlopen(req)
    content = str(resp.read().decode('utf-8').strip())
    daily_data = content.splitlines()
    hist_dict = dict()
    keys = daily_data[0].split(',')
    for day in daily_data[1:]:
        day_data = day.split(',')
        date = day_data[0]
        hist_dict[date] = \
            {keys[1]: day_data[1],
             keys[2]: day_data[2],
             keys[3]: day_data[3],
             keys[4]: day_data[4],
             keys[5]: day_data[5],
             keys[6]: day_data[6]}
    return hist_dict
