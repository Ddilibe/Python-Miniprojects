from forex_python.bitcoin import BtcConverter
import pandas as pd
import matplotlib.style as style
import matplotlib.pyplot as plt  
from datetime import datetime

b = BtcConverter() # Calls on the btc converter instance. An api that retrives information from a crypto source

start = datetime(2015, 1, 1) # start Date on which to retrive data
end = datetime(2022, 6,8) # End Date on when to retrive data 
price_data = b.get_previous_price_list("USD", start, end) 
# price_data contains data set retrived in in usd

size of data = len(price_data) # Size of the dataset
type_of_data = type(price_data) # Type of the data set(dict)

prices = pd.DataFrame(price_data.items(), columns=['date', 'price'])
# Prices were distributed into the columns date and prices
prices = prices.set_index("date") 
# Reassignes the index of the dataset to date changing the number of colunms into 2
prices.plot() # Prices plot is to visualize our progress

"""
changing the view of the plot
1. Making the curve smooth by  using a rolling avaerage

2. Improve the style of the plot using matplotlib

E.
"""
style.use('fivethirtyeight') # Design the size of the line

rolling = prices.rolling(30).mean()
# Rolling takes the mean of every 30 value and calls it one value
rolling.plot()
# The plot method plots it into a line graph

ax = rolling.plot() # Assigning the plot to a variable

# After so many manipulations, This method of the result was derived
pre_2021 = rolling.loc[:"2020-12-31"]
post_2021 = rolling.loc["2021-01-01": ]

fig, ax = plt.subplots(figsize=(8,4))
"""
    ax.plot (x-axis, y-axis, width-of-line, color-of-line)

"""
ax.plot(pre_2021.index.values, pre_2021["price"], linewidth=2)
ax.plot(post_2021.index.values, post_2021["price"], linewidth=4, color="red")

ax.axvspan(xmin=2192, xmax=361+2192, ymin=0, alpha=0.3, color="grey")

ticks = ["2015-01-01", "2016-01-01","2017-01-01", "2018-01-01", "2019-01-01", "2020-01-01","2021-01-01", "2022-01-01"]
tick_labels = ["2015","2016","2017","2018","2019","2020","2021","2022"]

plt.title("Bitcoin Prices Peaked In 2021")
plt.xticks(ticks, rotation="vertical")

ax.set_xticklabels(tick_labels)

plt.show()
