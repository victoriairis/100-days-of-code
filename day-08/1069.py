#diamantes

quantidade_linhas = input()
quantidade_linhas = int(quantidade_linhas)

i = 1
cont_a = 0
cont_b = 0

while i <= quantidade_linhas:
    linha = []
    linha = input()
    
    for x in linha:
        if x == '<':
            cont_a += 1
        elif x == '>':
            cont_b += 1
    
    print(cont_a)
    print(cont_b)

    if(cont_a == cont_b):
        print("Existem " + str(cont_a) + " diamantes")
    elif(cont_a < cont_b):
        print("Existem " + str(cont_a) + " diamantes")
    else: 
        print("Existem " + str(cont_b) + " diamantes")
    i+=1