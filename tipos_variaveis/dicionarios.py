pessoa = {"nome": "Nyelton", "idade": 30, "cidade": "Águas Lindas"}
print("Meu dicionario de exemplo:", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

# Atribuindo valor depois de instanciar o dicionario
pessoa["sobrenome"] = "Castro"
print("Sobrenome:", pessoa["sobrenome"])

print("Meu dicionario atualizado:", pessoa)

# Atualizando o valor da chave
pessoa["idade"] = 31
print("Idade atualizada:", pessoa["idade"])

# Removendo um par chave-valor
del pessoa["sobrenome"]
print("Removendo chave-valor sobrenome:", pessoa)

# Métodos principais: keys(), values(), items()

# Método keys(): Exibe todas as chaves do dicionario

# Transformar em lista pra acessar valores individualmente como uma lista
chaves = list(pessoa.keys())
print("Chaves do dicionário:",chaves)
print("Acessando a primeira chave:", chaves[0])

# Método values(): Exibe os valores do dicionário
valores = list(pessoa.values())
print("Todos os valores do dicionário:", valores)
print("Acessando o segundo valor do dicionário", valores[1])

# Método items(): Retorna tuplas com as chaves-valo
itens = list(pessoa.items())
print("Pares chave-valor do dicionário:", itens)

# intes[tupla][chave-valor]
print("Primeira chave-valor: %s = %s" %(itens[0][0], itens[0][1]))


