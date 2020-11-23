#gasto de combustível

tempo, velocidade = input().split()
consumo = 12 #carro faz 12 km com 1 litro

tempo = int(tempo)
velocidade = int(velocidade)

km = tempo * velocidade 
litros = km / consumo

print(litros)