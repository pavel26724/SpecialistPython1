# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    # TODO: your code here
    pass


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

def lucky_ticket(ticket_number):
    if int(str(ticket_number)[0]) + int(str(ticket_number)[1]) + int(str(ticket_number)[2]) \
            == int(str(ticket_number)[-1]) + int(str(ticket_number)[-2]) + int(str(ticket_number)[-3]):
        return ('Билет счастливый')
    else:
        return ('Билет НЕсчастливый')


# Тестируем функцию
print(lucky_ticket(123312))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
