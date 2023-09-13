a=int(input())
for x in range(1,20):
    if a+x>16:
        print(x,'okay')
        break
    else:
        continue
print('res: ', x+a)

b=int(input())
while b>20:
    b=b-20
print(b)

c=[1,2,3,4,5]
n=int(input())
print(c[n%5])

a=tuple(input())
for i in range (5) :
    print(a)


g=input('введите несколько символов в строку')
if g.isdigit():
   print('в строке одни цифры')
else:
    print('в строке есть буквы')
