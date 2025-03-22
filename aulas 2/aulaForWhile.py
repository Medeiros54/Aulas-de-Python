"""
Resumo do FOR:
For pode ser usado para "mostrar" ou acessar todos os itens dentro de uma lista, ou para fazer algo com cada item, como imprimir, somar, modificar, etc.
Ele percorre a lista item por item e faz algo com cada um desses itens.

"""

# Lista de clientes (nome e idade)
clientes = [
    {'nome': 'Ana', 'idade': 25},
    {'nome': 'Maria', 'idade': 35},
    {'nome': 'Pedro', 'idade': 28},
    {'nome': 'João', 'idade': 45},
    {'nome': 'Lucas', 'idade': 22}
]

# 1. Exibir o nome de todos os clientes
print("Nomes dos clientes:")
for cliente in clientes:
    print(cliente['nome'])

print("\n")

# 2. Calcular a idade média dos clientes
soma_idades = 0
for cliente in clientes:
    soma_idades += cliente['idade']

media_idade = soma_idades / len(clientes)
print(f"A idade média dos clientes é: {media_idade:.2f}")

print("\n")

# 3. Filtrar clientes com mais de 30 anos
clientes_acima_30 = []
for cliente in clientes:
    if cliente['idade'] > 30:
        clientes_acima_30.append(cliente['nome'])

print("Clientes com mais de 30 anos:")
print(clientes_acima_30)
