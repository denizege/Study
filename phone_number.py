# Вводится строка с номером телефона. Ожидается формат ввода:
# +7(xxx)xxx-xx-xx
# где x - это цифра. Размер введенных символов считается верным (то есть, не может быть, чтобы отсутствовала какая-либо цифра или была лишняя). 
# Необходимо проверить, что введенная строка соответствует этому формату. Вывести ДА, если соответствует и НЕТ - в противном случае.


phone_number = input()
expected_format = "+7(xxx)xxx-xx-xx"

res = 'ДА'

if len(phone_number) != len(expected_format):
    res = 'НЕТ'
    
for i, expected_char in enumerate(expected_format):
    if expected_char == 'x':
        if not phone_number[i].isdigit():
            res = "НЕТ"
            break
    else:
        if expected_char != phone_number[i]:
            res = "НЕТ"
            break
    
print(res)
