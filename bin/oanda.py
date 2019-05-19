import configparser
import oandapy as opy
import pandas as pd
import json
import oandapyV20
import oandapyV20.endpoints.accounts as accounts
from exampleauth import exampleauth

config = configparser.ConfigParser()
config.read('../config/oanda.cfg')

oanda = opy.APIv20(environment='practice',
                access_token=config['oanda']['access_token'])

data = oanda.get_history(instrument='EUR_USD',  # our instrument
                         start='2016-12-08',  # start data
                         end='2016-12-10',  # end date
                         granularity='M1')

print(data)