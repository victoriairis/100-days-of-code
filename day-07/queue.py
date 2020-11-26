#para usar os diversos tipos de filas implementados como listas podemos
#usar a biblioteca deque 

from collections import deque

fila = deque(["ispi", "laurinha", "pablo", "larry"])
fila.append("pablito")
fila

fila.popleft()
fila
