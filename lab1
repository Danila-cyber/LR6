'''
Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)  и целевую функцию для нахождения оптимального  решения.
Вариант 20: Имеется некоторая сумма денег. Сформируйте разные варианты ее размещения в банке на К разных вкладах
'''
import itertools

def locate(remains, depos, numsDepos, currDepos, results):
    if remains == 0:
        results.append(list(currentDeposits))
        return
    if depos >= numsDepos or remains < 0:
        return
    for i in range(remains + 1):
        currentDeposits[depos] = i  
        locate(remains - i, depos + 1, numsDepos, currDepos, results) 

def locateIterTools(summ, countDepos):
    for i in itertools.combinations_with_replacement(range(summ + 1), countDepos):
        if sum(i) == summ:
            yield i

summa = int(input("Какая сумма будет на вкладах: "))
countDeposits = int(input("Сколько вкладов будет: "))


choice = input("Какой функцией выводить ответ? 1 : Алгоритмический 2 : Itertools\n- ")
if choice == '1':
    print("Результат работы собственное функции")
    currentDeposits = [0] * countDeposits
    results = []
    for i in results:
        print(i)
    print(f"Общее количество вариантов: {len(results)}")
elif choice == '2':
    print('Результат работы функции itertools')
    results = list(locateIterTools(summa, countDeposits))
    for i in results:
        print(i)
    print(f"Общее количество вариантов: {len(results)}")
