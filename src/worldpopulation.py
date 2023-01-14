import pandas as pd
from bs4 import BeautifulSoup as BS
import requests as r
url = 'https://en.wikipedia.org/wiki/World_population'

data = r.get(url).text
soup = BS(data,'html.parser')

tables = soup.find_all('table')


for i,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = i
        break

# population_data = pd.DataFrame(columns=["Rank","Country","Density"])
# for row in tables[table_index].tbody.find_all("tr"):
#     col = row.find_all("td")
#     if (col != []):
#         rank = col[0].text
#         country = col[1].text
#         density = col[4].text.strip()
#         population_data =  population_data.append({"Rank":rank,"Country":country,"Density":density},ignore_index=True)

# print(population_data)

pop_data = pd.read_html(str(tables[table_index]),flavor='bs4')
print(pop_data)





