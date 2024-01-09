'''
Interpolação é quase um format

s - string
d e i - int 
f - float
x e X - Hexadecimal
'''

nome = 'Luiz'
preco = 1000.2000034
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O Hexadecimal de %d é %06x' % (15, 15))