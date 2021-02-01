from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd

start_date = '2020-01-04'
end_date = '2021-02-01'

panel_data = data.DataReader('TSM', 'yahoo', start_date, end_date)
print("\n")
#we are going to focus on the closing price
close = panel_data['Close']
print('\n')
#get all weekdays
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')

# How do we align the existing prices in adj_close with our new set of dates?
# All we need to do is reindex close using all_weekdays as the new index
close = close.reindex(all_weekdays)

# Reindexing will insert missing values (NaN) for the dates that were not present
# in the original set. To cope with this, we can fill the missing by replacing them
# with the latest available price for each instrument.
close = close.fillna(method='ffill')
print("\n")
print(panel_data)
information = close.describe()  #the information for this month such as average, mean....
print("\n")
print(information)
print('\n')

panel_data['SMA (5 days)'] = panel_data['Close'].rolling(window = 5).mean()
panel_data['SMA (10 Days)'] = panel_data['Close'].rolling(window = 10).mean()
panel_data['SMA (15 Days)'] = panel_data['Close'].rolling(window = 15).mean()
panel_data['SMA (20 Days)'] = panel_data['Close'].rolling(window = 20).mean()
panel_data['SD (5 days)'] = panel_data['Close'].rolling(window = 5).std()
panel_data['SD (10 days)'] = panel_data['Close'].rolling(window = 10).std()
panel_data['SD (15 days)'] = panel_data['Close'].rolling(window = 15).std()
panel_data['SD (20 days)'] = panel_data['Close'].rolling(window = 20).std()


panel_data['Bollinger High (5 days)'] =  (panel_data['Close'].rolling(window = 5).mean()) + ((panel_data['Close'].rolling(window = 5).std())*2)
panel_data['Bollinger Low (5 days)'] = (panel_data['Close'].rolling(window = 5).mean()) - ((panel_data['Close'].rolling(window = 5).std())*2)

panel_data['Bollinger High (10 days)'] =  (panel_data['Close'].rolling(window = 10).mean()) + ((panel_data['Close'].rolling(window = 10).std())*2)
panel_data['Bollinger Low (10 days)'] = (panel_data['Close'].rolling(window = 10).mean()) - ((panel_data['Close'].rolling(window = 10).std())*2)

panel_data['Bollinger High (15 days)'] =  (panel_data['Close'].rolling(window = 15).mean()) + ((panel_data['Close'].rolling(window = 15).std())*2)
panel_data['Bollinger Low (15 days)'] = (panel_data['Close'].rolling(window = 15).mean()) - ((panel_data['Close'].rolling(window = 15).std())*2)

panel_data['Bollinger High (20 days)'] =  (panel_data['Close'].rolling(window = 20).mean()) + ((panel_data['Close'].rolling(window = 20).std())*2)
panel_data['Bollinger Low (20 days)'] = (panel_data['Close'].rolling(window = 20).mean()) - ((panel_data['Close'].rolling(window = 20).std())*2)

print(panel_data)
panel_data.to_csv(r'C:\Users\rodri\Documents\Financial_Trading\tsm.csv')

panel_data['Close'].plot(label='TSM',figsize=(16,8),title='Closing Price')
panel_data['SMA (5 days)'].plot(label='5-Day SMA',color='green')
panel_data['SMA (10 Days)'].plot(label='10-Day SMA',color='red')
panel_data['SMA (15 Days)'].plot(label='15-Day SMA',color='blue')
plt.legend()
plt.grid()
plt.show()