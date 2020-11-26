cubic = []

for x in range(10):
	cubic.append(x**3)

cubic

#forma alternativa usando map

square = list(map(lambda x:x**2, range(10)))

#forma alternativa mais legivel

cubic_simple = [x**3 for x in range(10)]
