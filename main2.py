import pandas as pd
read = pd.read_csv('heis_usa.csv')
read.to_excel('result.xlsx')
