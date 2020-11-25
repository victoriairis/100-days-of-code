#sort simples
n1,n2,n3 = input().split()

n1 = int(n1) 
n2 = int(n2) 
n3 = int(n3) 
tam_vetor = 3
lista_inteiros = [n1, n2, n3]

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


bubbleSort(lista_inteiros)
print(lista_inteiros)