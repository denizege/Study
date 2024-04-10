# Вводятся целые числа в одну строчку через пробел. 
# Необходимо преобразовать эти данные в список целых чисел. 
# Затем, перебрать этот список в цикле for и просуммировать все нечетные значения. 
# Результат вывести на экран.


numbers = list(map(int, input().split()))

numbers_sum = 0
for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        numbers_sum += numbers[i]
print(numbers_sum)
