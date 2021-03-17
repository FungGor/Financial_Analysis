import pandas as pd
from pandas_datareader import data
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 
import statsmodels.api as sm


start_date = '2020-07-16'
end_date = '2021-03-17'

panel_data = data.DataReader('GME', 'yahoo', start_date, end_date)
print(panel_data)
print("\n")
#we are going to focus on the closing price
close = panel_data['Adj Close']
print(close)
print('\n')

short_window = 10
long_window = 20

signals = pd.DataFrame(index = panel_data['Adj Close'].index)
signals['signal'] = 0.0

# Create short simple moving average over the short window
signals['short_mavg']=panel_data['Adj Close'].rolling(window = short_window, min_periods=1, center=False).mean()

# Create long simple moving average over the short window
signals['long_mavg']=panel_data['Adj Close'].rolling(window = long_window, min_periods=1, center=False).mean()

#Create Signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:],1.0,0.0)

# Generate trading orders
signals['positions'] = signals['signal'].diff()

print(signals)

# Initialize the plot figure
fig = plt.figure()

# Add a subplot and label for y-axis
ax1 = fig.add_subplot(111,  ylabel='Price in $')

# Plot the closing price
panel_data['Adj Close'].plot(ax=ax1, color='r', lw=2.)

# Plot the short and long moving averages
signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

# Plot the buy signals
ax1.plot(signals.loc[signals.positions == 1.0].index, signals.short_mavg[signals.positions == 1.0],'^', markersize=10, color='m')

# Plot the sell signals
ax1.plot(signals.loc[signals.positions == -1.0].index, signals.short_mavg[signals.positions == -1.0],'v', markersize=10, color='k')

# Show the plot
plt.show()