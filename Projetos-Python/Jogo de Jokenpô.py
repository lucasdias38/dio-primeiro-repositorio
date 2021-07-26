from random import randint
print('Vamos jogar um jogo de Jokenpô, o famoso Pedra, Papel ou tesoura!')
print('0 - Pedra\n1 - Papel\n2 - Tesoura')
a = int(input('Segue os numeros de 0 á 2 para a sua escolha: '))
b = int(randint(0,2))
jogo = ['Pedra', 'Papel','Tesoura']
#          0        1        2
print('\nVocê escolheu {}'.format(jogo[a]))
print('O Computador escolheu {}\n'.format(jogo[b]))
if (a == 2 and b == 1) or (a == 1 and b == 0) or (a == 0 and b == 2):
    print('Parabéns, você ganhou!')
elif a == b:
    print('O jogo Empatou')
else:
    print('Você perdeu!')


