"""Variaveis Python
Constantes em python saõ variaveis em letras maiusculas
"""
velocidade = 64
local_km = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE_ACIMA = 62
RADAR_RANGE_ABAIXO = 58

if velocidade > RADAR_1 or velocidade < RADAR_RANGE_ACIMA:
    print('passou no ranger')
# elif velocidade 