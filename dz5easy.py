# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
import os
def sozd(naz):
    dir_path = os.path.join(os.getcwd(), naz)
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')
for i in range(1,10):
    naz='dir'+str(i)
    sozd(naz)
    
    

# И второй скрипт, удаляющий эти папки.
def udal(m):
    dir_path = os.path.join(os.getcwd(), m)
    try:
        os.rmdir(dir_path)
    except:
        print('Такая директория уже не существует')
pass
for i in range(1,10):
    m='dir'+str(i)
    udal(m)
    

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def prosm():       
    files = os.listdir(os.getcwd())
    print(files)
pass
print(prosm())
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

path1=os.path.basename('dz5easy.py')

fi=open(path1,"r")
k=fi.read()
fi.close()
fi2=open("kopiya.py", "x")
fi2.close()
f=open("kopiya.py", "w")
f.write(k)
f.close()
