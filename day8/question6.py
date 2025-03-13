"""Write a program that reads a CSV file and finds the total sales revenue for a specific product."""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/100SalesRecords.csv')
new_df = df[df['Item Type'] == 'Meat']
new_df = new_df.groupby('Item Type')['Total Revenue'].sum().to_frame('total_sales').reset_index()

print(new_df)
