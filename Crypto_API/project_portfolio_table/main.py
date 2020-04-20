#display results inside terminal
import os
import requests
import json
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

print "............................................"
print('MY PORTFOLIO')
print "............................................"

portfolio_value = 0.00
last_updated = 0

table = PrettyTable(['Rank', 'Name', 'Symbol', 'Amount Owned', '$ Value', '$ Price', '1h', '24h', '7d'])

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'1',
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': API_KEY,
}

id_url = url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/map'
id_parameters = {
           'symbol':'BTC'
         }

get_url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
get_parameters = {
  'id':'1'
}

session = Session()
session.headers.update(headers)

portfolio_value = 0.00
last_updated = 0

with open('portfolio.txt') as inp:
    for line in inp:
        ticker, amount = line.split()
        ticker = ticker.upper()

        id_parameters['symbol'] = ticker
        parameters['symbol'] = ticker
        response = session.get(id_url, params=id_parameters)
        data = json.loads(response.text)
        #data = json.dumps(data, sort_keys=True, indent=4)
        id = data["data"][0]["id"]
        get_parameters["id"] = id

        response = session.get(get_url, params=get_parameters)
        data = json.loads(response.text)
        #data = json.dumps(data, sort_keys=True, indent=4)
        #print(data)
        data = data["data"][str(id)]

        rank = data['cmc_rank']
        name = data['name']
        last_updated = data['last_updated']
        symbol = data['symbol']
        quotes = data['quote']['USD']
        hour_change = quotes['percent_change_1h']
        day_change = quotes['percent_change_24h']
        week_change = quotes['percent_change_7d']
        price = quotes['price']

        value = float(price) * float(amount)

        if hour_change > 0:
            hour_change = Back.GREEN + str(hour_change) + '%' + Style.RESET_ALL
        else:
            hour_change = Back.RED + str(hour_change) + '%' + Style.RESET_ALL

        if day_change > 0:
            day_change = Back.GREEN + str(day_change) + '%' + Style.RESET_ALL
        else:
            day_change = Back.RED + str(day_change) + '%' + Style.RESET_ALL

        if week_change > 0:
            week_change = Back.GREEN + str(week_change) + '%' + Style.RESET_ALL
        else:
            week_change = Back.RED + str(week_change) + '%' + Style.RESET_ALL

        portfolio_value += value

        value_string = '{:,}'.format(round(value,2))

        table.add_row([rank,
                       name,
                       symbol,
                       amount,
                       '{:,}'.format(round(value,2)),
                       str(round(price,2)),
                       str(hour_change),
                       str(day_change),
                       str(week_change)
                       ])

print(table)
print()

portfolio_value_string = '{:,}'.format(round(portfolio_value,2))
last_updated_string = last_updated

print('Total Portfolio Value: ' + Back.GREEN + '$' + portfolio_value_string + Style.RESET_ALL)
print
print('API Results Last Updated on ' + last_updated_string)
print
