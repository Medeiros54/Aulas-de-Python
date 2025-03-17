"""
Operadores de comparação
Os operadores de comparação são usados para comparar valores, o que vai retornar True ou False, dependendo da condição. A seguir, na Tabela 3 temos exemplos de alguns usados no Python.

Operador	Conceito	Exemplo
>(Maior que)	Verifica se um valor é maior que outro	x > 5
<(Menor que)	Verifica se um valor é menor que outro	x < 5
== (Igual a)	Verifica se um valor é igual a outro	x == 5
!= (Diferente de)	Verifica se um valor é diferente de outro	x != 5
>= (Maior ou igual a)	Verifica se um valor é maior ou igual a outro	x >= 5
<= (Menor ou igual a)	Verifica se um valor é menor ou igual a outro	x <= 5



Operadores lógicos
Os operadores lógicos são usados para unir duas ou mais expressões condicionais. Isso é feito por meio de conectivos, como podemos ver na Tabela 4.

Operador	Conceito	Exemplo
and	Retorna True se todas as condições forem verdadeiras, caso contrário retorna False	x > 1 and x < 5
or	Retorna True se uma das condições for verdadeiras, caso contrário retorna False	x > 1 or x < 5
not	Inverte o resultado: se o resultado da expressão for True, o operador retorna false	not(x > 1 and x < 5)

O operador lógico not inverte o valor booleano de uma expressão. Se a expressão for True, ele a torna False, e vice-versa.

exemplos:
print(not True)  # False
print(not False) # True
print(not (5 > 3)) # False, porque 5 > 3 é True, e `not` inverte o resultado
Por que as outras opções estão erradas?
and: Operador lógico que retorna True apenas se ambas as expressões forem True.
or: Operador lógico que retorna True se pelo menos uma das expressões for True.
is not: Operador de identidade, usado para verificar se dois objetos não são o 
mesmo na memória (não inverte valores lógicos diretamente).
🔹 Conclusão: O operador lógico que inverte o resultado de uma expressão é not.









"""

idade_lucas = 21
idade_carolina = 19

# OPERADOR OR
if idade_lucas >= 18 or idade_carolina >= 18: 
    print("Pelo menos um dos dois é maior de idade")
else:
    print("Lucas e Carolina não são maiores de idade")

# OPERADOR AND
if idade_lucas >= 18 and idade_carolina >= 18:
    print("Lucas e Carolina são maiores de idade")
else:
    print("Pelo menos um dos dois não é maior de idade")


"""
Operadores de identidade
Os operadores de identidade servem para a comparação de objetos. Nessa comparação é verificado se eles ocupam a mesma posição na memória, o que significará que se trata do mesmo objeto, como vemos isso na Tabela 5.

Operador	Conceito	Exemplo
is:	Retorna True se as variáveis comparadas forem o mesmo objeto	nome is ‘Marcos’
is not:	Retorna True se as variáveis comparadas não forem o mesmo objeto	x is not ‘Python’
. Operadores de identidade
Vejamos com mais detalhes o uso dos operadores de identidade:


"""

ime_carlos = 'Botafogo'
time_luciano = 'Flamengo'
time_fabricia = 'Botafogo'

if time_carlos is time_luciano: # se(if) o time_carlos for igual time_luciano
    print("time_carlos - time_luciano = mesmo objeto") #mostre na tela: Mesmo Objeto.
else:
    print("time_carlos - time_luciano = objetos diferentes") #se não, mostre: Objetos diferentes.

if time_carlos is time_fabricia:
    print("time_carlos - time_fabricia = mesmo objeto")
else:
    print("time_carlos - time_fabricia = objetos diferentes")
