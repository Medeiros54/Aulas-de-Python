"""
Listas:
Nada de novo, você as começa com [] e toma cuidado na separação,
principalmente se forem strings!

lista1 = ['Victor', 'Gabriela', 'Joaquim']
você pode pedir para pegar apenas um dos nomes, sendo cada um como um índice, começando do zero.

lista1 = ['Victor', 'Gabriela', 'Joaquim']
print(lista1)
print(lista1[1]) <- Retorna 'Gabriela'




lista1 = ['Victor', 'Gabriela', 'Joaquim']
lista1[1] = 'Gabriela Cavala Premium' # <- aqui eu editei/mudei o nome/valor 'Gabriela', indicando o índice e o que como eu queria.
print(lista1)
"""



"""
Listas Append.
Usamos isso quando queremos adicionar algo no fim da lista sem a necessidade de altera-lá.
Você pode adicionar um valor apenas no append.

"""

lista2 = ['Victor', 'Gabriela', 'Joaquim']
print(lista2)
lista2.append('Antonia')
print(lista2)


"""
Insert.
A gente usa pra conseguir colocar um valor dentro da lista,

programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
programadores.insert(1, 'Rafael') <- Rafael será colocado no índice 1.

                         0          1         2           3        4.      5
print(programadores) # ['Victor', 'Rafael', 'Juliana', 'Samuel', 'Caio', 'Luana']

____________________________________________________________________________________________________________________________
Remove:

Podemos remover diretamente usando o programadores.remove('Victor')
ou
Podemos remover pelo índice! programadores.pop(0)
"""

"""
Tuplas:

A ÚNICA LISTA QUE NÃO PODE SER ALTERADA APÓS CRIADA!

times_rj = ('Botafogo', 'Flamengo', 'Fluminense', 'Vasco') <- as tuplas são criadas por parantêses. 

print(type(times_rj)) # class=’tuple’
print(times_rj) # ('Botafogo', 'Flamengo', 'Fluminense', 'Vasco')

Uma observação a ser feita no uso de uma tupla é que se ela tiver um único item, 
é necessário colocar uma vírgula depois dele, 
pois caso contrário, o objeto que vamos obter é uma string, 
porque o valor do item é do tipo string.

times_rj = ('Portuguesa',)
"""
