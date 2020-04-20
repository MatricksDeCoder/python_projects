#rank top 100(example here will use 10) crypto by rank,
# market cap, price, volume, price changes
import os
import json
import requests
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style

path           = '~/Desktop/Completed_Projects/python_projects/Crypto_API'
from dotenv import load_dotenv
project_folder = os.path.expanduser(path)
load_dotenv(os.path.join(project_folder, '.env'))
API_KEY = os.getenv("API_KEY")

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'10',
  'sort':'market_cap',
  'sort_dir':'desc'
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': API_KEY,
}

sort = 'market_cap'
session = Session()
session.headers.update(headers)

while True:

    print "................................................"
    print 'CoinMarketCap Explorer Menu'
    print('1 - Top 10 sorted by market cap')
    print('2 - Top 10 sorted by price')
    print('3 - Top 10 sorted by 1h percent change')
    print('4 - Top 10 sorted by 24h percent change')
    print('5 - Top 10 sorted by 7d percent change')
    print('6 - Top 10 sorted by 24 hour volume')
    print('0 - Exit')
    print "--------------------------------------------------"

    choice = input('What is your choice? (1-7): ')

    if choice == '1':
        sort  = 'market_cap'
    if choice == '2':
        sort = 'price'
    if choice == '3':
        sort = 'percent_change_1h'
    if choice == '4':
        sort = 'percent_change_1h'
    if choice == '5':
        sort = 'percent_change_24h'
    if choice == '6':
        sort = 'percent_change_7d'
    if choice == '0':
        break

    parameters['sort'] = sort

    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    #data = json.dumps(data, sort_keys=True, indent=4)

    array_data = data["data"]

    table = PrettyTable(['Rank', 'Asset','Symbol', 'Price', 'Market Cap', 'Volume', '1h', '24h', '7d'])

    print "............................."
    for data in array_data:
        rank = data['cmc_rank']
        name = data['name']
        symbol = data['symbol']
        last_updated = data['last_updated']
        quotes = data['quote']['USD']
        price = quotes['price']
        market_cap = quotes['market_cap']
        volume = quotes['volume_24h']
        hour_change = quotes['percent_change_1h']
        day_change = quotes['percent_change_24h']
        week_change = quotes['percent_change_7d']

        if hour_change is not None:
            if hour_change > 0:
                hour_change = Back.GREEN + str(hour_change) + '%' + Style.RESET_ALL
            else:
                hour_change = Back.RED + str(hour_change) + '%' + Style.RESET_ALL

        if day_change is not None:
            if day_change > 0:
                day_change = Back.GREEN + str(day_change) + '%' + Style.RESET_ALL
            else:
                day_change = Back.RED + str(day_change) + '%' + Style.RESET_ALL

        if week_change is not None:
            if week_change > 0:
                week_change = Back.GREEN + str(week_change) + '%' + Style.RESET_ALL
            else:
                week_change = Back.RED + str(week_change) + '%' + Style.RESET_ALL

        if volume is not None:
            volume_string = '{:,}'.format(volume)

        if market_cap is not None:
            market_cap_string = '{:,}'.format(market_cap)

        table.add_row([rank,
                       name,
                       symbol,
                       '$' + str(price),
                       '$' + str(market_cap),
                       '$' + volume_string,
                       str(hour_change),
                       str(day_change),
                       str(week_change)])

    print "......................................."
    print(table)
    print "---------------------------------------"

    choice = input('Again? (y/n): ')

    if choice == 'n':
        break
