import pandas as pd
from pandas_datareader import data
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 

start_date = '2020-11-16'
end_date = '2021-02-01'

panel_data = data.DataReader('TSM', 'yahoo', start_date, end_date)
print(panel_data)
print("\n")
#we are going to focus on the closing price
close = panel_data['Close']
print('\n')

#https://github.com/umeshpalai/DailyReturn-LogReturn-CumulativeReturn-in-Python/blob/master/Daily%20Return%2C%20Log%20Return%20%26%20Cumulative%20Return%20in%20Python.ipynb
panel_data['Daily_Return'] = panel_data['Close']/panel_data['Close'].shift(1)-1
panel_data.head()

panel_data['Daily_Return_PCT'] = panel_data['Close'].pct_change(1)
panel_data.head()

panel_data['Daily_Log_Return'] = np.log(panel_data['Close']/panel_data['Close'].shift(1))
panel_data.head()

panel_data['Cumulative_return'] = np.cumsum(panel_data['Daily_Return'])
panel_data.head()

panel_data['Cumulative_Log_return'] = np.cumsum(panel_data['Daily_Log_Return'])
panel_data.head()

panel_data['Cumulative_return_Comp'] = (1 + panel_data['Daily_Return']).cumprod()
panel_data.head()

panel_data['Relative_Return'] = 100*(np.exp(panel_data['Cumulative_Log_return'])-1)
panel_data.head()
panel_data.to_csv(r'C:\Users\rodri\Documents\Financial_Trading\Revenue.csv')
print(panel_data)

print('\n')
##Important Parameters
log_returns = np.log(panel_data['Close']/panel_data['Close'].shift(1))
print(log_returns)


panel_data['Relative_Return'].plot(label='Total_Relative_Revenue',figsize=(16,8),title='Total Relative Revenue')
plt.xlabel('Date')
plt.ylabel('Total Revenue Returns (%)')
plt.legend()
plt.grid()
plt.show()