# 1.--------- Создайте переменную x и присвойте ей значение 10. Выведите значение переменнойна экран.---------
variable = 10

print(variable)

# 2.--------- Создайте переменные name (строка), age (число) и is_student (булевый тип). Выведите их значения.---------
name = "Aruzhan" #str 
age = 27 #int
is_student = True #bull

print(name)
print(age)
print(is_student)

# 3.--------- Напишите программу, которая запрашивает у пользователя три числа, сравнивает их между собой и выводит максимальное и  минимальное число---------
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