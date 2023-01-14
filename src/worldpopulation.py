import pandas as pd
from bs4 import BeautifulSoup
import requests as r
url = 'https://en.wikipedia.org/wiki/World_population'

soup = r.get(url).text
print(soup)



