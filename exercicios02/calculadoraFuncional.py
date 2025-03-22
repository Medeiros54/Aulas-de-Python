# Calculadora com while


"""
while True: #enquanto essa condição for True
    sair = input('Quer sair? [S]im') #Usuário digita S ou N
    sair = sair.lower() # o resultado do usuário é convertido em minúsculo  
    sair = sair.startswith('s') #se começar com S, será TRUE (boleano)
    print(sair)
   
 """
 

while True: #definição das variáveis
    
    numero1 = input('Digite seu número: ')
    numero2 = input('Digite seu número: ')
    operador = input('Digite seu Operador (+-/*)')
    operadores_permitidos = '+-/*'  #definindo os operadores permitidos no input acima
    
    numeros_validos = None #
    num1Float = 0 #tranformei o numero1 em Float
    num2Float = 0
    
    try: #Tente isso
        num1Float = float(numero1) #tranformei o numero1 em Float
        num2Float = float(numero2) #tranformei o numero2 em Float
        numeros_validos = True #verifico se os dois números são verdadeiros e não letras
        
    except:    
       numeros_validos = None  #se for letra, o programa para aqui.
    
    if numeros_validos is None: #se os números não forem válidos, ou seja, forem letras ou outra coisa, erro.
        print('Um ou ambos números não são válidos')
        continue

     #definindo os operadores permitidos no input
    
    if operador not in operadores_permitidos: #se digitar um operador fora da lista o operador será inválido
         print('Operador inválido')
         continue
     
    if len(operador) > 1: #se tiver + de um operador, erro.
        print('Digite apenas um operador')
        continue
    
    print('O resultado da sua conta é: ')
    if operador == '+':
        print(num1Float + num2Float)
    elif operador == '-':
        print(num1Float - num2Float)
    elif operador == '*':
        print(num1Float * num2Float)
    elif operador == '/':
        if num2Float != 0:
            print(num1Float / num2Float)
        else:
            print('Erro: divisão por zero!')
 
 
 
 
 
 
    sair = input('Deseja [S]air?').lower().startswith('s')
    
    if sair is True:
        break
