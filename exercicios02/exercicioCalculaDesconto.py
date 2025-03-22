"""

- Deve ser criada uma função com o nome "calcula_desconto", que deve receber os seguintes parâmetros:
- 1º parâmetro: deve ter o nome "preco" (representa o valor do produto);
- 2º parâmetro: deve ter o nome "desconto" (representa o percentual de desconto a ser aplicado no preço);
- No final devem ser impressos os valores do produto sem desconto e com desconto;

"""
def calcula_desconto(preco, desconto): #defini os parametros 
    novo_preco = preco - (preco * desconto) #estabeleci a conta pro novo preco e coloquei como novo preco
    return(novo_preco) #pedi para retornar o novo preco

preco = 50
desconto = 0.1

preco_com_desconto = calcula_desconto(preco, desconto) #o preço com desconto é a função calcula_desconto + seus parâmetros.


print(f'O preço do produto é: {preco} ' )
print(f'O preço do produto com desconto é: {preco_com_desconto}')