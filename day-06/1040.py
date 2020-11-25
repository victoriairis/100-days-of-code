#media 3

n1, n2, n3, n4 = input().split()

media = (int(n1) * 2 + int(n2) * 3 + int(n3) * 4 + int(n4) * 1) / 10

print(media)

if(media >= 7):
    print("Aprovado")
elif(media < 5):
    print("Reprovado")
else:
    print("Recuperacao")