"""Given a CSV file with temperature data for each day of the week, find the average temperature for each day."""

import pandas as pd

df = pd.read_csv('data/temperature.csv')

print(f"The average temperature is {df['temp'].mean():.2f}")