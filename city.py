# Вводится список названий городов в одну строчку через пробел. 
# Определить, что в этом списке все города имеют длину более 5 символов. 
# Реализовать программу с использованием цикла while и оператора break. 
# Вывести ДА, если условие выполняется и НЕТ - в противном случае.


city = input().split()

i = 0
while i < len(city):
    if len(city[i]) <= 5:
        print('No')
        break
    i += 1
else:
    print('Yes')
