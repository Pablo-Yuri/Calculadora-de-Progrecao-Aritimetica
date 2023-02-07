print('Calculo An')
a1 = int(input('Digite o valor de a1: '))
n = int(input('Digite o valor de n: '))
r = int(input('Digite a razão: '))
n0 = n
#print('O valor do an é (An = a1 + (n-1).r')
n1 = n-1
print('An=a1+(n-1).r\n'
      'a{}={}+({}-1).{}'.format(n, a1, n, r))
print('a{}={}+{}.{}'.format(n, a1, n1, r))
n2 = n1*r
print('a{}={}+{}'.format(n, a1, n2))
n3 = a1+n2
print('a{}={}'.format(n, n3))
print('O valor de a{} é igual a {}: '.format(n0, n3))
