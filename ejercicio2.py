ant = 0
suma = 0
j = 1
pares = []
for i in range(0, 33):
    ant = j
    j = suma
    i = ant
    suma = i + j
    if suma%2 == 0:
        pares.append(suma)
x = sum(pares)
print(x)
    
    
    
