import os
import requests
import json
from datetime import datetime
import time

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

already_hit_symbols = []

print 'ALERTS TRACKING....................................'

while True:
    with open('prices.txt') as inp:
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
            price = quotes['price']

            if float(price) >= float(amount) and symbol not in already_hit_symbols:
                os.system('say ' + name + ' hit ' + amount)
                last_updated_string = last_updated
                print(name + ' hit ' + amount + ' on ' + last_updated_string)
                already_hit_symbols.append(symbol)

    print '.......................................'
    time.sleep(300)
