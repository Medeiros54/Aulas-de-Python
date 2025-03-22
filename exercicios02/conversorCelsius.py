
"""

temos uma função que converte a temperatura de Celsius para Fahrenheit. Preencha as lacunas para que o código funcione de acordo com os itens abaixo:

- o nome da função deve ser "celsius_fahrenheit";
- a função "celsius_fahrenheit" deve possuir a seguinte fórmula:

Temperatura Fahrenheit = (Temperatura Celsius * 9 / 5 ) + 32
(use essa mesma ordem da fórmula no código)

"""


temperatura_celsius = int(input("Digite a temperatura em graus celsius: "))

def celsius_fahrenheit(temp_celsius):
    temp_fahrenheit = (temp_celsius * 9 / 5) + 32
    return temp_fahrenheit

# Chamando a função e armazenando o resultado em uma variável
temperatura_fahrenheit = celsius_fahrenheit(temperatura_celsius)

# Exibindo o resultado
print(temperatura_celsius, "°C equivalem a:", temperatura_fahrenheit, "°F")

#Função celsius_fahrenheit: A fórmula foi ajustada corretamente para fazer a conversão de Celsius para Fahrenheit.

#Correção no nome da função e variável:

#Você usou celcius_fahrenheit em vez de celsius_fahrenheit (que é o nome correto).
#Também, a função agora retorna o valor de Fahrenheit, e o resultado é armazenado na variável temperatura_fahrenheit.
#Chamada da função: A função celsius_fahrenheit(temperatura_celsius) é chamada com o valor que o usuário digita, e o resultado é armazenado em temperatura_fahrenheit.
