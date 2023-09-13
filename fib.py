print('Введите число:')
def f(n):
    f1=1
    f2=0
    while True:
        if f2<=n:
            if f2==n:
                return 'Принадлежит'
            else:
                predf=f2
                f2+=f1
                f1=predf
        else:
            return 'Не принадлежит'
            break
print(f(int(input())))

