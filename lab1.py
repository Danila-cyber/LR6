'''
Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)  и целевую функцию для нахождения оптимального  решения.
Вариант 20: Имеется некоторая сумма денег. Сформируйте разные варианты ее размещения в банке на К разных вкладах.
'''
import timeit
from itertools import product

# Алгоритмический вариант
def splitSumAlgoritm(summa, count, prefix=[]):
    if count == 1:
        yield prefix + [summa]
    else:
        for i in range(summa + 1):
            yield from splitSumIterTools(summa - i, count - 1, prefix + [i])

def splitSumIterTools(summa, count, limit):
    all_combinations = product(range(summa + 1), repeat=count)
    variants_func = [comb for comb in all_combinations if sum(comb) == summa]
    return variants_func

summa = int(input("Какая сумма будет на вкладах: "))
countDeposits = int(input("Сколько вкладов будет: "))

choice = input("Какой функцией выводить ответ? 1 : Алгоритмический 2 : Itertools\n- ")
if choice == '1':
    variants_alg = list(splitSumAlgoritm(summa, countDeposits))
    t_alg = timeit.timeit(lambda: splitSumAlgoritm(summa, countDeposits), number=1)
    print(f"Число вариантов (алгоритмический): {len(variants_alg)}")
    print(f"Время алгоритмический варианта: {t_alg} сек")
    for var in variants_alg:
        print(var)
elif choice == '2':
    variants_func = splitSumIterTools(summa, countDeposits)
    t_func = timeit.timeit(lambda: splitSumIterTools(summa, countDeposits), number=1)
    print(f"Число вариантов (itertools): {len(variants_func)}")
    print(f"Время функционального варианта: {t_func} сек")
    for var in variants_func:
        print(var)
