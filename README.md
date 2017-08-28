# scrape_LTC_prices_then_average

Run ltc_scrape_strip.py (this scrapes the required price data and strips the currency symbol out) on as many sites as possible (of course changing the URL and xpath data as applicable for each website) and then use the ltc_average.py to work out the average price of LTC gainst GBP (prints to screen and writes to .txt document). Perhaps use cron to email the result to yourself (and others) at any given frequency.
