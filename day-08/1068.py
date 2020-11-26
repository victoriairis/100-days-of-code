n = input()
n = int(n)
i = 1
conta = 0
contb = 0
pilha = []
while i <= n:
    expressao = []
    expressao = input()

    for x in expressao:
        if(x == '(' or x == ')'):
            pilha.append(x)
    print(pilha)

    for y in pilha:
        if(y == ')'):
            pilha.pop()
            conta+=1
        if(y == '('):
            pilha.pop()
            contb+=1
            
    if(conta == contb):
        print("correto")
    else: 
        print("incorreto")
    i+=1