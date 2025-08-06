# ------------ 1. Создайте переменную x и присвойте ей значение 10. Выведите значение переменнойна экран. ------------
variable = 10

print(variable)

# ------------ 2. Создайте переменные name (строка), age (число) и is_student (булевый тип). Выведите их значения. ------------
name = "Aruzhan" #str 
age = 27 #int
is_student = True #bull

print(name)
print(age)
print(is_student)

# ------------ 3. Напишите программу, которая запрашивает у пользователя три числа, сравнивает их между собой и выводит максимальное и  минимальное число ------------
first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
third_number = int(input("Введите третье число: "))

if first_number >= second_number and first_number >= third_number:
    maxi = first_number
elif second_number >= first_number and second_number >= third_number:
    maxi = second_number
else:
    maxi = third_number

if first_number <= second_number and first_number <= third_number:
    mini = first_number
elif second_number <= first_number and second_number <= third_number:
    mini = second_number
else:
    mini = third_number

print("Максимальное число:", maxi)
print("Минимальное число:", mini) 


# --------- ДОП 1. Напишите программу, которая запрашивает у пользователя его возраст, преобразует введенное значение в целое число, добавляет к нему 5 и выводит сообщение: "Через 5 лет вам будет X лет", где X — рассчитанное значение. ---------
age = int(input("Введите ваш возраст: "))

transformation = age + 5

print(f"Через 5 лет вам будет {transformation} лет")

# --------- 2. Количество чётных и нечётных чисел в диапазоне. Задача: Пользователь вводит числа a и b (a ≤ b). Вывести количество чётных и нечётных чисел в этом диапазоне. ---------
a = int(input("Введите число: "))
b = int(input("Введите еще число: "))

even_count = 0
odd_count = 0

i = a
while i <= b:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    i += 1

print("Количество чётных чисел:", even_count)
print("Количество нечётных чисел:", odd_count)