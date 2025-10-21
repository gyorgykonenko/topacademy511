# Периметр треугольника
# Внимание! Обязательно проверять неравенство треугольника
a = input('Введите первую сторону треугольника (А): ')
b = input('Введите вторую сторону треугольника (B): ')
c = input('Введите третью сторону треугольника (C): ')
num_a = int(a)
num_b = int(b)
num_c = int(c)
bc = num_b + num_c
num_bc = int(bc)
ab = num_a + num_b
num_ab = int(ab)
ac = num_a + num_c
num_ac = int(ac)
# Проверяем неравенство
if num_bc <= num_a:
    print ('Сторона А равна', num_a, 'и она больше сторон ВС')
if num_ab <= num_c:
    print ('Сторона С равна', num_c, 'и она больше сторон АВ')
if num_ac <= num_b:
    print ('Сторона В равна', num_b, 'и она больше сторон АС')
if num_bc <= num_a or num_ab <= num_c or num_ac <= num_b:
    print ('Такого треугольника не существует')     
else:
    print ('Периметр равен ', + num_a + num_b + num_c)
    