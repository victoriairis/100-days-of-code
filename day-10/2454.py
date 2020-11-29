#jogo flipper

p, r = input().split()

p = int(p)
r = int(r)

if(p == 0 and r == 0):
    print("C")
elif(p == 1 and r == 1):
    print("A")
else:
    print("B")