# A tupla é imutavel

minha_tupla = (1, 2, 2, 3, 4)
print("Minha tupla:", minha_tupla)

# Ver o exercicio de lista pra ver como acessar os elementos e slice

# Adicional de como acessar o ultimo elemento
print("Minha tupla [-1]", minha_tupla[-1])


# Métodos da tupla

# Método count(): conta quantas vezes tem o msm elemento
contagem = minha_tupla.count(2)
print("Quantas vezes aparece o numero 2/count(2):", contagem)

# Método index(): Retorna o indice do elemento
indice = minha_tupla.index(3)
print("Indice do elemento 3/index(3):", indice)