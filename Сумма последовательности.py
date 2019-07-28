# Курс основы программирования на Python
# Задание по программированию: Сумма последовательности
# 08.05.2019
#
# Дана последовательность чисел, завершающаяся числом 0. Найдите сумму всех этих чисел, не используя цикл.
#
# Формат ввода
#
# Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в
# последовательность не входит, а служит как признак ее окончания).
#
# Формат вывода
#
# Выведите ответ на задачу.

def sum_inp():
    num = int(input())
    if num == 0:
        return num
    num = num + sum_inp()
    return num


print(sum_inp())
