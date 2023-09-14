import math
v='-'
z='.'
a=False
while a==False:
   a=input('введите число: ')
   if a.isdigit():
     a=int(a)
     break
   else:
      if v in a:
         if z in a:
             a=float(a)
             break
         else:
            a=int(a)
            break
      else:
        a=False
print('для сложения введите +')
print('для вычитания введите -')
print('для умножения введите *')
print('для деления введите /')
print('для возведения в степень введите **')
print('для ввыведения остатка при делении введите %')
print('для целочисленного деления введите //')
print('для округления введите okr')
print('для выведения логарифма введите log')
m=['-','+','/','*','**','//','%','log','okr+','okr-']
w=['okr+','okr-']
b=False
while b==False:
    b=input('введите символ: ')
    if b in m:
      if b in w:
        print('ведите в следующую строку любое число')
        break
      else:
        break
    else:
      b = False
c=False
while c==False:
   c=input('введите число: ')
   if c.isdigit():
    c = int(c)
    break
   else:
     if v in c:
         if z in c:
            c = float(c)
            break
         else:
            a=int(a)
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








