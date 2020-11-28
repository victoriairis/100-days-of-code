def renda(valor):
    if(0 < valor <= 2000):
        print("Insento")
    elif(2000 < valor <= 3000):
        print("8%")
    elif(3000 < valor <= 4500):
        print("18%")
    else:
        print("acima de 4500, 28% de imposto")

valor = input()
valor = float(valor)

renda(valor)