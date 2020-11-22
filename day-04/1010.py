#calculo simples

codigo1, qnt1, valor1 = input().split()
codigo2, qnt2, valor2 = input().split()
qnt1 = int(qnt1)
qnt2 = int(qnt2)
valor1 = float(valor1)
valor2 = float(valor2)

soma_valor = (qnt1 * valor1) + (qnt2 * valor2)

print(soma_valor)