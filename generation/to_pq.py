import pandas as pd


df1 = pd.read_csv('submit_data.csv')
df2 = pd.read_csv('deal_data.csv')



df1.to_parquet('submits.parquet')
df2.to_parquet('deals.parquet')
