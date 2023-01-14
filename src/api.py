import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI

class BitCoin:
    def __init__(self):
        self.data_to_return = {}
    
    def get_values(self):
        cg = CoinGeckoAPI()
        bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)
        bitcoin_price_data = bitcoin_data['prices']
        data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])
        data['date'] = data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))
        self.data_to_return = data.iloc[0:,1:]
        return self.data_to_return
        

bit = BitCoin()

data = bit.get_values()
print(data)