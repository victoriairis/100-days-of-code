ddd = input()
ddd = int(ddd)

def retorno(ddd):
    switcher={
        61:'brasilia',
        71:'salvador',
        11:'sao paulo',
        21:'rio de janeiro',
        32:'juiz de fora',
        19:'campinas',
        27:'vitoria',
        31:'belo horizonte'
    }
    return switcher.get(ddd, "ddd inválido")

print(retorno(ddd))