# Вводятся два целых положительных числа n и m, причем, n < m. 
# Вывести в строку через пробел квадраты целых чисел в диапазоне [n; m]. 
# Программу реализовать при помощи цикла while.

n, m = map(int, input().split())

res=[]
while n<=m:
    res.append(n**2)
    n+=1

print(*res)