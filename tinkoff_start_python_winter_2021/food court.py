"""Даня в обеденный перерыв ходит в одно и то же кафе. Ему, как сотруднику банка, положено специальное предложение: при каждой покупке больше, чем на 100 рублей,
Даня получает купон на бесплатный обед. Даня узнал стоимость своих обедов на ближайшие n дней. Ему хочется минимизировать свои затраты, грамотно используя талоны.
Требуется найти минимальные суммарные Данины затраты на обеды.
Формат входных данных
В первой строке дается натуральное число n (0≤n≤100). В каждой из n строк записана стоимость обеда в каждый из дней (неотрицательное целое число, не большее, чем 300).
Формат результата
В первой строке выдайте минимально возможную суммарную стоимость обедов.
"""

n = int(input())
sum_lunch = 0  # итоговая сумма за обеды
lunches = []
extra = 0
flag = 'F'
for i in range(n):
    x = int(input())  # цена за очередной обед
    lunches.append(x)
for i in range(len(lunches)):
    if extra == 0:
        sum_lunch += lunches[i]
    elif extra > 0 and lunches[i] == max(lunches[j + 1:]):
        extra -= 1
        if lunches[i] > 100:
            flag = 'T'
    else:
        sum_lunch += lunches[i]
    if lunches[i] > 100 and flag != 'T':
        extra += 1
        j = i
        flag = 'F'

sum_lunch_alt = 0
extra_a = 0
lunches_p = []
for i in range(len(lunches)):
    if lunches[i] > 100:
        extra_a += 1
        lunches_p.append(i)
        sum_lunch_alt += lunches[i]
j = 0
lunches1 = []
for i in lunches:
    if i <= 100:
        lunches1.append(i)
for j in range(len(lunches_p)):
    for i in range(len(lunches)):
        if lunches1 != []:
            if lunches[i] == max(lunches1):
                k = i
    fl = False
    for i in lunches_p:
        if k > i:
            fl = True
            lunches_p.remove(i)