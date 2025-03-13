"""Given a CSV file with student names and scores, find the student with the highest score."""

from numpy import random
import pandas as pd

df = pd.read_csv('data\students.csv', index_col=0)
df['Scores'] = (random.randint(100, size=(100)))
df.to_csv('data\students.csv')
print(df.query(f"Scores == {df['Scores'].max()}"))

