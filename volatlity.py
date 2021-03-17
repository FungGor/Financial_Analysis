import pandas as pd
from pandas_datareader import data
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 
import statsmodels.api as sm


start_date = '2020-11-16'
end_date = '2021-03-17'

panel_data = data.DataReader('GME', 'yahoo', start_date, end_date)
print(panel_data)
print("\n")
#we are going to focus on the closing price
close = panel_data['Adj Close']
print(close)
print('\n')

panel_data['Daily_Return_PCT'] = panel_data['Adj Close'].pct_change(1)
panel_data.head()
print(panel_data['Daily_Return_PCT'])
print('\n')

panel_data['Daily_Log_Return'] = np.log(panel_data['Adj Close']/panel_data['Adj Close'].shift(1))
panel_data.head()
print(panel_data['Daily_Log_Return'])
print('\n')

voltality = panel_data['Daily_Return_PCT'].rolling(window = 5).std()*np.sqrt(5)
voltality.plot(figsize=(10,8))
plt.show()
