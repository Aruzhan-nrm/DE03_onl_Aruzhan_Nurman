import pandas as pd
import numpy as np

df = pd.read_csv(f'python\HW_8\customers.csv')
print(df)
price = [10.99, 20.99, 30.99, 40.99, 50.99, 60.99, 70.99, 80.99, 90.99, 100.99, 110.99, 120.99, 130.99, 140.99, 150.99, 160.99, 170.99, 180.99, 190.99, 200.99]
df['price'] = price
print(df)
count = [23, 45, 67, 89, 12, 34, 56, 78, 90, 11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 21]
df['count'] = count
print(df)

df['total'] = df['count'] * df['price']

low_count = df[df['count'] < 50]
print(f'Low count:\n{df[low_count]}')