# Задание 1
file = open(r"lesson 5\file.txt", "r", encoding="utf-8")
content = file.read()
file.close()

new_file = open(r"lesson 5\file_copy.txt", "w", encoding="utf-8")
new_file.write(content)
new_file.close()

print(content)

# # Задание 2
# file = open(r"lesson 5\file.txt", "r", encoding="utf-8")
# content = file.read()
# file.close()

# content_upper = content.upper()

# new_file = open(r"lesson 5\file_upper.txt", "w", encoding="utf-8")
# new_file.write(content_upper)
# new_file.close()

# print(content_upper)