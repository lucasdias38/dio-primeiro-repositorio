a = int(input('Digite o numero para realizar a tabuada: '))
for i in range (1,11):
    print('{} * {:2} = {}'.format(a, i, (a * i)))