# importing libraries 
import pandas as pd
import csv
from scipy.stats import norm
import statistics
%matplotlib inline
import sklearn
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

# loading csv 
data = pd.read_csv('auctions.csv')

# Renaming columns and rounding decimals
data.rename(columns = {'RoR': 'return_on_reserve',
                      'STR': 'lots_sold',
                      'BPL': 'bidders_per_lot'}, inplace = True)
data = np.round(data,decimals=2)

# Exploratory analysis
data.info()
data.describe()

# Features engeneering
data['total_sales'] = (data.avg_reserve+(data.avg_reserve * data.return_on_reserve))*(data.lots * data.lots_sold)
data['return_on_reserve'] = data.avg_reserve * data.return_on_reserve
data['lots_sold'] = (data.lots_sold * data.lots).astype(int)
data['bidders_per_auction'] = (data.bidders_per_lot * data.lots).astype(int)
del data['bidders_per_lot']

# total number of lots -- 239593
number_of_lots = data['lots'].sum()   # total number of lots in all the auctions
print(number_of_lots)

# popularity of kinds of auction
data['auction_mech'].value_counts()
# EnglishForward    3228
# FixedPrice        1568
# SealedBid         1424

# States and number of auctions
print(data['state'].value_counts())
print(data['state'].nunique())
# First 5
# CA    1292
# FL     783
# GA     650
# TX     481
# SC     405
# NV     375

# Percentage of average number of lots sold for kind of auctions
type_sold = data.groupby('auction_mech')['lots_sold'].mean()
type_sold
# EnglishForward    0.672038
# FixedPrice        0.497347
# SealedBid         0.601088

# Histogram with number of auctions per State
plt.style.use('seaborn-whitegrid')
fig_3 = data['state'].value_counts().plot(kind = 'bar', color = ['c','y','r', 'g', 'orange']);
plt.xlabel('State')
plt.ylabel('Number of auctions')
plt.title('Number of auctions per State', fontsize = 20)

# Histogram with state and percentage of lots sold
fig_4 = data.groupby('state')['lots_sold'].mean().sort_values(ascending=False).\
        plot(kind = 'bar', color = ['c','y','r', 'g', 'orange']);

plt.xlabel('State')
plt.ylabel('Percentage of lots sold')
plt.title('State and percentage of lots sold', fontsize = 20)

# Plotting correlation matrix
matrix = np.triu(corr)
ax = sns.heatmap(
    corr,
    vmin=-1, vmax=1, center=0,
    mask=matrix,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
)
ax.set_title('Correlation Matrix for Auctions 2019')

# Scatter plot of Total sales price Vs Number of lots
plt.style.use('seaborn-whitegrid')
x = data.total_sales/1e6
y = data.lots
plt.scatter(x, y, color = 'c')
plt.xlabel('Total sales price (Millions)')
plt.ylabel('Number of lots')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,527865))
plt.title('Total Sales Price vs Number of Lots', fontsize = 20)
plt.show()

# Scatter plot of Total sales price Vs Bidders per auction
x = data.total_sales/1e6
y = data.bidders_per_auction
plt.scatter(x, y, color = 'y')
plt.xlabel('Total sales price (Millions)')
plt.ylabel('Bidders per auction')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,527865))
plt.title('Total Sales Price vs Bidders per Auction', fontsize = 20)
plt.show()

# Scatter plot of Lots sold Vs Number of lots
x = data.lots_sold
y = data.lots
plt.scatter(x, y, color = 'c')
plt.xlabel('Lots sold')
plt.ylabel('Number of lots')
plt.title('Lots Sold vs Number of Lots', fontsize = 20)
plt.show()

# Scatter plot of Lots sold vs Bidders per auction
x = data.lots_sold
y = data.bidders_per_auction
plt.scatter(x, y, color = 'y')
plt.xlabel('Lots sold')
plt.ylabel('Bidders per auction')
plt.title('Lots Sold vs Bidders per Auction', fontsize = 20)
plt.show()

# Hystogram for type and number of auctions
fig_1 = data['auction_mech'].value_counts().plot(kind = 'bar', color = ['c','y','r']);

plt.xlabel('Type of auction')
plt.ylabel('Number of auctions')
plt.title('Type and number of auctions', fontsize = 20)

# Hystogram for auction type and percentage of lots sold
fig_2 = data.groupby('auction_mech')['lots_sold'].mean().sort_values(ascending=False).\
        plot(kind = 'bar', color = ['c','y','r']);

plt.xlabel('Type of auction')
plt.ylabel('Percentage of lots sold')
plt.title('Auction type and percentage of lots sold', fontsize = 20)

# Pie chart for percentage of Total Sales Price with respect to Auction Type
labels = 'English Forward', 'Fixed Price', 'Sealed Bid'
sizes = data.groupby('auction_mech')['total_sales'].mean()
explode = (0.04,0.04,0.04)
colors = ['c','y','r']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, explode = explode, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.title('Percentage of Total Sales Price with respect to Auction Type', fontsize = 13)

plt.show()


