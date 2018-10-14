from dz5easy import prosm  as d
from dz5easy import udal  as u
from dz5easy import sozd  as s 
import os
a=int(input('введите цифру действия:''\n'
        '1. Перейти в папку''\n'
        '2. Просмотреть содержимое текущей папки''\n'
        '3. Удалить папку''\n'
        '4. Создать папку'))
if a!=2:
    b=input('введите имя папки')
    if a==1:
        path1=os.path.join(os.getcwd(), b)
        try: os.chdir(path1)
        except: print('нет такой')
        else: print('успешно перешел') 
    if a==3:
        try: u(b)
        except:print('невозможно удалить')
        else: print('успешно удалил') 
    if a==4:
        try: s(b)
        except:print('невозможно создать')
        else: print('успешно создал')
else:
    d()
