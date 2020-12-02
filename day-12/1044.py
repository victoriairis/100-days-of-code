#multiplos

a,b = input().split()

a = int(a)
b = int(b)

if(a%b == 0 or b%a == 0):
    print("SÃO MULTIPLOS")
else:
    print("NÃO SÃO MULTIPLOS")