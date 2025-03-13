"""Given a CSV file with employee details (name, age, salary), calculate the average salary of all employees."""

import pandas as pd

def main():
  df = pd.read_csv('data/employees.csv')

  new_df = df.dropna() # remove all null records
  average_salary = new_df['Salary'].mean()

  #print((new_df['Salary'].sum()/len(new_df)))
  print(f'Average salary = {average_salary:,.2f}')


if __name__ == '__main__':
  main()