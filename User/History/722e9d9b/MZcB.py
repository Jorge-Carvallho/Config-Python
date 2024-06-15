"""Variaveis Python
Constantes em python saõ variaveis em letras maiusculas
"""
velocidade = 61
local_KM  = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

veloc_carro_pass_radar_1 = velocidade > RADAR_1

carro_multado_radar_1 = local_KM >= (LOCAL_1 - RADAR_RANGE) and \
    local_KM <= (LOCAL_1 + RADAR_RANGE)

carro_pass_radar_1 = local_KM >=(LOCAL_1 - RADAR_RANGE) and \

    
