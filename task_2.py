"""
2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

my_mail = open('my_file_2.txt', 'r', encoding='utf=8')
content = my_mail.read()
print(f'Содержимое файла: \n {content}')
my_mail = open('my_file_2.txt', 'r', encoding='utf=8')
content = my_mail.readlines()
print(f'Количество строк в файле: {len(content)}')
my_mail = open('my_file_2.txt', 'r', encoding='utf=8')
content = my_mail.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} строки: {len(content[i])}')
my_mail = open('my_file_2.txt', 'r', encoding='utf=8')
content = my_mail.read()
content = content.split()
print(f'Общее количество слов: {len(content)}')
my_mail.close()
