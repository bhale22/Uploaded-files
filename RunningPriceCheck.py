import pandas as pd
import yfinance as yf
from Get_Price import get_price

df = pd.read_csv('Stockscsv.csv')

for row in range (len(df)):
    ask = get_price(df.loc[row, "Symbol"])
    status = df.loc[row,"Status"]
    if ask > 0:
        if status != 'Completed':
            df.loc[row, "Current_Price"] = ask
        if status == 'Held' or status == 'Open':
            df.loc[row,"Current_Gain_Loss"] = ((ask - df.loc[row,"Buy_Price"])/df.loc[row,"Buy_Price"])
df.to_csv('Stockscsv.csv', index = False)
print(df)
