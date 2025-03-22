"""Marque a opção que contém o código que atenda aos seguintes itens:

- A aplicação deve ter três variáveis para representar as notas;
- A média vai ser igual a soma das notas dividido pela quantidade delas;
- Caso a média seja no mínimo 7, o aluno será aprovado;
- Caso a média seja maior ou igual a 5 e menor que 7, o aluno estará de recuperação;
- Caso nenhuma das condições anteriores aconteça, o aluno estará reprovado."""

nota1 = 7
nota2 = 7
nota3 = 7

media = (nota1 + nota2 + nota3) / 3

if media >7:
    print('Você foi aprovado')
elif media >= 5 and media < 7:
    print('Você está de recuperação')
    
else:
    print('Você foi reprovado')