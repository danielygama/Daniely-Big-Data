import numpy as np

# Gerando duas listas aleatórias de 10 números inteiros
lista1 = np.random.randint(1, 101, 10)
lista2 = np.random.randint(1, 101, 10)

print("Lista 1:", lista1)
print("Lista 2:", lista2)

# Calculando as operações
soma = lista1 + lista2
subtracao = lista1 - lista2
multiplicacao = lista1 * lista2
divisao = lista1 / lista2  # Divisão por zero pode gerar um aviso

# Imprimindo os resultados
print("\nResultados:")
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)