import requests
import pandas as pd

response = requests.get("https://fakestoreapi.com/products")

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
else:
    print(f"Ошибка при запросе: {response.status_code}")

df = df.dropna() # Удаляем строки с пропущенными значениями

df["price"] = df["price"].astype(float) # Преобразование в числовой формат

df["rating_rate"] = df["rating"].apply(lambda x: x["rate"]) # Извлечение рейтинга
df["rating_count"] = df["rating"].apply(lambda x: x["count"]) # Извлечение количества отзывов

filtered_df = df[df["price"] > 100] # Фильтрация товаров дороже 100$

print("Товары дороже 100$:")
print(filtered_df[["title", "price", "category", "rating_rate"]])

avg_price_by_category = df.groupby("category")["price"].mean().reset_index() # Средняя цена по категориям
print("Средняя цена по категориям:")
print(avg_price_by_category)

df.to_csv("clean_products.csv", index=False, encoding="utf-8") # Сохранение очищенного DataFrame
avg_price_by_category.to_csv("avg_price_by_category.csv", index=False, encoding="utf-8") # Сохранение средней цены по категориям

print("Файлы 'clean_products.csv' и 'avg_price_by_category.csv' сохранены!")