#lanches

codigo, quantidade = input().split()

#switch em python - usando dicionario
def escolha(codigo):
    return {
    '1': 4,
    '2': 4.50,
    '3': 5,
    '4': 2,
    '5': 1.5
    }[codigo]

valor = int(quantidade) * int(escolha(codigo))

print(valor)





