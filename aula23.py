"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim) <- EVITAR AO MÁXIMO
    <- Contagem de complexidade (ruim) 
    
    NO PYTHON NÃO EXISTE CONST, É COMO SE FOSSE LET! 
    Para criar algo que você quer parecer imutável, use Variável com LETRAS MAIÚSCULAS! 
"""
velocidade = 60  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')
"""
jeito mais errado
if velocidade > RADAR_1:
    print ('Você ultrapassou o Limite de Velocidade Permitida, RADAR 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1:
        print ("O CARRO FOI MULTADO NO RADAR 1")
        """
        
        