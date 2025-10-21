from random import randint
a = randint(1, 10)
b = randint(1, 10)
contin = 1
zadani = 0
verno = 0
neverno = 0
num_zadani = input ('Введите количество заданий: ')
num_zadani = int(num_zadani)
while contin == 1:
    result = a + b
    answer = int(input('Сколько будет %(a)i + %(b)i = ' % {
     'a': a, 'b': b }))
    if answer != result:
        neverno = neverno + 1
        print('Нет, попробуй ещё раз! Отгадал неверно', neverno)
        contin = 1
        zadani = zadani + 1
    else:    
        verno = verno + 1
        print ('Верно!!! Отгадал верно', verno)
        contin = 1
        zadani = zadani + 1
    a = randint(1, 10)
    b = randint(1, 10)
    procent = ((neverno - verno) / neverno) * 100
    print ('Процент ошибки', procent,'%')
print ('Конец')