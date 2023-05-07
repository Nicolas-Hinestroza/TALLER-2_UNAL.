N = int(input("Escribe el primer numero (Dentro del rango 01-24): ")) # Definimos la variable N 
n = int(input("Escribe el segundo numero (Dentro del rango 01-24): ")) # Definimos la variable n
if N <= 24 and n <= 24:  # definimos las variables en el rando de 1 a 24 ya estas son todas aquellas que se repiten después de los dos puntos que marca tu reloj,
    if n == N: # si ambos valores son iguales
        print("Los numeros que escribiste son numeros espejos (" + str(N) + ":" + str(n) + ") ") # Imprimimos los resultados si son numero espejo
    else: # si no
        print("Los numeros que escribiste NO son numeros espejos (" + str(N) + ":" + str(n) + ") ") # Imprimimos los resultados si no son numeros espejo
else: # si no
    print("Escibe un valor dentro del rango 01-24 ") # Imprimimos erros