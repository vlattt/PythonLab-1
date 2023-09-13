import math
print('Для сложения введите +')
print('Для вычитания введите -')
print('Для умножения введите *')
print('Для деления введите /')
print('Для возведения в степень введите **')
print('Для ввыведения остатка при делении введите %')
print('Для целочисленного деления введите //')
print('Для округления введите okr+/okr-')
print('Для выведения логарифма введите log')
m=['-','+','/','*','**','//','%','log']
w=['okr+','okr-']
b=False
while b==False:
    b=input('Введите функцию: ')
    if b in m:
      if b in w:
        print('Введите число')
        break
      else:
        break
    else:
      b = False
v='-'
z='.'
a=False
while a==False:
   a=input('Введите первое число: ')
   if a.isdigit():
     a=int(a)
     break
   else:
      if z in a:
       a = float(a)
      else:
        a=False
c=False
while c==False:
   c=input('Введите второе число:')
   if c in w:
      break
   if c.isdigit():
    c = int(c)
    break
   else:
     if z in c:
       c = float(c)
     else:
       c=False
print(a,b,c,"=")
if b == '+':
    print(a+c)
elif b == '-':
    print(a-c)
elif b == '/':
    print(a/c)
elif b == '*':
    print(a*c)
elif b =='**':
    print(a**c)
elif b =='//':
    print(a//c)
elif b == '%':
    print(a % c)
elif b =='log':
    print(math.log(a,c))
elif b =='okr+':
    print(math.ceil(a))
elif b =='okr-':
    print(math.floor(a))








