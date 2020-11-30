def rafael(x,y):
    r = (3*x)**2 + y**2
    return int(r)

def beto(x,y):
    b = 2*(x**2)+(5*y)**2
    return int(b)

def carlos(x,y):
    c = (100*x) + (y**3)
    return int(c)

qnt_casos = int(input())
i = 0

while(i < qnt_casos):
    x,y = input().split()
    x = int(x)
    y = int(y)
    c = carlos(x,y)
    b = beto(x,y)
    r = rafael(x,y)

    if(c > b and c > r):
        print("Carlos Ganhou")
    elif(b > r and b > c):
        print("Beto Ganhou")
    elif(r > b and r > c):
        print("Rafael ganhou")
    i =+ 1
