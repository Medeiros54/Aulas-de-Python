

# F strings! 
# Você utiliza f'{variavel}, ou seja, f na frente seguindo de um '

nome = 'Victor Medeiros'
peso = (float(135))
altura = (float(1.80))
imc = peso / altura ** 2

linha_2 = f'{nome} tem {altura:.3f} e pesa {peso}. Logo, seu IMC é de, {imc}'

print(linha_2);

#Usamos o F-string como forma de agilizar uma expressão e torna-la visivelmente melhor

#AGORA, USANDO FORMATS
# .:2f <- significa que você quer DUAS casas decimáis após o fim do teu número
a = 'A'
b = 'BBBBB'
c = 1.1

string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c)

#Parametro Nomeado
formato2 = string.format(
a, b, nome3=c)
#nesse caso, eu estaria renomeando C! Tudo o que vir depois de um paramentro nomeado, precisa ser nomeado.