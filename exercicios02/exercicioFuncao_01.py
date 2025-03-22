
"""Questão #4711
Completando a função
O código abaixo deve atender aos seguintes itens:

- Deve uma função com o nome "soma" que apenas retorna a soma entre dois números;
- O 1º parâmetro da função "soma" deve se chamar "num_1". O 2º parâmetro deve se chamar "num_2";
- Os valores dos números devem ser digitados pelo usuário;
- A variável "soma_numeros" deve receber o retorno da função;
- No final, deve ser impresso o valor de "soma_numeros"."""

def soma(num_1 , num_2): #defina os parâmetros que serão usados
    return num_1 + num_2 #fale quais parâmetros serão usados

num_1 = float(input('Digite o Primeiro Número: ')) #peça ao usuário para digitar o valor com ponto flutuante (poderia ser int)
num_2 = float(input('Digite o segundo número: '))

soma_numeros = soma(num_1, num_2) #Faça uma nova atribuição para soma usando os numeros.
print(soma_numeros)


"""

📌 Por que usamos a vírgula (,) dentro dos parênteses da função?

def soma(num_1, num_2):
A vírgula separa os parâmetros da função.

num_1 e num_2 são variáveis separadas → Cada uma delas recebe um valor quando a função é chamada.
A vírgula não está somando nada, apenas separando os argumentos.
💡 Pense na vírgula como uma separação entre diferentes informações que a função precisa para funcionar.


🛑 E se usássemos + no lugar da vírgula?
Se escrevêssemos assim:

def soma(num_1 + num_2):  
Isso causaria um erro no Python! ❌

Motivo:

Antes mesmo da função ser executada, o Python tentaria somar num_1 + num_2, mas nesse momento, os valores ainda não existem!
Os parâmetros ainda não receberam valores, então não faz sentido tentar somá-los dentro da definição.
"""

