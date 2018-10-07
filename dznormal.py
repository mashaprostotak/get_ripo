# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n,m):
    lst=[1,1]
    for i in range(2,m):
        p=lst[i-2]+lst[i-1]
        lst.append(p)   
    print(lst[(n-1):m])   
pass

fibonacci(3,5)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for i in range(len(origin_list)):
        for j in range(i + 1, len(origin_list)):
            if origin_list[i] > origin_list[j]:
               origin_list[i], origin_list[j] = origin_list[j], origin_list[i]        
    print(origin_list)        
    pass

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

list1=[-5,-2,7,8,6,-10,-12,5,6,666]
def polozhitelno(lst):
    newlist=[]
    for i in lst:
        if i<0:
            newlist.append(i)
    for i in newlist:
        lst.remove(i)
    return(lst)

def myfilter(func,lst):
       print(func(lst))
myfilter(polozhitelno,list1)
        
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
a1=input('введите координаты А1 через запятую ')
a2=input('введите координаты А2через запятую')
a3=input('введите координаты А3через запятую')
a4=input('введите координаты А4через запятую')
listx=[]
listy=[]
for i in range(len(a1)-1):
    if a1[i]==',':
        x1=a1[:i]
        listx.append(int(x1))
        y1=a1[(i+1):]
        listy.append(int(y1))
for i in range(len(a2)-1):
    if a2[i]==',':
        x2=a2[:i]
        listx.append(int(x2))
        y2=a2[(i+1):]
        listy.append(int(y2))
for i in range(len(a3)-1):
    if a3[i]==',':
        x3=a3[:i]
        listx.append(int(x3))
        y3=a3[(i+1):]
        listy.append(int(y3))
for i in range(len(a4)-1):
    if a4[i]==',':
        x4=a4[:i]
        listx.append(int(x4))
        y4=a4[(i+1):]
        listy.append(int(y4))
#упорядочиваем значения х точек, чтобы определить их расположение слева направо в координатной системе
#сравниваем разницу соседних точек по х
#ищем соответствующием им у и сравниваем их
if (sorted(listx)[1]-sorted(listx)[0])==(sorted(listx)[3]-sorted(listx)[2]):
    for i in range(len(listx)):
        if listx[i]==sorted(listx)[0]:
                ay=listy[i]
        if listx[i]==sorted(listx)[1]:
                dy=listy[i]
        if listx[i]==sorted(listx)[3]:
                cy=listy[i]
        if listx[i]==sorted(listx)[2]:
                by=listy[i]
    if (dy-ay)==(cy-by):
        print('праллелограмм возможен')
else:
    print('такой параллелограм не существует')
