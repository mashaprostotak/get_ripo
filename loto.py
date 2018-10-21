import random

poolchisel = list(range(1, 91))
kartochkakompa = random.sample(poolchisel, 15)
kartochkakompa_sorted = sorted(kartochkakompa)
kartochkaigroka = random.sample(poolchisel, 15)
kartochkaigroka_sorted = sorted(kartochkaigroka)


def display_cards():
    print("Вот карточка компьютера:\n")
    print('\n',kartochkakompa_sorted[0:5],'\n',kartochkakompa_sorted[5:10],"\n",kartochkakompa_sorted[10:16])
    print("///////////////////////////////////")
    print("\nВот карточка игрока:\n")
    print('\n',kartochkaigroka_sorted[0:5],'\n',kartochkaigroka_sorted[5:10],"\n",kartochkaigroka_sorted[10:16])


def sluchayniy():
    chislo = random.choice(poolchisel)
    poolchisel.remove(chislo)
    return chislo


def igra():
    while poolchisel:
        choice = sluchayniy()
        print("Случайне число: " + str(choice))
        display_cards()
        danet = input("вычеркнуть?")
        danet=danet.upper()
        
        
        if danet == "ДА":
            if choice in kartochkakompa_sorted:
                kartochkakompa_sorted.remove(choice)
            elif choice in  kartochkaigroka_sorted:
                kartochkaigroka_sorted.remove(choice)
            else:
                print("вы проиграли! такого числа нет на карточке!")
                break
            
        if danet == "НЕТ":
            if choice in kartochkakompa_sorted:
                kartochkakompa_sorted.remove(choice)
            if choice in kartochkaigroka_sorted:
               print("вы проиграли! это число у вас на карте")
            else:
                continue
    else:
        if len(kartochkaigroka_sorted) == 0:
            print("ВЫ ВЫИГРАЛИ УРА!")
        elif len(kartochkakompa_sorted) == 0:
            print("Компьютер одержал победу !")
        

igra()
