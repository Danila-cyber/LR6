'''
Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)  и целевую функцию для нахождения оптимального  решения.
Вариант 20: Имеется некоторая сумма денег. Сформируйте разные варианты ее размещения в банке на К разных вкладах.
# Ограничение: все вклады должны быть кратны 2 (чётные) -> уменьшает переборы
'''
import timeit
from itertools import combinations_with_replacement

# Целевая функция: минимизируем разброс вкладов (сумму отклонений от среднего)
def objective(arr):
    avg = sum(arr) / len(arr)
    return sum(abs(x - avg) for x in arr)

# Алгоритмический вариант (рекурсивный перебор c ограничением кратности D)
def splitSumAlgoritm(summa, count, limit, prefix=[]):
    if count == 1:
        if summa % limit == 0:
            yield prefix + [summa]
    else:
        min_val = 0
        max_val = summa - (count - 1) * min_val
        for i in range(min_val, max_val+1, limit):
            yield from splitSumAlgoritm(summa - i, count - 1, limit, prefix + [i])

def splitSumIterTools(summa, count, limit):
    candidates = [x for x in range(0, summa + 1, limit)]
    variants_func = [comb for comb in combinations_with_replacement(candidates, count) if sum(comb) == summa]
    return variants_func

summa = int(input("Какая сумма будет на вкладах: "))
countDeposits = int(input("Сколько вкладов будет: "))
limit = 2

choice = input("Какой функцией выводить ответ? 1 : Алгоритмический 2 : Itertools\n- ")
if choice == '1':
    variants_alg = list(splitSumAlgoritm(summa, countDeposits, limit))
    t_alg = timeit.timeit(lambda: splitSumAlgoritm(summa, countDeposits, limit), number=1)
    best_alg = min(variants_alg, key=objective)
    print(f"Число вариантов (алгоритмический): {len(variants_alg)}")
    print(f"Лучшее распределение (алгоритмический): {best_alg} с отклонением {objective(best_alg):.2f}")
    print(f"Время алгоритмический варианта: {t_alg} сек")
elif choice == '2':
    variants_func = splitSumIterTools(summa, countDeposits, limit)
    t_func = timeit.timeit(lambda: splitSumIterTools(summa, countDeposits, limit), number=1)
    best_func = min(variants_func, key=objective) if variants_func else None
    print(f"Число вариантов (itertools): {len(variants_func)}")
    print(f"Лучшее распределение (itertools): {best_func} с отклонением {objective(best_func):.2f}")
    print(f"Время функционального варианта: {t_func} сек")
