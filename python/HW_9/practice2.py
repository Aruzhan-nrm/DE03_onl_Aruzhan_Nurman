# #Напишите программу, которая выводит все числа от 1 до 20, но вместо чисел, кратных 3, печатает слово "Fizz", а вместо чисел, кратных 5, — "Buzz".
# def fizz_buzz(): # функция для вывода чисел от 1 до 20
#     for i in range(1, 21): 
#         if i % 3 == 0 and i % 5 == 0: 
#             print("FizzBuzz")
#         elif i % 3 == 0: 
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)


#Напишите программу, которая выведет сумму всех элементов списка.
# numbers = [2, 5, 7, 3, 8]

# sum_numbers = sum(numbers)
# print("Сумма чисел:", sum_numbers)

# Напишите программу на Python, которая загружает данные из CSV файла, очищает их (удаляет пропущенные значения и дубликаты) и выводит итоговый DataFrame
import pandas as pd
import numpy as np

df = pd.read_csv('python/lesson 9/data.csv')
print(df)

average_price = df[(df['price'] > 300) & (df['price'] < 800)]
print(average_price)

sorted_df = df.sort_values(by = 'price', ascending = False)
print('Сортировка по убыванию прайса: ', sorted_df)

df['total_price'] = df['price'] * df['quantity']
print(df)

popular_product = df[df['quantity'] > 2]
print('Популярный товар: ', popular_product)

df = df.dropna(subset=['product'])
df = df.drop_duplicates(subset=['customer_name'])
print(df)