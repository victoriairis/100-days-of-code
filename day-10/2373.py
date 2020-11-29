#garçom

n = input()
n = int(n)
i = 1
copos_quebrados = 0

while(i <= n):
    l,c = input().split()
    l = int(l)
    c = int(c)
    if(c > l):
        copos_quebrados += c

print(copos_quebrados)
