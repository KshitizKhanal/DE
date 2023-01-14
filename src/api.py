import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI

class bitcoin:
    def __init__(self):
        cg = self.CoinGeckoAPI()
        bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)
        bitcoin_price_data = bitcoin_data['prices']