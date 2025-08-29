import pandas as pd
import numpy as np

df = pd.read_csv("python/HW_8/customers.csv")

print("Весь файл: ", df) 

country = ['USA', 'France', 'Italy', 'Spain', 'USA', 'France', 'Italy', 'USA', 'France', 'Italy', 'Spain', 'USA', 'France', 'Italy', 'Spain', 'USA', 'France', 'Italy', 'France', 'USA']
df['country'] = country
print("Добавленный столбец country: ", df)
#Самая часто встречающаяся страна
most_frequent_country = df['country'].mode()[0]
print("Самая часто встречающаяся страна: ", most_frequent_country)

prices = [10.99, 20.99, 30.99, 40.99, 50.99, 60.99, 70.99, 80.99, 90.99, 100.99, 110.99, 120.99, 130.99, 140.99, 150.99, 160.99, 170.99, 180.99, 190.99, 200.99]
df['price'] = prices
print("Добавленный столбец price: ", df)
df['discount'] = 0.15 #15% скидка
df['final_price'] = (df['price'] * (1 - df['discount'])).round(2) # Вычисление финальной цены с учетом скидки
print("Добавленный столбец final_price: ", df)

max_price = df['final_price'].max()
print("Максимальная цена: ", max_price)

min_price = df['final_price'].min()
print("Минимальная цена: ", min_price)

sum_price = df['final_price'].sum()
print("Сумма всех цен: ", sum_price)

mean_price = df['final_price'].mean()
print("Средняя цена: ", mean_price)

sorted_df = df.sort_values(by='final_price', ascending=False)
print("Отсортированный DataFrame по убыванию final_price: ", sorted_df)