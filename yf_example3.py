""" yf_example3_solution.py

To download daily stock prices for Qantas for a given year into a CSV file
"""

import os

import toolkit_config as cfg
import yf_example2


def qan_prc_to_csv(year):
    """ Download stock prices from Yahoo Finance for a given year into
    CSV file called "qan_prc_YYYY.csv" where 'YYYY' corresponds to the year 'year'

    Parameters
    ----------
    year : int
        An integer with a four-digit year

    """

    tic = 'QAN.AX'
    start=f'{year}-01-01'
    end=f'{year}-12-31'

    pth = os.path.join(cfg.DATADIR, f'qan_prc_{year}.csv')
    df = yf_example2.yf_prc_to_csv(tic, pth, start, end)

if __name__ == "__main__":
    qan_prc_to_csv(year = 2020)