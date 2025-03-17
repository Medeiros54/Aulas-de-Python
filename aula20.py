'''
.<número de dígitos>f
x ou X - Hexadecímal 
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita 
ˆcentro 
Sinal - + ou -
= - Força o número a aparecer antes do zeros
Ex.: 0>-100,.1f
Conversion Flags - !r !s !a
'''

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: <10} ')
print(f'{variavel: ^10}.')
print(f'{1000.28173821:.2f}')
print(f'{1000.1293921:.4f}')