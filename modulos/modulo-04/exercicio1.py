# Exercício 1 - Considerando os vetores v [1, 2] e w [2, 1], crie um script Python que faça a soma dos vetores.
# Não use funções de pacotes prontos, somente a linguagem Python pura e suas funções, se necessário.

v1 = [1,2]
v2 = [2,1]

def somar_vetores(vetor1, vetor2) -> []:
    if (len(vetor1) != len(vetor2)):
        raise ValueError('Ambos vetores devem ter a mesma dimensão')

    result = []
    for i in range(len(vetor1)):
        result.append(vetor1[i] + vetor2[i])
    
    return result

somar_vetores(v1, v2)

# Exercício 2 - Considerando os vetores v [1, 2] e w [2, 1], crie um script Python 
# que faça a subtração dos vetores. Não use funções de pacotes prontos, somente a 
# linguagem Python pura e suas funções, se necessário.

v1 = [1,2]
v2 = [2,1]

def subtrair_valores(vetor1, vetor2) -> []:
    result = []
    for value in zip(vetor1, vetor2):
        result.append(value[0] - value[1])
    return result

subtrair_valores(v1, v2)

# Exercício 3 - Considerando o escalar e vetor abaixo, crie uma função que receba os 2 
# como parâmetro e multiplique o vetor pelo escalar. Use apenas Python puro.

num = 3
vetor = [1, 2, 3]

def multiplicar_vetor_escalar(numero: float, v: []) -> []:
    result = []
    for i in range(len(v)):
        result.append(v[i] * numero)
    return result

multiplicar_vetor_escalar(num, vetor)

# Exercício 4 - Considerando os 2 vetores abaixo, crie uma função Python que faça 
# o dot product entre os 2 vetores e retorne apenas um valor escalar.

v1 = [1, 2]
v2 = [2, 1]

def dot_product(vetor1: [], vetor2: []) -> float:

    if (len(vetor1) != len(vetor2)):
        raise ValueError('Ambos vetores devem ter a mesma dimensão')

    valor = 0
    for value in zip(vetor1, vetor2):
        valor += value[0] * value[1]
    return valor

dot_product(v1, v2)

# Exercício 5 - Resolva o exercício anterior usando a função dot() do NumPy
import numpy as np

v1 = [1, 2]
v2 = [2, 1]

np.dot(v1, v2)

# Exercício 6 - Crie uma lista em Python com 3 dimensões, preenchida com zeros.
# Dica: a função pprint do pacote pprint permite imprimir uma lista tridimensional
# de forma mais legível.

import pprint

v = [0,0,0]
pprint.pprint(v)

# Exercício 7 - Considerando o vetor criado no item anterior, altere o valor na posição
# nas coordenadas (2, 1, 0) para 92.
for i in range(len(v)):
    v[i] = 92

pprint.pprint(v)

# Exercício 8 - Considere o vetor multidimensional A abaixo. Transforme-o em um vetor de 
# uma única dimensão, com todos os elementos ordenados na mesma sequência do vetor original.
# Dica: Esta operação é chamada de flatten do vetor (algo como "achatar" um vetor), sendo 
# uma das operações de pré-processamento mais comum em modelos de Deep Learning para Visão
# Computacional. NumPy oferece uma função para isso.

import numpy as np

A = np.array([[[ 0,  1],
               [ 2,  3],
               [ 4,  5],
               [ 6,  7]],
              [[ 8,  9],
               [10, 11],
               [12, 13],
               [14, 15]],
              [[16, 17],
               [18, 19],
               [20, 21],
               [22, 23]]])

print("\nVetor multidimensional original:\n\n", A.flatten())

# Exercício 9 - Considere o vetor multidimensional A abaixo. Transforme-o em um vetor de
# uma única dimensão, com todos os elementos ordenados na mesma sequência do vetor original.
# Use a função ravel() do NumPy.
# A função ravel() possui o parâmetro "order" que pode ser "C", "F", "A" ou "K".
# Qual a diferença entre usar os parâmetros C e F?
import numpy as np

A = np.array([[[ 0,  1],
               [ 2,  3],
               [ 4,  5],
               [ 6,  7]],
              [[ 8,  9],
               [10, 11],
               [12, 13],
               [14, 15]],
              [[16, 17],
               [18, 19],
               [20, 21],
               [22, 23]]])

print("\nVetor multidimensional original:\n\n", A.ravel())
print("\nVetor multidimensional original:\n\n", A.ravel("C"))
print("\nVetor multidimensional original:\n\n", A.ravel("F"))
print("\nVetor multidimensional original:\n\n", A.ravel("A"))
print("\nVetor multidimensional original:\n\n", A.ravel("K"))

# A diferença é que o F retornar os itens da mesma posição

# Exercício 10 - Calcule o Inner e Outer product dos vetores abaixo.
import numpy as np

vetor1 = [1, 2]
vetor2 = [2, 1]

print('Inner product: %s' % np.inner(vetor1, vetor2))
print('Outer product: %s' % np.outer(vetor1, vetor2))
