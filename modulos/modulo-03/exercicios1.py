# imports
import math
from sympy import *
from sympy.solvers import solve

# Exercício 01 - Crie uma função em Python que retorne o resultado do polinômio abaixo. Em seguida, defina x = 3 e execute a função
# p(x) = x^4 - 4 * x² + 3x

p = lambda x: (x ** 4 - 4 * x ** 2 + 3 * x)

print(p(3))

# Exercício 2 - Dado o polinômio ax^3 + bx^2 + cx + d, solicite que o usuário digite o valor dos 4 coeficientes e o valor de x e resolva o polinômio.
# Dica 1: Use a função pow() do pacote math para representar operações de potência.
# Dica 2: Armazene os coeficientes digitados em uma lista Python.

# ax^3 + bx^2 + cx + d



a = 3 # float(input('Informe o valor do coeficiente a: '))
b = 7 # float(input('Informe o valor do coeficiente b: '))
c = 1 # float(input('Informe o valor do coeficiente c: '))
d = 2 # float(input('Informe o valor do coeficiente d: '))
x = 5 # float(input('Informe o valor de x: '))

coeficientes = [d, c, b, a]

sum1 = 0

for i, valor in enumerate(coeficientes):
    if i == 0:
        sum1 += valor
    else:
        sum1 += valor * pow(x, i)

print(sum1)

# Exercício 3 - Usando o Sympy, resolva a equação x² + 2x - 8 = 0
init_printing()


x = Symbol('x')
solve(x ** 2 + 2 * x - 8, x)

# Exercício 4 - use o sympy para apresentar a equação ax² + bx + c = 0 em seu formato simbolico
a, b, c = symbols('a b c')
x = Symbol('x')

eq = a * x ** 2 + b * x + c
solve(eq, x)

# Exercício 5 - Use "subs" do sympy, para plugar os valores, 1, 2, e -8 para os coeficientes abc na equação
# do exercício 4
r_eq = solve(eq, x)
r_eq[0].subs({'a': 1, 'b': 2, 'c': -8})
r_eq[1].subs({'a': 1, 'b': 2, 'c': -8})

# Exercício 6 - Usando a função expand() do sympy, encontre a versão extendida do polinômio P
# P = (x - 1) * (x - 2) * (x - 3)

x = Symbol('x')
eq = (x - 1) * (x - 2) * (x - 3)

eq = eq.expand()
eq = eq.factor()
eq.simplify()

roots = solve(eq, x)
simplify(eq - ((x-roots[0]) * (x-roots[1]) * (x-roots[2])))


I * I
help(I)
x = Symbol('x')
solve(x ** 2 + 1, x)
z = 4 + 3* I
z

# Exercício 7 - Pesquise na documentação do Sympy as funções necessárias para extrair
# o módulo (valor absoluto de z e seu argumento)
Abs(z)
arg(z)

# Exercício 8 - Desafio e pesquisa
# A formula Euler mostra uma relação importante entre a função exponencial e^x e as funções
# trigonométricas sin(x) e cos(x)
# e^ix = cos(x) + i sin(x)

x = symbols('x', real = True)
exp(I * x).expand(complex=True)
 
# Exercicio 9 - Resolva o sistema de equações lineares abaixo usando a função solve() do sympy
x, y, z = symbols('x y z')
eq1 = x + y + z
eq2 = x + y + 2 * z

solve([eq1-1, eq2-3], (x, y, z))


# Exercicio 10 - Encontre o logaritmo de 1.5 na base 2, base 10 e logaritmo natural
math.log(1.5)
math.log2(1.5)
math.log(1.5, 2)
math.log10(1.5)
math.log(1.5, 10)


