#salario com bonus

nome, salario_fixo, vendas = input().split()

salario_fixo = float(salario_fixo)
vendas = float(vendas)

porcentagem = vendas * 0.15

salario_bonus = salario_fixo + porcentagem

print(salario_bonus)