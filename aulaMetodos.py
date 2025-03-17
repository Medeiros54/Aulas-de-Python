"""
Método FIND.

Acho que ele se auto-explica.
A gente usa esse método para procurar uma string em alguma parte do código e mostrar onde está seu índice.

Caso ele não ache, apontará como -1.
"""


mensagem = 'string no Python'
print(mensagem.find('Python')) # 10


"""
Método replace()
O método replace() é utilizado para substituir ocorrências de substrings dentro de uma string.

Aqui nós já tinhamos nossa primeira variável declarada, mas decidimos fazer uma alteração.
1- mensagem já foi declarada
2- criamos uma nova variável para alterar a variável mensagem.
3- temos que usar o nomeDaVariavel.replace e depois entre parentesês colocar os parâmetros que queremos que mude.
"""

mensagem = 'Quero aprender Java! Na DevMedia tem salas de Java para aprender essa linguagem'
nova_mensagem = mensagem.replace('Java', 'Python')
print(nova_mensagem) # Quero aprender Python! Na DevMedia tem salas de Python para aprender essa linguagem


mensagem2 = 'Quero aprender a programar essa caralha logo'
novaMensagem2 = mensagem2.replace('caralha', 'linguagem')
print(novaMensagem2)


"""
Método split()
Com o método split() desmembramos uma string em múltiplas strings através de um separador 
passado no parâmetro, retornando todas numa lista.

Ele separa strings longas, como uma frase e retorna um array com todos os valores
declarados na variável individualmente. Pode ser útil demais.

É obrigatório o uso de um separador na função split() quando usada com aspas, pois caso contrário,
um erro será gerado com a mensagem ValueError: empty separator.
Se as aspas não forem usadas com split(), a função considerará o espaço em branco como separador.  
Mas você também pode pedir para que ele separa uma letra ou palavra da variável.

Também podemos pedir para o separador qual é o primeiro valor de uma variável, apenas colocando 
mensagem.split[1] <- atenção como você escreveu pra não errar. Antes era com () e agora com [].
Ele retornará pra você como se cada palavra fosse um índice, começando do 0.
No caso, retornaria a palavra "aprendendo".
"""

mensagem = 'Estou aprendendo Python na DevMedia'
nova_mensagem = mensagem.split(' ')
print(type(nova_mensagem)) # type 'list'
print(nova_mensagem) # ['Estou', 'aprendendo', 'Python', 'na', 'DevMedia']


"""
Método Upper e Lower.

Fácil, você usa para deixar as letras minúscula em MAIÚSCULAS, já o Lower, é o contrário.

mensagem = 'e ai, cheguei.'
nova_mensagem = mensagem.upper()
print(nova_mensagem)


"""