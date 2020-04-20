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
import json

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
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  #data = json.dumps(data, sort_keys=True, indent=4)
  data = data["data"]
  for crypto in data:
    print 'Rank is '+ str(crypto["cmc_rank"]) + " Name is " + crypto["name"] + " Price is " + "$"+ str(crypto["quote"]["USD"]["price"])
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)