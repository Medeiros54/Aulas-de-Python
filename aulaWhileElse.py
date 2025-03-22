"""

string = 'Valor Qualquer' 

i = 0 #usei o I pra indicar um índice
while i < len(string): #enquanto o índice for = ou - que 1,
    letra = string[i] #aqui eu pego cada um das letras da string
    
    if letra == ' ': #se dentro da variavel ter um espaço vazio, pare.
        break
    
    print(letra) 
    i += 1 # O índice 'i' é incrementado, indo para o próximo caractere da string
    
else: 
    print('Não encontrei espaço na string')
    
print('O espaço está antes de: ') 

"""


frase = ' O Python é uma linguagem de programação' \
    'multiparadigma' \
    'Python foi criado por Guido Van Rossum'

