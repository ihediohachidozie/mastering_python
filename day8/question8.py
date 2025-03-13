"""Implement a program that reads a CSV file and generates a bar chart to represent the data using Matplotlib."""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/100SalesRecords.csv')

new_df = df.groupby('Item Type')['Total Revenue'].sum().to_frame('total_revenue').reset_index()
#plt.pie(new_df['total_revenue'], labels=new_df['Item Type'])
#plt.bar(new_df['total_revenue'], new_df['Item Type'])
#plt.show()
#new_df.plot(kind='bar')
items = new_df['Item Type']
values = new_df['total_revenue']

plt.barh(new_df['Item Type'], new_df['total_revenue'], color=['#8B0000','#006400','#DB7093','#00008B','#800080','#FA8072','#87CEEB'])
plt.title('Revenue by Item Type')
plt.xlabel('Item Type')
plt.ylabel('Sales')

#plt.

plt.show()

#print(new_df['total_revenue'])



