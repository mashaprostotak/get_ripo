__author__ = 'Еремеева М.О.'
print(-1>999999)
p=int(input("введите число"))
i=1
r1=0
#ищем максимальный разряд
while (p//i)>0:
    i=i*10

#сравниваем цифры друг с другом (в такой последовательности, потому что просто программу из easy  переделала)
    
while (i/10)>=1:
    r=p//(i/10)
    p=p-r*(i/10)
    i=i/10
    if (r>r1):
        r1=r
#выводим самую большую           
print (int(r1))
    
    


# Задача-2: 

thisdict = {"x":float(input("vvedite pervoe chislo")),
                "y":float(input("vvedite vtoroe chislo"))}
            
x=thisdict["y"]
y=thisdict["x"]

print(x,y)

# Задача-3:
from math import sqrt
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if ((b**2-4*a*c)<0):
    print("nevozmozhno")
else:
    d=sqrt(b**2-4*a*c)
    x1=(d-b)/(2*a)
    x2=((-1)*d-b)/(2*a)
    if ((b**2-4*a*c)==0):
        print (x1)
    else:
        print(x1,x2)
