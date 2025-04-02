"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
 def jogoPalavras(palavra, tentativa):
    palavra = 'Pudim'
    if tentativa == palavra.find:
     print (f'Você achou a letra: {palavra} ')"""



def jogoPalavras():
    palavra = 'Pudim'
    tentativa = input('Digite uma letra para tentar achar a palavra: ')
    
    if tentativa in palavra:
        print(f'Você achou a palavra: {tentativa}')
    else:
        print('Você errou')
 
    while palavra != tentativa:
        continue
    
    
        
        
jogoPalavras()