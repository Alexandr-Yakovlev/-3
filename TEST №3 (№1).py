# Задача №1 (гр. 201. Яковлев АА)
def Num_cart(a):
    a = str(a)
    a1 = a[0:12]
    a2 = a[12:]
    b = []
    for i in a1:
        i = '*'
        b.append(i)
    for i in a2:
        b.append(i)
    print(b)
a = int(input('введите 16-и значный номер карты: '))
a = str(a)
if len(a) == 16:
    Num_cart(a)
else:
    print('Ввели несуществующий номер')