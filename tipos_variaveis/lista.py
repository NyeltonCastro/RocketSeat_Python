# Declaração

minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]

# Exibindo a lista toda
print("Minha lista de exemplo: ", minha_lista)

# Exibindo um elemento da lista
print("Exibindo o primeiro elemento da minha lista:",minha_lista[0])

# Fatiar/Slice Exibindo do elemento x ao y
print("Exibindo do 1 ao 5:", minha_lista[0:5])

# Fatiando do começo ao xº elemento
print("Exibindo do começo a o rocketseat:",minha_lista[:6])

# Fatiando do xº elemento ao final 
print("Exibindo de rocketseat ao final:",minha_lista[5:])


# Métodos de lista

# Método append(): Adiciona um elemento ao final da lista
minha_lista.append(6)
print("Após append(6):", minha_lista)

# Método index(): Mostra a localização do elemento na lista
indice = minha_lista.index(6)
print("O indice do elemento 6:", indice)

# Método insert(): Insere um elemento em um índice específico
minha_lista.insert(2, 10)
print("Após o insert(2,10):", minha_lista)

# Método pop(): Remove um elemento de índice específico e retorna ele
elemento_removido = minha_lista.pop(3)
print("Elemento removido:", elemento_removido)
print("Minha lista após pop(3)", minha_lista)

# Método remove(): Remove o elemento com o valor especificado
minha_lista.remove(True)
print("Minha lista após remove(True)", minha_lista)

# Método sort(): Organiza a lista com valores do msm tipo
outra_lista = [8, 4, 3, 6, 9, 5, 7, 1]
outra_lista.sort()
print("Outra lista após o sort()", outra_lista)
