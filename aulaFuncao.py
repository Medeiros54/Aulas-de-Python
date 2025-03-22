"""
Uma função é um bloco de código que você chamar
e pode ser usado várias vezes em várias partes do programa.

usamos DEF para definir uma função.

def hello(meu_nome):
  print('Olá',meu_nome)
  

 Vou deixar uma função de código de salário.
 IMPORTANTE -> devemos usar o return dentro da função ou para exibir algo que uma função faz.
 """
 





def calcular_pagamento(qtd_horas, valor_hora): #começamos com uma função
  horas = float(qtd_horas) #falamos que o parametro horas pode ser de ponto flutuante
  taxa = float(valor_hora) #as taxas também.
  if horas <= 40: #se a quantidade de horas for menor ou = a 40:
    salario=horas*taxa #calcule: horas * taxa 
    
  else:
    h_excd = horas - 40 #se for + de 40 horas
    salario = 40*taxa+(h_excd*(1.5*taxa)) #A taxa será de 1.5 * o valor que a empresa cobra + as 40 horas * o excedente.
  return salario #retorne o valor atualizado.

str_horas= input('Digite as horas: ') #Agora pedimos o parâmetro ao usuário
str_taxa=input('Digite a taxa: ') #idem
total_salario = calcular_pagamento(str_horas, str_taxa) 

print('O valor de seus rendimentos é R$',total_salario)




"""
Função Builtin 



"""