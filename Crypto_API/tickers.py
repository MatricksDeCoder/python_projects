import os
import requests
import json

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
  'limit':'5',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': API_KEY,
}

session = Session()
session.headers.update(headers)

try:
  while True:
        choice = input("Do you want to enter any custom parameters? ('y'/'n'): ")
        print choice

        if choice == 'y':
            limit = input('What is the custom limit?: ')
            start = input('What is the custom start number?: ')

        parameters["start"] = start
        parameters["limit"] = limit

        response = session.get(url, params=parameters)
        data = json.loads(response.text)

        #print(json.dumps(results, sort_keys=True, indent=4))

        data = data['data']

        for crypto in data:
            rank = crypto['cmc_rank']
            name = crypto['name']
            symbol = crypto['symbol']

            circulating_supply = int(crypto['circulating_supply'])
            price = crypto["quote"]["USD"]["price"]

            circulating_supply_string = '{:,}'.format(circulating_supply)

            print(str(rank) + ': ' + name + ' (' + symbol + ')')
            print('Price: \t\t\t$' + str(price))
            print('Circulating supply: \t' + circulating_supply_string)
            print "........................................................"

        choice = input('Again? (y/n): ')

        if choice == 'n':
            break
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)



