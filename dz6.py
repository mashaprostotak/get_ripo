# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Tr:
    
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1=float(x1)
        self.y1=float(y1)
        self.x2=float(x2)
        self.y2=float(y2)
        self.x3=float(x3)
        self.y3=float(y3)
        self.AB=math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
        self.BC=math.sqrt((self.x3-self.x2)**2+(self.y3-self.y2)**2)
        self.AC=math.sqrt((self.x3-self.x1)**2+(self.y3-self.y1)**2)
        

    def ploshad(self):
        p=(self.AB+self.AC+self.BC)/2
        plosh=math.sqrt(p*(p-self.AB)*(p-self.BC)*(p-self.AC))
        return plosh
    def vysota(self):
        p=(self.AB+self.AC+self.BC)/2
        plosh=math.sqrt(p*(p-self.AB)*(p-self.BC)*(p-self.AC))
        return plosh/0.5/self.AB
    def perimetr(self):
        
        return self.AB+self.BC+self.AC

treugolnik1=Tr(-5,2,7,-7,5,7)
print(treugolnik1.ploshad())
print(treugolnik1.vysota())
print(treugolnik1.perimetr())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.





class Trapezia:
    def __init__(self,x1, y1, x2, y2, x3, y3,x4,y4):
        self.x1=float(x1)
        self.y1=float(y1)
        self.x2=float(x2)
        self.y2=float(y2)
        self.x3=float(x3)
        self.y3=float(y3)
        self.x4=float(x4)
        self.y4=float(y4)
        self.AB=math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
        self.BC=math.sqrt((self.x3-self.x2)**2+(self.y3-self.y2)**2)
        self.AD=math.sqrt((self.x4-self.x1)**2+(self.y4-self.y1)**2)
        self.CD=math.sqrt((self.x4-self.x3)**2+(self.y4-self.y3)**2)

    def proverka(self):
        #условие что две стороны равны, а две другие параллельны
        #поскольку неизвестно как расположена трапеция, нужно учесть все варианты
        if (self.AB==self.CD and (self.x4-self.x1==self.x3-self.x2) ) or (self.BC==self.AD and (self.y2-self.y1==self.y3-self.y4)  ) :
            print("существует")
        else:
            print("не существует")
            
    def storonitr(self):
        print ("AB=", self.AB, '\n',"BC=", self.BC, '\n', "CD=", self.CD, '\n', "AD=", self.AD)

    def perimetrtr(self):
        print (self.AB+self.BC+self.CD+self.AD)

    def ploshadtr(self):
        #площадь трапеции через четыре стороны
        if self.AB==self.CD:
            a=self.BC
            b=self.AD
            c=self.CD
            d=self.AB
            
        if self.BC==self.AD:
            a=self.CD
            b=self.AB
            c=self.BC
            d=self.AD
        p1=(a+b)/2
        p2=((b-a)**2+c**2-d**2)/(2*(b-a))
        p3=math.sqrt(c**2-p2**2)
        p4=p1*p3
        print (p4)

trap1=Trapezia(0,0,14,0,11,5,3,5)
trap1.storonitr()
trap1.proverka()
trap1.ploshadtr()
trap1.perimetrtr()
















        
