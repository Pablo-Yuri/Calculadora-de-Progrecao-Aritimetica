# print('calculo do N (número de termos)').
an = int(input('Digite o an: '))
a1 = int(input('Digite o valor de a1: '))
r = int(input('Digite a razão: '))
n = r
print('a{}={}+(n-1).{}'.format(an, a1, r))
n1 = an - a1
print('a{}={}+{}n-{}'.format(an, a1, r, r))
print('a{}-{}={}n-{}'.format(an, a1, r, r))
print(' {}+{}={}n'.format(n1, r, r))
n2 = n1 + r
print('{}={}n'.format(n2, r))
n3 = (n2 / r)
print('{}n={}'.format(r, n2))
print('n={}/{}\nn={}'.format(n2, r, n3))
print('O valor de N é: {}'.format(n3))
