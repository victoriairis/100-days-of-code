#tabuada

n = input()
n = int(n)

i = 0
res = 0
while(i <= 10):
    res = i * n
    print(str(n) + " * " + str(i) + " = " + str(res) )
    i+=1