'''
Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)  и целевую функцию для нахождения оптимального  решения.
Вариант 20: Имеется некоторая сумма денег. Сформируйте разные варианты ее размещения в банке на К разных вкладах.
Ограничение: На вклад нельзя положить сумму меньше, чем 25% от всей суммы.
'''
import itertools

def locate(summ, countDepos, varr, results):
    if countDepos == 0:
        if summ == 0:
            results.append(varr[:])
        return

    for i in range(summ + 1):
        varr.append(i)  
        locate(summ - i, countDepos - 1, varr, results)
        varr.pop()

def locateIterTools(summ, countDepos):
    results = []
    for i in itertools.combinations_with_replacement(range(summ+1), countDepos):
        if sum(i) == summ:
            results.append(list(i))
    for i in itertools.combinations_with_replacement(range(summ, 0-1, -1), countDepos):
        if sum(i) == summ:
            results.append(list(i))
    return results

summa = int(input("Какая сумма будет на вкладах: "))
countDeposits = int(input("Сколько вкладов будет: "))

choice = input("Какой функцией выводить ответ? 1 : Алгоритмический 2 : Itertools\n- ")
if choice == '1':
    print("Результат работы собственное функции")
    currentDeposits = [0] * countDeposits
    results = []
    locate(summa, countDeposits, [], results)
    for i in results:
        print(i)
    print(f"Общее количество вариантов: {len(results)}")
elif choice == '2':
    print('Результат работы функции itertools')
    res = locateIterTools(summa, countDeposits)
    for i in res:
        print(i)
    print(f"Общее количество вариантов: {len(res)}")

