# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

frukti=['apple','pear','watermelon','kiwi']
a=0
for i in frukti:
    a+=1
    print(a,'. ',format(i,'>'),sep="")
    
# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
frukti=['apple','pear','watermelon','kiwi']
yagodi=['strawberry','blueberry', 'watermelon']
for i in frukti:
    for m in yagodi:
        if m==i:
            frukti.remove(m)
print(frukti)        
    
# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
list=[1,6,88,76,53]
list2=[]
for k in list:
    if (k%2)==0:
        list2.append(float(k/4))
    else:
        list2.append(k*2)
print(list,'\n',list2)        
