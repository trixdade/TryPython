import numpy as np
import math as m
import matplotlib.pyplot as plt
from collections import Counter
from prettytable import PrettyTable

# rand(p) - returns 0 or 1 with probability p
def rand_0_or_1(probability):
    np.random.seed()
    if np.random.random() > probability:
        return 0
    else:
        return 1

# печать таблицы
def printTable(data, thead):
    table1 = PrettyTable(thead)
    tdata = data[:]
    columns = len(thead)
    while tdata:
        table1.add_row(tdata[:columns])
        tdata = tdata[columns:]
    print(table1)

# нахождение медианы в выборке
def findMediana(mass):
    if len(mass)%2 == 0:
        mass.sort()
        return (mass[len(mass)//2] + mass[(len(mass)//2) + 1])/2
    else:
        mass.sort()
        return mass[len(mass)//2] 
    
# Program starts
p = float(input("Enter probability value: "))
n = int(input("Enter number of experiments: "))

numbers = []
# generate number 0 or 1 with probability 'p' of 1
for x in range(0, n):
    c = 0
    i = 0
    while i != 1:
        i = rand_0_or_1(p)
        c += 1
    numbers.append(c)

Data = [] # здесь будут все данные для таблицы
c = Counter(numbers) # считаем количество каждого элемента в numbers
maximum = max(c) # максимальная случайная величина
for x in range(1, maximum + 1):
    d = dict(c)
    Data.append(x) # сначала добавляем значение СВ
    Data.append(d.get(x, 0)) # количество выпадений СВ X, если нет, то 0
    Data.append(round(d.get(x, 0)/n, 3)) # частота СВ 
        
        
thead = ["Value", "Amount", "Freq"] # задаем заголовки столбцов
printTable(Data, thead) # печатаем таблицу 1

# подготовка структур данных для таблицы
E = []
E_exp = []
E_diff = []
E_lib = []
D = []
D_exp = []
D_diff = []
Me_exp = []
R_exp = []
table = PrettyTable()

# создаем названия колонок
table.add_column("E",[E])
table.add_column("E_exp", [E_exp])
table.add_column("E_diff", [E_diff])
table.add_column("E_lib", [E_lib])
table.add_column("D", [D])
table.add_column("D_exp", [D_exp])
table.add_column("D_diff", [D_diff])
table.add_column("Me_exp", [Me_exp])
table.add_column("R_exp", [R_exp])

E.append(round(1/p,3)) # теоретическое мат ожидание
E_exp.append(round(np.mean(numbers), 3)) # выборочное среднее
E_diff.append(round(m.fabs(1/p - np.mean(numbers)), 5)) # разница
E_lib.append(round(np.mean(np.random.geometric(p, n)), 5)) # мат ожидание из библиотеки
D.append(round((1-p)/(p*p), 3)) # дисперсия


# подсчет выборочной дисперсии 
s = 0
M = np.mean(numbers) # выборочное среднее для вычисления выборочной дисперсии
for xi in numbers:
    #print('x = ', round(xi,3))
    #print('x - M = ', round(xi-M,3))
    #print('(x - M)^2 = ', round((xi-M)*(xi-M),3))
    s = s + (xi - M)*(xi - M)
    #print('s = ', round(s,3))
    
D_exp.append(round(s/n,5)) # выборочная дисперсия 
D_diff.append(round(np.fabs(D_exp[0] - D[0]),5)) # разница
Me_exp.append(findMediana(numbers)) # медиана

R_exp.append(max(numbers)-min(numbers)) # разность макс и мин значений в выборке

print(table)  # Печатаем таблицу 2

y2 = [] # понадобится для построения графика F_exp
Data2 = [] # вся информация для третьей таблицы
difference = [] # понадобится для подсчета максимальной разницы в выборке
c = Counter(numbers)
maximum = max(c)
for x in range(1, maximum + 1):
    d = dict(c)
    Data2.append(x)
    Data2.append(round((1-p)**(x-1) * p, 5)) # теоретическая вероятность
    Data2.append(round(d.get(x, 0)/n, 5)) # частота
    difference.append(((1-p)**(x-1) * p) - d.get(x, 0)/n)
    y2.append(d.get(x, 0)/n)
        
max_diff = max(difference)    

thead = ["Value", "Probability", "Freq"]
printTable(Data2, thead) # печатаем таблицу 3

print('Max difference = ', round(max_diff, 5))

y1 = [] # понадобится для построения графика F
summ = 0
x = range(1, maximum + 1)
for value in range(0, maximum):
    summ += (1-p)**value * p
    y1.append(summ)
    
# получаем значения интегральной функции F_exp
for i in range(1, len(y2)): 
    y2[i] = y2[i] + y2[i-1] 

# построение графиков
fig, ax = plt.subplots()
ax.plot(x, y1, color="blue", label="F(x)")      
ax.plot(x, y2, color="red", label="F_exp(x)")  
plt.title("F and F_exp graph")     
ax.set_xlabel("x")                             
ax.set_ylabel("y")                             
ax.legend() 


# исправить график СВ
# посмотреть как выводится формула мат ожидания и дисперсии для СВ