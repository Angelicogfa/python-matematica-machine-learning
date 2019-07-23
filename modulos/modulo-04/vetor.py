import numpy as np

# Declarando os Vetores (pela definiçao matematica)
# Representamos em Python como uma lista

x = [1,2,3]
y = [4,5,6]

print('\nListas em python não são vetores')
print(type(x))
print(type(y))

# Isso aqui não é adição de vetores
print(x + y)

# Agora sim, adição de vetores usando numpy
print('\nAgora sim, adição de vetores usando numpy')
soma = np.add(x, y)
print(soma)
print(type(soma))

# Produto entre vetores
print('\nProduto entre vetores')
mul = np.cross(x, y)
print(mul)
print(type(mul))