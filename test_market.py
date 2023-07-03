from fugle_marketdata import RestClient

import os
api_key = os.getenv('FUGLE_API_KEY')

client = RestClient(api_key=api_key)
stock = client.stock
r = stock.snapshot.movers(market='TSE', direction='up', change='percent')

