import pandas as pd
from pandas_datareader import data
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 

start_date = '2020-11-16'
end_date = '2021-02-01'

APPLE =  data.DataReader('AAPL', 'yahoo', start_date, end_date)
TSM = data.DataReader('TSM', 'yahoo', start_date, end_date)


#Daily Return

#Daily Return
APPLE['Daily_Return'] = APPLE['Close']/APPLE['Close'].shift(1)-1
APPLE.head()
TSM['Daily_Return'] = TSM['Close']/TSM['Close'].shift(1)-1
TSM.head()

#Daily Log Return
APPLE['Daily_Log_Return'] = np.log(APPLE['Close']/APPLE['Close'].shift(1))
APPLE.head()
TSM['Daily_Log_Return'] = np.log(TSM['Close']/TSM['Close'].shift(1))
TSM.head()

#PCT 
APPLE['Daily_Return_PCT'] = APPLE['Close'].pct_change(1)
APPLE.head()
TSM['Daily_Return_PCT'] = TSM['Close'].pct_change(1)
TSM.head()

#Cumulative Return
APPLE['Cumulative_return'] = np.cumsum(APPLE['Daily_Return'])
APPLE.head()
TSM['Cumulative_return'] = np.cumsum(TSM['Daily_Return'])
TSM.head()

#Cumulative Log Return
APPLE['Cumulative_Log_return'] = np.cumsum(APPLE['Daily_Log_Return'])
APPLE.head()
TSM['Cumulative_Log_return'] = np.cumsum(TSM['Daily_Log_Return'])
TSM.head()

#Relative Return
APPLE['Relative_Return'] = 100*(np.exp(APPLE['Cumulative_Log_return'])-1)
APPLE.head()
TSM['Relative_Return'] = 100*(np.exp(TSM['Cumulative_Log_return'])-1)
TSM.head()

print(APPLE)
print('\n')
print(TSM)
print('\n')
APPLE.to_csv(r'C:\Users\rodri\Documents\Financial_Trading\APPLE_Revenue.csv')
TSM.to_csv(r'C:\Users\rodri\Documents\Financial_Trading\TSM_Revenue.csv')
#Weight Traing -- Advanced Quantitative Trading Strategy
#https://www.learndatasci.com/tutorials/python-finance-part-2-intro-quantitative-trading-strategies/
Returns = []
rt_apple = APPLE['Daily_Log_Return'].tail(1).tolist()
rt_tsm = TSM['Daily_Log_Return'].tail(1).tolist()

log_apple = APPLE['Daily_Log_Return'].tolist()
log_tsm = TSM['Daily_Log_Return'].tolist()

weight = [1/3,1/3]
Returns.append(log_apple[-1])
Returns.append(log_tsm[-1])
Return_Array = np.array(Returns)
Weighted = np.array(weight)
print(Return_Array.T)
print(Weighted.T)

# Total log_return for the portfolio is:
portfolio_log_return = Weighted.dot(Return_Array)
print(portfolio_log_return)

#Log Return Matrix for those instruments (It could be donated as Matrix R Log_Returns)
Portfolio = pd.concat([APPLE['Daily_Log_Return'],TSM['Daily_Log_Return']], ignore_index=False,axis=1)
Portfolio.columns = ['APPL','TSM']
print(Portfolio)

print('\n')
#Create the weight matrix
weighted_matrix = pd.DataFrame(1/3, index=Portfolio.index, columns=Portfolio.columns)

#Just for example
print(weighted_matrix.tail())
print('\n')
print(Portfolio.head())
print('\n')
# Initially the two matrices are multiplied. Note that we are only interested in the diagonal, 
# which is where the dates in the row-index and the column-index match.
temp_var = weighted_matrix.dot(Portfolio.transpose())
print(temp_var.head().iloc[:, 0:5])
print('\n')
# The numpy np.diag function is used to extract the diagonal and then
# a Series is constructed using the time information from the log_returns index
log_return_portfolio = pd.Series(np.diag(temp_var), index=Portfolio.index)
print(log_return_portfolio)
print('\n')
total_relative_returns = (np.exp(log_return_portfolio.cumsum())-1)

fig, (ax1,ax2) = plt.subplots(2,1,figsize=(16,12))
ax1.plot(log_return_portfolio.cumsum())
ax1.set_ylabel('Portfolio cumulative log returns')
ax2.plot( 100 * total_relative_returns)
ax2.set_ylabel('Portfolio total relative returns (%)')
plt.show()