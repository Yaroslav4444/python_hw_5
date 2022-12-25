"""
5) Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле
 и выводить ее на экран.
"""

my_txt = open('task_5.txt', 'w', encoding='utf=8')
print("Введите числа через пробел: ")
while True:
    text = input()
    my_txt.write(text + '\n')
    if text == "":
        break

my_txt = open('task_5.txt', 'r', encoding='utf=8')
my_list = my_txt.read().split()
total = 0
for el in my_list:
    total += float(el)
print("Сумма чисел в файле: ", total)
my_txt.close()
