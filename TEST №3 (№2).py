# Задача №2. гр. 201, Яковлев АА.
def fun_palindrom(a):
    print(a)
    b = a[::-1]
    if a == b:
        print('Палиндром')
    else:
        print('Не палиндром')


a = str(input('Введите слово: '))
fun_palindrom(a)