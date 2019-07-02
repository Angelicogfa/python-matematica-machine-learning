import numpy as np

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

#%% Exemplo de rede neurais. Digamos que você tenha as seguintes duas matrizes, chamadas inputs e pesos:

inputs = np.array([[-0.27, 0.45, 0.64, 0.31]])
print(inputs)
print(inputs.shape)

pesos = np.array([[0.02, 0.001, -0.03, 0.036], [0.04, -0.003, 0.025, 0.009], [0.012, -0.045, 0.028, -0.067]])
print(pesos)
print(pesos.shape)

np.matmul(inputs, pesos.T)