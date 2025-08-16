list_number = []
for i in range(5):
    num = int(input("Введите пять чисел:"))
    list_number.append(num)
for number in list_number:
    if number > 10:
        print(number)
    else:
        print("Таких чисел нет")   