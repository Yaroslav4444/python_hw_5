"""
1) Создать программно файл в текстовом формате, записать в него построчно
данные, вводимые пользователем. Об окончании ввода данных свидетельствует
пустая строка.
"""

new_txt = open('my_file.txt', 'w', encoding='utf=8')
user_text = input('Введите текст \n')
while user_text:
    new_txt.writelines(user_text)
    user_text = input('Введите текст \n')
    if not user_text:
        break

new_txt.close()
