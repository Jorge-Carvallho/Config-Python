"""Variaveis Python
Constantes em python saõ variaveis em letras maiusculas
"""
velocidade = 63
local_km = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

veloc_carro_pass_radar_1 = velocidade = RADAR_1
veloc_carro_no_range = velocidade > RADAR_1 + RADAR_RANGE and \
    velocidade < RADAR_1 - RADAR_RANGE

if velocidade in veloc_carro_pass_radar_1:
    print('Carro passou  no Radar 1')

elif veloc_carro_no_range:
    print('Carro passou no limite do range não multado ')

