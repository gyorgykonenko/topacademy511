# Написать программу, которая выводит все буквы слова: 
# 1. В столбик
#for s in 'World':
#    print(s) 
# 2. В строчку через пробел 
#for s in 'World':
#    print(s, end=' ')
#    print('\n ')
# 3. В столбик в обратном порядке
#myworld = 'World'
for s in range(len('World') - 1, -1, -1):
    print('World'[s]) 
# 4*. В столбик, но все буквы маленькие
#for s in 'WORLD':
#    print(s.lower())

