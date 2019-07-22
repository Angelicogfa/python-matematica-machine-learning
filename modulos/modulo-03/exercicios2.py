from scipy import *
from scipy.linalg import *
from matplotlib.pyplot import * 
%matplotlib inline

# Considere os vetores v1 e v2 abaixo para resolver os exercicios de 1 a 5.

v1 = array([1., 2., 3.])
v2 = array([2, 0, 1.])

# Exercício 1 - Multiplique o vetor v1 por 3 e divida o vetor V2 por 4
v1 * 3
v2 / 4

# Exercício 2 - Faça uma combinação linear entre eles. Multiplique o vetor 1 
# por 3 e multiplique o vetor v2 por 5. Então some os resultados

r1 = v1 * 3
print(r1)
r2 = v2 * 5
print(r2)

print(r1 + r2)

# Exercício 3 - Encontre o produto escalar entre os vetores v1 e v2. Considerando
# os vetores v1 e v2 acima, o resultado do produto escalar é 5. Crie o código
# que encontre esse resultado

print(v1.dot(v2))

# Exercício 4 - Faça uma multiplicação element-wise entre os vetores v1 e v2
print(v1 * v2)

# Exercício 5 - Encontre o cosseno do vetor v1
print(cos(v1))

# Exercício 6 - Considere o vetor v e a matriz M abaixo. Multiplique o vetor pela matriz
v = array([1., 2.])
M = array([[1., 2], [3., 4]])

print(v * M)

# Exercício 7 - Usando a função solve() do pacote linalg do scipy, encontre
# a solução do sistema de equações lineares representado pelos 2 array abaixo
import scipy.linalg as sl
A = array([[1., 2.], [3., 4.]])
b = array([1., 4.])

sl.solve(A, b)
