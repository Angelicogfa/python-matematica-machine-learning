# !pip install numpy
import numpy as np

#%% Execício 11 - Crie uma matriz numpy que contenha um escalar, usando a função array do Numpy
s = np.array(8)

#%% Exercício 12 - Qual o shape de um escalar ?!
s.shape

# operações com escalares
x = s - 2
print(x)
type(x)

#%% Exercício 13 - Crie um vetor com numpy a partir de uma lista em Python e visualize o shape
vec = np.array([2,4,6,8,10])
print(vec.shape)
print(vec)
print(type(vec))

vec[1]
vec[1:3]

#%% Exercício 14 - Crie uma matriz 3x3 conteundo os numeros de um a nove e visualize o shape
mat = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(mat.shape)
print(mat)

mat[1][2]

#%% Exercício 15 - Crie um tensor 3x2x3x1 e visualize o shape

ten = np.array([[[[1],[2],[3]], [[4],[5],[6]]],[[[1],[2],[3]], [[4],[5],[6]]], [[[1],[2],[3]], [[4],[5],[6]]]])
print(ten.shape)
print(ten)


#%% Exercíccio 16 - Imprima um unico elemento do tensor
print(ten[2][1][1][0])

#%% Exercício 17 - Altere o shape de um vetor
vec = np.array([1,2,3,4])
vec.shape
vec = vec.reshape([2,2])
vec.shape

#%% Exercício 18 - Suponha que você tenha uma lista de numeros e queira adicionar 5 a cada item da lista
valores = [1,2,3,4,5]

for i in range(len(valores)):
    valores[i] += 5

print(valores)

valores2 = np.array([1,2,3,4,5]) + 5
print(valores2)

#%% Exercício 19 - Digamos que você tenha um objeto chamado "valores" e você queira reutilizá-lo, mas primeiro
# você precisa definir todos os seus valores em zero. Facil, basta multiplicar por zero e atribuir o
# resultado de volta ao objeto, certo ? Como você faria isso.

valores = [5,6,7,8,10,15,55,96]
valores *= 0
print(valores)

#%% Exercício 20 - Considerando as duas matrizes abaixo, como você faria a soma entre elas ?

x = np.array([[1,3], [4,5]])
y = np.array([[8,7], [11,17]])

x + y



