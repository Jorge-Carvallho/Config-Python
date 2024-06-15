"""Variaveis Python
Constantes em python saõ variaveis em letras maiusculas
"""
velocidade = 61
local_km = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

veloc_carro_pass_radar_1 = velocidade > RADAR_1

carro_passou_radar_1 = local_km >= (LOCAL_1 - RADAR_RANGE) and \
    local_km <= (LOCAL_1 + RADAR_RANGE)

carro_multado_radar_1 = carro_passou_radar_1 and veloc_carro_pass_radar_1


if veloc_carro_pass_radar_1:
    print('Velocidade carro dentro do ranger')

if carro_passou_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_multado_radar_1:
    print('Carro multado em radar 1')
