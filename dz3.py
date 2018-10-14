# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number=str(number)[:(ndigits+3)]
    if (int(number[-1]))>=5:
        number=float(number[:-1])+0.1**ndigits
    else:
        number=float(number[:-1])
    return number    
    pass


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    summ1=0
    summ2=0
    for i in range(3):
        summ1=summ1+int(str(ticket_number)[i])
    for j in str(ticket_number)[3:7]:
        summ2=summ2+int(j)
    if summ1==summ2:
        return ("счастливый")
    else:
        return ("попробуйте еще раз")    
    pass


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
