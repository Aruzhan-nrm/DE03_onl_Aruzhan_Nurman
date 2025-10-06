# # ------------------------- Задание 1. Загрузка данных -------------------------
# import pandas as pd

# df = pd.read_csv(r"python\HW_10\orders.csv")

# # Преобразуй столбцы к правильным типам дата - datetime
# df['order_date'] = pd.to_datetime(df['order_date'], errors='raise')
# # возврат - bool
# df['returned'] = df['returned'].astype(bool)
# # цена/количество/скидка/доставка - числа
# df['unit_price'] = df['unit_price'].astype(float) 
# df['quantity'] = df['quantity'].astype(int)
# df['discount'] = df['discount'].astype(float)
# df['shipping_cost'] = df['shipping_cost'].astype(float)

# # Проверь данные: количество не меньше 1, цена больше 0, скидка от 0 до 10
# if (df['quantity'] < 1).any():
#     raise ValueError("Ошибка: количество должно быть не меньше 1")

# if (df['unit_price'] <= 0).any():
#     raise ValueError("Ошибка: цена должна быть больше 0")

# if ((df['discount'] < 0) | (df['discount'] > 10)).any():
#     raise ValueError("Ошибка: скидка должна быть в диапазоне от 0 до 10")

# print("Все данные корректные!")
# print(df.head())

# ------------------------- Задание 2. Подготовка данных -------------------------
import pandas as pd

def prepare_data(df: pd.DataFrame) -> pd.DataFrame: # вынес подготовку данных в отдельную функцию
    # Добавь gross = цена * количество
    df['gross'] = df['unit_price'] * df['quantity']
    
    # Добавь net = сумма заказа с учётом скидки и доставки
    df['net'] = df['gross'] * (1 - df['discount']) + df['shipping_cost']
    df.loc[df['returned'] == True, 'net'] = 0   # если возврат
    
    # Сделай колонку с месяцем заказа
    df['order_month'] = df['order_date'].dt.to_period('M').dt.to_timestamp()
    
    return df

df = pd.read_csv(r"python\HW_10\orders.csv")
df['order_date'] = pd.to_datetime(df['order_date'])   

df = prepare_data(df) 

print(df.head())

# ------------------------- Задание 3. Подготовка данных -------------------------
import pandas as pd


# Общая выручка (gross и net)
def total_revenue(df: pd.DataFrame):
    return df['gross'].sum(), df['net'].sum()

# Средний и медианный чек
def avg_median_check(df: pd.DataFrame):
    return df['net'].mean(), df['net'].median()

# Количество уникальных клиентов
def unique_customers(df: pd.DataFrame):
    return df['customer_id'].nunique()

# Доля возвратов
def return_rate(df: pd.DataFrame):
    return df['returned'].mean()

# Топ-N продуктов по продажам (по gross)
def top_products(df: pd.DataFrame, n=5):
    return df.groupby('product')['gross'].sum().sort_values(ascending=False).head(n)

# Заказы и продажи по странам
def sales_by_country(df: pd.DataFrame):
    return df.groupby('country').agg(
        orders=('order_id', 'count'),
        sales=('net', 'sum')
    ).sort_values('sales', ascending=False)

# Продажи по месяцам
def sales_by_month(df: pd.DataFrame):
    return df.groupby('order_month')['net'].sum()

if __name__ == "__main__":
    # тут df уже должен быть подготовлен (из предыдущих шагов)
    
    gross_sum, net_sum = total_revenue(df)
    print("Общая выручка (gross):", gross_sum)
    print("Общая выручка (net):", net_sum)

    avg_check, median_check = avg_median_check(df)
    print("Средний чек:", avg_check)
    print("Медианный чек:", median_check)

    print("Количество уникальных клиентов:", unique_customers(df))
    print("Доля возвратов:", return_rate(df))

    print("\nТоп-5 продуктов по продажам:")
    print(top_products(df, n=5))

    print("\nПродажи по странам:")
    print(sales_by_country(df))

    print("\nПродажи по месяцам:")
    print(sales_by_month(df))

# ------------------------- Задание 4. Сохранение результатов -------------------------
from pathlib import Path
from typing import Dict, Any
import pandas as pd

def save_reports(reports: Dict[str, pd.DataFrame], folder: str = "reports") -> Dict[str, str]:

    path = Path(folder)
    statuses: Dict[str, str] = {}

# Имя файлов, которые мы хотим получить
    filenames = {
        'overview': 'report_overview.csv',
        'top_products': 'report_top_products.csv',
        'countries': 'report_countries.csv',
        'monthly': 'report_monthly.csv'
    }

# Попытка создать папку (если нет) — отдельный try, чтобы поймать ошибки прав
    try:
        path.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        msg = f"Не удалось создать папку для отчётов '{path}': {e}"
        print("❌", msg)
        # пометим все как пропущенные из-за ошибки создания папки
        for key in filenames.values():
            statuses[key] = f"skipped: {msg}"
        return statuses

# Сохраняем каждый файл отдельно — чтобы ошибка с одним файлом не ломала остальные
    for key, fname in filenames.items():
        file_path = path / fname

        df = reports.get(key)
        if df is None:
            msg = f"Пропущено: в reports нет ключа '{key}'."
            print("⚠️", msg)
            statuses[fname] = f"skipped: {msg}"
            continue

# простая проверка — чтобы не пытаться вызвать to_csv у чего-то не DataFrame-подобного
        if not hasattr(df, "to_csv"):
            msg = f"Пропущено: объект reports['{key}'] не поддерживает to_csv()."
            print("⚠️", msg)
            statuses[fname] = f"skipped: {msg}"
            continue

        try:
            df.to_csv(file_path, index=False)
            msg = f"Сохранён: {file_path}"
            print("✅", msg)
            statuses[fname] = "ok"
        except PermissionError as e:
            msg = f"Ошибка прав при записи файла '{file_path}': {e}"
            print("❌", msg)
            statuses[fname] = f"permission_error: {e}"
        except Exception as e:
            msg = f"Ошибка при сохранении '{file_path}': {e}"
            print("❌", msg)
            statuses[fname] = f"error: {e}"

    return statuses

# ------------------------- Задание 5. Обработка ошибок -------------------------
def main():
    try:
        # 1. Загружаем данные
        df = pd.read_csv("orders.csv")

        # 2. Готовим данные
        df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
        df['gross'] = df['unit_price'] * df['quantity']
        df['net'] = df['gross'] * (1 - df['discount'])

        # 3. Аналитика
        reports = run_analytics(df)  # эта функция у тебя есть из прошлого задания

        # 4. Сохранение результатов
        save_reports(reports, folder="reports")

        print("✅ Работа завершена успешно.")

    except FileNotFoundError as e:
        print(f"❌ Файл не найден: {e.filename}. Проверьте путь и название файла.")
    except PermissionError as e:
        print(f"❌ Недостаточно прав для доступа к файлу или папке: {e}")
    except KeyError as e:
        print(f"❌ Ошибка в данных: отсутствует колонка {e}")
    except ValueError as e:
        print(f"❌ Ошибка значения: {e}")
    except Exception as e:
        print(f"❌ Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()
