# mystr = 'Wera'
# print(len(mystr)) 
# first = mystr[0] 
# print(first)
# Написать программу, которая выводит все буквы слова: 
# 1. В столбик 
# 2. В строчку через пробел 
# 3. В столбик в обратном порядке 
# 4*. В столбик, но все буквы маленькие
mystr = 'WORLD'
# mystr = 'World'
a = len(mystr)
a = int(a)
# print(len(mystr)) 
while a > 0:
    b = mystr[a-1] 
#   print(b, end=' ')
    print(b.lower())
    a = a - 1