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
from datetime import datetime

currency ="USD"
url = 'https://sandbox-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
parameters = {
  'convert': currency
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': API_KEY,
}

session = Session()
session.headers.update(headers)


#last_updated_string = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I:%

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  #data = json.dumps(data, sort_keys=True, indent=4)

  active_currencies = int(data['data']['active_cryptocurrencies'])
  active_markets = int(data['data']['active_exchanges'])
  active_market_pairs = int(data['data']['active_market_pairs'])
  btc_dominance = float(data['data']['btc_dominance'])
  eth_dominance = float(data['data']['eth_dominance'])
  altcoin_market_cap = int(data['data']['quote'][currency]['altcoin_market_cap'])
  altcoin_volume_day= int(data['data']['quote'][currency]['altcoin_volume_24h'])
  total_market_cap= int(data['data']['quote'][currency]['total_market_cap'])
  total_volume_day = int(data['data']['quote'][currency]['total_volume_24h'])
  last_updated_string = data['data']['last_updated']
  #last_updated_string = last_updated.strftime('%B %d, %Y at %I:%M%p')

  active_currencies = '{:,}'.format(active_currencies)
  active_markets = '{:,}'.format(active_markets)
  active_market_pairs = '{:,}'.format(active_market_pairs)
  altcoin_market_cap = '{:,}'.format(altcoin_market_cap)
  altcoin_volume_day = '{:,}'.format(altcoin_volume_day)
  total_market_cap = '{:,}'.format(total_market_cap)
  total_volume_day = '{:,}'.format(total_volume_day)

  print "..............................................................................................."
  print 'There are currently ' + active_currencies + ' active cryptocurrecies and ' + active_markets + ' active markets.'
  print 'There are currently ' + active_market_pairs + ' active market pairs.'
  print 'The global cap of all cryptos is ' + total_market_cap + ' and the 24h global volume is ' + total_volume_day+ '.'
  print 'The altcoin cap of cryptos is ' + altcoin_market_cap + ' and the 24h global volume is ' + altcoin_volume_day+ '.'
  print 'Bitcoin\'s total percentage of the global cap is ' + str(btc_dominance) + '%.'
  print 'Ethereum\'s total percentage of the global cap is ' + str(eth_dominance) + '%.'
  print('This information was last updated on ' + last_updated_string + '.')
  print "..............................................................................................."

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print e
