# --------- 1. Откройте файл example.txt и выведите его содержимое на экран.
file = open(r"hw of less5\example.txt", "r", encoding="utf-8")
content = file.read()
print(content)
file.close()

# --------- 2. Создайте файл output.txt и запишите в него строку "Hello, World!"
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello, World!")

# --------- 3. Напишите программу, которая считает количество строк, слов и символов в заданном текстовом файле и выводит результаты.
myfile = "hw of less5\example1.txt"

with open(myfile, "r", encoding="utf-8") as file:
    content = file.read()

# количество строк
lines = content.splitlines()
num_lines = len(lines)

# количество слов
words = content.split()
num_words = len(words)

# количество символов
num_chars = len(content)

print("Количество строк:", num_lines)
print("Количество слов:", num_words)
print("Количество символов:", num_chars)