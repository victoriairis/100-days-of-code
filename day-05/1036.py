#bhaskara
import math
a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

delta = (b**2) - (4*a*c)

raiz_delta = math.sqrt(delta)

r1 = (-b + raiz_delta) / 2*a
r2 = (-b - raiz_delta) / 2*a

print(r1)
print(r2)