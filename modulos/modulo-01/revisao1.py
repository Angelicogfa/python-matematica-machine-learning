#%% diretorios
from os import path
arquivos = path.join(path.abspath('.'), 'Modulo01\\arquivos')

def read_data(file: str) -> []:
    registros = []
    with open(path.join(arquivos, file), 'r') as file:
        for line in file:
            registros.append(float(line))
        registros.sort()
    return registros

#%% Exercício 1 - Leia 2 números do terminal e imprima a soma, subtração, multiplicação e divisão

soma = lambda x, y: x + y
subtracao = lambda x,y: x - y
multiplicacao = lambda x, y: x * y
divisao = lambda x, y: x / y

valor1 = int(input('Informe o valor 1: '))
valor2 = int(input('Informe o valor 2: '))

print(soma(valor1, valor2))
print(subtracao(valor1, valor2))
print(multiplicacao(valor1, valor2))
print(divisao(valor1, valor2))

#%% Exercício 2 -  Escreva um programa em Python para converter uma medida de graus em radianos

pi = 22 / 7 # (3.14)
graus = float(input('Informe o grau: '))
radiano = graus * (pi / 180)
print(radiano)

#%% Exercício 3 - Escreva um programa em Python para calcular a área de um paralelogramo
area_paralelograma = lambda x, y: x * y
base = float(input('Informe a base: '))
altura = float(input('Informe a altura: '))
print('Área: %s' % area_paralelograma(base, altura))

#%% Exercício 5 - Escreva um programa em Python para imprimir todas as permutações de uma determinada string (incluindo duplicatas). Por exemplo a string: ABCD.

def permute_string(texto: str) -> []:
    if len(texto) == 0:
        return ['']
    
    prev_list = permute_string(texto[1:len(texto)])
    next_list = []
    
    # Precorrendo a matriz formada pelas permutações
    for i in range(0, len(prev_list)):
        for j in range(0, len(texto)):
            nova_string = prev_list[i][0:j]+texto[0]+prev_list[i][j:len(texto)-1]
            if nova_string not in next_list:
                next_list.append(nova_string)
    return next_list
print(permute_string('VvA'))

#%% Exercício 6 - Escreva um programa em Python para calcular o valor discriminante

def discriminant():
    x = float(input('Valor de X: '))
    y = float(input('Valor de Y: '))
    z = float(input('Valor de Z: '))
    
    discriminant = (y ** 2) - (4 * x * z)
    
    if discriminant > 0:
        print('Duas soluções. Valor discriminante é: %s' % discriminant)
    elif (discriminant == 0):
        print('Uma solução. Valor discriminante é: %s' % discriminant)
    else:
        print('Não existe solução real. Valor discriminante é %s' % discriminant)
        
discriminant()

#%% Exercício 7 - Escreva um programa em Python para calcular raízes quadradas usando o método babilônico
def algoritmo_babilonico(number):

    if (number == 0):
        return 0

    g = number / 2.0
    g2 = g + 1
    while g != g2:
        n = number / g
        g2 = g
        g = (g + n) / 2
    
    return g
    
r = algoritmo_babilonico(4)
print(r)


#%% Exercício 8 - Escreva um programa em Python que receba um arquivo com notas de um teste e divida as notas em classes de frequência.

def gerar_classes(numeros: [], quantidade_classe: int):
    menor = min(numeros)
    maior = max(numeros)

    distancia = (maior - menor) / quantidade_classe
    result = []

    for i in range(quantidade_classe):
        proximo = round(menor + distancia, 2)

        if (proximo > maior):
            proximo = maior

        classe = (menor, proximo)
        result.append(classe)
        menor = round(proximo + 0.01, 2)
    
    return result

def agrupar_registros_por_classe(numeros: [], classes: []):
    registros = []

    for classe in classes:
        minimo = classe[0]
        maximo = classe[1]
        itens = []
        for numero in numeros:
            if numero >= minimo and numero <= maximo:
                itens.append(numero)
        registros.append({ 'classe': classe, 'itens': itens, 'count': len(itens) })
    
    return registros

if __name__ == '__main__':
    registros = read_data('notas.txt')
    classes = gerar_classes(registros, 4)
    itens = agrupar_registros_por_classe(registros, classes)
    for i in itens:
        print('De %s a %s: %s item(ns)' % (i['classe'][0], i['classe'][1], i['count']))

#%% Exercício 9 - Escreva um programa em python que receba um arquivo com valores e calcule as principais
# medidas estatisticas: média, mediana, moda, variancia e desvio padrao
from collections import Counter

def media(registros: []):
    quantidade = len(registros)
    total = sum(registros)
    return total / quantidade

def mediana(registros: []):
    quantidade = len(registros)
    registros.sort()

    if quantidade % 2 == 0:
        n1 = int((quantidade / 2) - 1)
        n2 = int(((quantidade / 2) + 1) - 1)

        return (registros[n1] + registros[n2]) / 2
    else:
        n1 = int((quantidade / 2) - 1)
        return registros[n1]

def moda(registros: []):
    storage = { }

    for number in registros:
        if (number not in storage):
            storage[number] = 0
        storage[number] += 1

    print(storage) 
    key = 0
    value = 0
    for v in storage:
        if storage[v] > value:
            key = v
            value = storage[v]
    return key

def variancia_desvio_padrao(registros: []):

    def diferencas(numeros: []):
        m = media(numeros)
        regs = []
        for numero in numeros:
            regs.append(m - numero)
        return regs

    diferenca_quadrada = []
    for n in diferencas(registros):
        diferenca_quadrada.append(n ** 2)
    
    variancia = sum(diferenca_quadrada) / len(registros)
    desvio_padrao = algoritmo_babilonico(variance) # ou variance ** 0.5
    return variancia, desvio_padrao

if __name__ == '__main__':
    dados = read_data('dados.txt')
    m = media(dados)
    median = mediana(dados)
    mode = moda(dados)
    variance, sd = variancia_desvio_padrao(dados)
    print('Media: {0:5f}'.format(m))
    print('Modiana: {0:5f}'.format(median))
    print('Moda: {0:5f}'.format(mode))
    print('Variancia: {0:5f}'.format(variance))
    print('Desvio Padrão: {0:5f}'.format(sd))

#%% Exercício 10 - Escreva um programa em Python que dados 3 números, resolva a equação quadrática.
# Equação quadrática: ax² + bx + c = 0 -> (delta) = b² - 4 * a * c -> -b +- raiz(delta) / 2 * a
from cmath import sqrt

a = float(input('Informe o valor de a: '))
b = float(input('Informe o valor de b: '))
c = float(input('Informe o valor de c: '))

# discriminante ou delta
d = -4 * a * c

raiz1 = -b - sqrt(d) / (2 * a)
raiz2 = -b + sqrt(d) / (2 * a)
