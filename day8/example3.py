"""Read a CSV file and process its data."""
import pandas as pd

df = pd.read_csv('data\student_marks.csv', index_col=0)
#df['Total'] = df[['Maths', 'Physics', 'Chemistry', 'English', 'Biology', 'Economics', 'History', 'Civics']].sum(axis=1)
df['Total_Score'] = df.eval('Maths + Physics + Chemistry + English + Biology + Economics + History + Civics')
df['Avg_Score'] = ((df['Total_Score']/8).round(2))
df.to_csv('data\scores.csv')
