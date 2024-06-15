"""Variaveis Python
Constantes em python saõ variaveis em letras maiusculas
"""
velocidade = 61
local_km = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

veloc_carro_pass_radar_1 = velocidade = RADAR_1
veloc_carro_no_range = velocidade > RADAR_1 and velocidade < RADAR_1

if veloc_carro_pass_radar_1:
    print('Carro passou  no Radar 1')
    
if veloc_carro_no_range:
    print()