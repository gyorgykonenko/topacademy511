from random import randint
a = randint(1, 10)
b = randint(1, 10)
kolvo = 1
zadani = 0
verno = 0; neverno = 0
kolvo_zadani = input ('Введите количество заданий: ')
kolvo_zadani = int(kolvo_zadani)
while kolvo <= kolvo_zadani:
        result = a + b
        answer = int(input('Сколько будет %(a)i + %(b)i = ' % {
         'a': a, 'b': b }))
        if answer != result:
            neverno = neverno + 1
            print('Нет, попробуй ещё раз! Отгадал неверно', neverno, 'раз')
        else:    
            verno = verno + 1
            print ('Верно!!! Отгадал верно', verno, 'раз')
        a = randint(1, 10)
        b = randint(1, 10)
        kolvo = kolvo + 1
procent = ((neverno - verno) / neverno) * 100
print ('Процент ошибки', procent,'% из', kolvo - 1, 'попыток')
print ('Конец')