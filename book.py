# Вводится информация по книге (каждое значение с новой строки): название, автор, число страниц (целое число), цена (вещественное число). 
# На основе этих данных формируется список book с элементами в порядке их ввода. 
# Затем, из этого списка необходимо удалить 3-й элемент (число страниц), в качестве автора записать "Пушкин" и цену увеличить в 2 раза. 
# Результат вывести на экран командой: print(book)


title = input()
author = input()
number = int(input())
price = float(input())

new_price = price*2

book = [title, author, number, price]
book[3] = new_price
book[1] = 'Пушкин'
del(book[2])

print(book)
