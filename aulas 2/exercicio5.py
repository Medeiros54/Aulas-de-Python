
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

entrada = input('Digite um número Inteiro ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_text = 'Impar'

    if par_impar == True:
        par_impar_text ='Par'
        
        print(f'O número {entrada_int} é {par_impar_text}') 
else:
    print ('Você não digitou um número inteiro')'''

Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

""" entrada = input('Por favor, digite o horário')

try:
      hora = int(entrada)
      
      if hora >= 0 and hora <= 11:
          print(f'Bom dia, agora são: {hora}')
          
      elif hora <= 12 and hora <=17:
          print(f'Boa tarde, agora são: {hora}')
          
      elif hora <= 18 and hora <= 23:
          print(f'Boa noite, agora são: {hora}')
          
      else: print('Não conheço essa hora')
except:
      print('Por favor, digite números inteiros.')
"""


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome  > 1:
    print(f'Seu nome é {nome} e contém {tamanho_nome} caracteres')
elif tamanho_nome >= 5 and tamanho_nome <=6:
    print(f'Seu nome é muito grande')
else: 
    print('Por favor, digite algo com mais de 3 caracteres')