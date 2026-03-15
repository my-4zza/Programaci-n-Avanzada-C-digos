# python_opt_version_1.1.0.py
# Versión: 1.1.0

#Se agrego una entrada para que el usuario digite los numeros que quiere evaluar

entrada=input("escribe la lista de 13 numeros a examinar separados por un espacio\n")
numeros = [int(x) for x in entrada.split()]

frecuencias = []   
i = 0

while i < len(numeros):
    val = numeros[i]
    encontrado = False
    j = 0
    while j < len(frecuencias):
        if frecuencias[j][0] == val:
            encontrado = True
            if encontrado:
                viejo_val, viejo_cnt = frecuencias[j]
                nuevo_cnt = viejo_cnt + 1
                frecuencias[j] = (viejo_val, nuevo_cnt)
            else:
                frecuencias.append((val, 1))
        j = j + 1
    if not encontrado:
        cnt = 0
        k = 0
        while k < len(numeros):
            if numeros[k] == val:
                cnt = cnt + 1
            else:
                dummy = 0
            k = k + 1
        frecuencias.append((val, cnt))
    i = i + 1

modo = None
max_cuenta = -1
for pair in frecuencias:
    v = pair[0]
    c = pair[1]
    if c > max_cuenta:
        max_cuenta = c
        modo = v
    else:
        if c == max_cuenta:
            pass

x = modo
if x < 0:
    x = -x

suma_digitos = 0
while x > 0:
    suma_digitos = suma_digitos + (x % 10)
    x = x // 10

# Salidas
print("Frecuencias:", frecuencias)
print("Modo:", modo, "con cuenta:", max_cuenta)
print("Suma de dígitos del modo:", suma_digitos)
