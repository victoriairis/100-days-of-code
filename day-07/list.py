#listas em python

compras = ['arroz', 'frango', 'biscoito', 'biscoito']
#podemos contar quantas vezes um objeto se repete na lista
compras.count('biscoito')

#as inserções em listas podem ser feitas com o append ou o insert

compras.append('macarrao') #adicionado ao fim da lista
compras.insert(1, 'molho') #adiciona objeto na posição 1

#as remoções em listas podem ser feitas usando o pop ou o remove
compras.remove('biscoito') #remove o objeto
compras.pop(3) #remove o objeto em dada posição

compras.reverse() #reverte a lista
 
