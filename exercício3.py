primeiro_valor = input("Digite o Primeiro valor ")
segundo_valor = input("Digite o Segundo valor ")

if primeiro_valor < segundo_valor:
    print(f"{primeiro_valor} é menor do que {segundo_valor}")
elif primeiro_valor > segundo_valor:
    print(f"{primeiro_valor} é menor do que o segundo valor {segundo_valor}")
else: 
    print(
        f'{primeiro_valor=} é maior'
        f' do que {segundo_valor=}'
    )