# Имеется следующее меню:
# m = '''1. Введение в Python
# 2. Строки и списки
# 3. Условные операторы
# 4. Циклы
# 5. Словари, кортежи и множества
# 6. Выход'''
# В программе вводится целое число от 1 до 6. Нужно вывести пункт меню, связанный с этим числом. Реализовать программу с использованием операторов if-elif

m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''

lst = m.split('\n')


user_input = input()
if user_input in lst[0]:
    print(lst[0])
elif user_input in lst[1]:
    print(lst[1])
elif user_input in lst[2]:
    print(lst[2])
elif user_input in lst[3]:
    print(lst[3])
elif user_input in lst[4]:
    print(lst[4])
elif user_input in lst[5]:
    print(lst[5])
elif user_input in lst[6]:
    print(lst[6])
