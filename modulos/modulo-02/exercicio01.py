import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

#%% Resolvendo sistemas de equações em python
# Usando numpy podemos resolver sistemas de equações em Python. Cada equação pode ser representada,
# com matrizes. Por Exemplo, se tivermos a equação 3x - 9y = -42, ela pode ser representada como 
# [3, -9] e [-42]. Se adicionar-mos outra equação, por exemplo, 2x + 4y = 2, podemos mesclar com a 
# equação anterior para obter [[3, -9], [2, 4]] e [-42, 2]. Agora vamos resolver os valores de x e y

A = np.array([[3, -9], [2,4]])
B = np.array([-42, 2])

# Depois usamos a função linalg.solve() para resolver os valores de x e y, assim:

x, y = np.linalg.solve(A, B)
print('Os valores de x e y nas equações acima são, respectivamente:' ,x, y)

#%% Exercício 1 - Resolva o sistema de equações: 
# 1x + 1y = 35
# 2x + 4y = 94

a1 = np.array([[1, 1], [2, 4]])
b1 = np.array([35, 94])

x1,y1 = np.linalg.solve(a1, b1)
print('Os valores de x e y nas equações acima são, respectivamente:' ,x1, y1)

#%% Exercício 2 - Resolva a equação quadratica de ax ** 2 + bx + c = 0, usando a formula matematica
# Solicite ao usuário que digite os valores dos 3 coeficientes da equação (a, b, c) e resolva os valores de x
# Use a funçao sqrt() do pacote math
# Fique atento aos possíveis valores de retorno da equação:
#   * se d < 0: sem solução em R
#   * se d = 0: a equação tem apenas uma solução em R, x = -b2a
#   * se d > 0: a equação tem duas solucoes, x1 e x2

a = float(input('Informe o valor de a: '))
b = float(input('Informe o valor de b: '))
c = float(input('Informe o valor de c: '))

d = (b ** 2) - 4 * a * c

if d < 0:
    print('Sem solução em R')
elif d == 0:
    x2 = - b / 2 * a
    print('x é igual à : ', x2)
else:
    x2_1 = (-b + sqrt(d)) / (2 * a)
    x2_2 = (-b - sqrt(d)) / (2 * a)
    print('x1 é igual à: ', x2_1)
    print('x2 é igual à: ', x2_2)
    
#%% Exercício 3 - Resolva a equação quadratica ax ** 2 + bx + c = 0, criando uma função python que receba os 3 coeficientes

def equacao_quadratica(a: int, b: int, c: int):
    delta = lambda a, b, c: (b ** 2) - 4 * a * c
    
    d = delta(a, b, c)
    
    if d < 0:
        return ()
    elif d == 0:
        return (- b / 2 * a, )
    else:
        return (-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a)
    
equacao_quadratica(5, 1, 0)

#%% Exercício 4 - Estude https://docs.python.org/3.6/library/math.html

#%% Exercício 5 - Crie uma classe em python para calcular um número elevado ao quadrado

class Potencia:
    def __init__(self, potencia = 2):
        self.__potencia = potencia

    def elevar(self, base: float) -> float:
        valor = 1

        if self.__potencia > 0:   
            return self.__calcular(self.__potencia, base)
        elif self.__potencia < 0:
            base = 1 / base
            return self.__calcular(self.__potencia * -1, base)
        else:
            return 1

    def __calcular(self, potencia: float, base: float) -> float:
        valor = base
        for i in range(potencia - 1):
                valor *= base
        return valor

potencia = Potencia(-1)
potencia.elevar(-5)

class MathFunction:
    def __init__(self, code: str):
        self.code = code
        self._func = eval('lambda x: ' + code)

    def __call__(self, arg):
        return self._func(arg)
    
    def __repr__(self):
        return 'f(x) = ' + self.code

sq = MathFunction('x ** 0.5')
sq
sq(2)

#%% Exercício 6 - Crie uma função em Python para resolver a equação quadrática ax**2 + bx + c = 0, aplicando tratamento de erros

from numpy import linalg
from numpy import array
from math import sqrt

class NoRootsError(Exception):
    pass
class NoRelationalNumbersError(Exception):
    pass
class NoQuadraticError(Exception):
    pass


def returnX(a, b, c):
    if a == 0:
        raise NoQuadraticError
    if b ** 2 - 4 * a * c < 0:
        raise NoRootsError
    try:
        first_solution = (-b + sqrt(b ** 2 - 4 * a * c)) / 2 * a
        second_solution = (-b - sqrt(b ** 2 - 4 * a * c)) / 2 * a
        return (first_solution, second_solution)
    except ValueError:
        raise NoRelationalNumbersError


returnX(1, 9, 8)

#%% Exercício 7 - Crie um plot com a linha que representa a função linear
# y = mx + b
# ou
# y = ax + b

y = lambda x: 20 * x + 15
dados = [1, 2, 5, 6, 8, 10, 11.5, 13.8]
result = [y(x) for x in dados]

plt.plot(dados, result, 'r-')
plt.title('Dados')
plt.ylabel('y')
plt.xlabel('x')
plt.show()

m = 2
b = 7

x = np.linspace(-100., 100.)
fig, ax = plt.subplots()
ax.plot(x, m * x + b)
ax.set_xlim((-100., 100.))
ax.set_ylim((-100., 100.))
plt.show()

#%% Exercício 8 - Crie um plot que represente a função quadrática: x ** 2 + 2 * x + c

a = []
b = []

for x in range(-50, 50, 1):
    y = x ** 2 + 2*x + 2
    a.append(x)
    b.append(y)

plt.plot(a, b)
plt.show()

#%% Exercício 9 - Crie uma função que calculo o slope e intercepto (coeficientes m e b) da função
# linear estudada nas aulas anteriores, calcule e desenhe a linha que representa a função
from statistics import mean
y = lambda x, m, b: m * x + b

xs = np.array([1,2,3,4,5], dtype=np.float64)
ys = np.array([5,4,6,5,6], dtype=np.float64)

def best_fit_scope_interceptor(xs, ys):
    m = ((mean(xs)*mean(ys)) - mean(xs * ys)) / ((mean(xs) * mean(xs)) - mean(xs * xs))
    b = mean(ys) - m * mean(xs)
    return m, b

m, b = best_fit_scope_interceptor(xs, ys)
print(round(m,2), round(b, 2))

# lina
line = [y(x, m, b) for x in xs]

import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

plt.scatter(xs, ys, color='#003F72')
plt.plot(xs, line)
plt.show()

#%% - Exercicio 10 - Defina um novo valor de x e encontre o y correspondente

novo_x = [7]
previsao_y = [y(x, m, b)]

plt.scatter(xs, ys, color='#003F72', label='Dados')
plt.scatter(novo_x, previsao_y, color='green', label='Previsao', marker='*')
plt.plot(xs, line, label='Linha de Regressão')
plt.legend()
plt.show()