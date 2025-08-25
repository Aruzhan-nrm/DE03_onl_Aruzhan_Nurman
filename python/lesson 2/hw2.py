# 1. -------------- Напишите программу,которая запрашивает у пользователя строку и выводит количество гласных и согласных букв в этой строке
text = input("Введите слово: ")

vowels = 'аоуыиэяюе'

vowel_count = 0
consonant_count = 0

for char in text:
    if char in vowels: 
        vowel_count += 1
    else:
        consonant_count += 1

print("Гласных букв:", vowel_count)
print("Согласных букв:", consonant_count)

# 2. -------------- Напишите программу, которая запрашивает у пользователя числа, вычисляет их сумму и среднее значение. Программа должна использовать циклы для обработки ввода и условные операторы для проверки корректности ввода.

total = 0
count = 0

while True:
    text = input("Введите число или нажмите стоп для завершения: ")
    
    if text == "стоп":
        break

    number = int(text)
    total += number
    count += 1

if count > 0:
    average = total / count
    print(f"Сумма чисел: {total}")
    print(f"Среднее значение: {average}")
else:
    print("Вы не ввели ни одного числа.")


# 3. -------------- Разработайте программу, которая запрашивает у пользователя число и выводит таблицу умножения для этого числа до 10.
number = int(input("Введите число: "))

i = 1
while i <= 10:
    result = number * i
    print(f"{number} x {i} = {result}")
    i += 1