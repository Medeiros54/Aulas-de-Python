"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input ('Digite seu nome: ')
idade = input ('Digite a sua idade ')

idade_int = int(idade) 

if nome and idade:  
    print (f'Seu nome é: {nome}')
    print (f'Sua idade é de: {idade_int} anos')
    print (f'Seu nome invertido é {nome[::-1]}')
    print (f'Seu nome contém {len(nome)} letras')
    print (f'A primeira letra do seu nome é {nome[0]}')
    print (f'A ultima letrad do seu nome é {nome[-1]}')
    print (f'O dobro da sua idade é {idade_int * 2}')

else: 
    print ('Você não completou o Input')