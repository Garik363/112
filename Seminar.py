# задача 1 Найдите сумму цифр трехзначного числа.
#  *Пример:*
#  123 -> 6 (1 + 2 + 3)
#  100 -> 1 (1 + 0 + 0) |
# n = input("Введите трехзначное число: ")
# n = int(n)
 
# d1 = n % 10
# n = n // 10
# d2 = n % 10
# n = n // 10
 
# print("Сумма цифр числа:", n + d1 + d2)

# задача 2 Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10
s = int(input("Введите количество сделанных журавликов: "))
ser = s / 6
p = ser
k = (ser + p) * 2
print("Сережа сделал:", int(ser), "Катя сделала:", int(k), "Петя сделал:", int(p))
