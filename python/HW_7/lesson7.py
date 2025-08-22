# Напишите программу, которая запрашивает у пользователя ввод числа и выполняет деление 100 на это число. Обработайте возможные исключения, такие как деление на ноль и ввод нечислового значения.
try:
    number = input("Введите число: ")
    result = 100 / number
    print("Результат:", result)

except ZeroDivisionError:
    print("Ошибка: На ноль не делим!")

except ValueError:
    print("Ошибка: Введите число!")

# Напишите программу, которая запрашивает у пользователя ввод числа, проверяет его на положительное значение, используя пользовательское исключение, и выводит результат.
# class NegativeNumberError(Exception):
#     pass

# try:
#     number = int(input("Введите число: "))
#     if number <= 0:
#         raise NegativeNumberError("Число должно быть положительным!")
#     print("Вы ввели положительное число:", number)
# except NegativeNumberError as e:
#     print("Ошибка:", e)
# except ValueError:
#     print("Ошибка: Введите число!")