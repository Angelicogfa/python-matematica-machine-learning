import numpy as np
import numpy.linalg as linalg

#%% Exercício 21 - Dada a matriz abaixo, multiplique 0.5 cada elemento da matriz

m = np.array([[1,2,3], [9,8,7]])
print(m)

print(m * 0.5)

#%% Exercício 22 - Qual a razão da mensagem de erro ao tentar executar a multiplicação das duas matrizes abaixo ?!
a = np.array([[1,2,3,4,], [6,7,8,9]])
b = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])

# Se as matrizes tiverem shapes incompatíveis. você recebe a mensagem de erro abaixo.
# Veja que A x B não é a mesma coisa que B x A na multiplicação de matrizes
np.matmul(b, a)
np.matmul(a, b)

#%% Exercício 23 - Obter a transposição de uma matriz
m = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(m)
print('\n')
print(m.T)

# ou 
np.transpose(m)

#%% Exercício 24 - Exemplo de rede neurais. Digamos que você tenha as seguintes duas matrizes, chamadas inputs e pesos:

inputs = np.array([[-0.27, 0.45, 0.64, 0.31]])
print(inputs)
print(inputs.shape)

pesos = np.array([[0.02, 0.001, -0.03, 0.036], [0.04, -0.003, 0.025, 0.009], [0.012, -0.045, 0.028, -0.067]])
print(pesos)
print(pesos.shape)

print(np.matmul(inputs, pesos.T))

#%% Exercício 25 - Desafio
# Use as duas matrizes abaixo para resulver os exercícios de 25 a 28
a = np.array([[3,2,-1], [6,4,-2], [5,0,3]])
b = np.array(([[2,3,2], [3,-4,-2], [4,-1,1]]))

# Na álgebra linear, o Rank de uma matriz A é a dimensão do espaço vetorial gerado (ou estendido) por 
# suas colunas. Isso corresponde ao número máximo de colunas linearmente independentes de A. Isso, por
# sua vez, é idêntico à dimensão do espaço ocupado por suas linhas. Rank é, portanto, uma medida
# da "não-degeneração" do sistema de equações lineares e transformação linear codificada por A. Existem
# várias definições equivalentes de Rank e o Rank de uma matriz é uma de suas caracteristicas mais fundamentais.

linalg.matrix_rank(a)

#%% Exercício 26 - Calcule a * b
np.dot(a,b)

#%% Exercício 27 - Qual o segundo autovetor em B
eig_vals, eig_vecs = linalg.eig(b)
eig_vecs[:,1]

#%% Exercicio 28 - Resolva Bx = b onde b= [14,-1,11]
_b = np.array([14,-1,11])
linalg.solve(b, _b)

#%% Exercício 29 - Calcule a inversa da matriz abaixo
a_matriz = [[3,2,1],\
            [2,-1,0],\
            [1,1,-2]]

b_matriz = [5,4,12]

# convertendo as matrizes para formato np
a_m = np.array(a_matriz)
b_m = np.array(b_matriz).transpose()

# resolvendo o problema
np_a_inv = linalg.inv(a_m)
np_x_mat = np_a_inv.dot(b_m)

print(np_x_mat)

#%% Exercício 30 - Faça um plot, usando matplotlib, que mostre a relação entre x e y
import matplotlib.pyplot as plt

x = np.array([-0.42, 1.34, 1.6, 2.65,3.53,4.48,5.48,6.21, 7.49,8.14, 8.91, 10.1])
y = np.array([1.58, 1.61,2.04,5.47,9.8,16.46, 25.34, 33.32,49.7, 58.79,71.26, 93.34])

plt.plot(x, y, 'o-')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


