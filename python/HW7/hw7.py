# ------------- 1.Напишите функцию, которая принимает список чисел и возвращает их среднее значение. Обработайте исключения, связанные с пустым списком и некорректными типами данных.-------------
def average(numbers):
    try:
        if len(numbers) == 0:  # проверка на пустой список
            raise ValueError("Пустой список")
        return sum(numbers) / len(numbers)
    except TypeError:
        return "Ошибка: в списке есть некорректные данные"
    except ValueError as e:
        return f"Ошибка: {e}"

print(average([10, 20, 30]))   # 20.0
print(average([]))             # Ошибка: Пустой список
print(average([10, "a", 20]))  # Ошибка: в списке есть некорректные данные

# ------------- 2. Создайте программу, которая считывает список чисел из файла, проверяет каждое число на чётность и записывает результаты (чётное или нечётное) в другой файл. Используйте обработку исключений для возможных ошибок ввода-вывода.-------------
def check_numbers(input_file, output_file):
    try:
        # читаем все строки из input.txt
        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        results = []
        for line in lines:
            try:
                num = int(line.strip())  # пробуем превратить строку в число
                if num % 2 == 0:
                    results.append(f"{num} - чётное\n")
                else:
                    results.append(f"{num} - нечётное\n")
            except ValueError:
                results.append(f"{line.strip()} - не число!\n")

        # записываем результаты в output.txt
        with open(output_file, "w", encoding="utf-8") as f:
            f.writelines(results)

        print(f"Результаты записаны в файл {output_file}")

    except FileNotFoundError:
        print(f"Файл {input_file} не найден! Создай его рядом с программой.")
    except IOError as e:
        print(f"Ошибка ввода-вывода: {e}")


check_numbers("input.txt", "output.txt")