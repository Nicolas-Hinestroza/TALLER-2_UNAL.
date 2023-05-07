def mcm(a, b): # definimos la funcion mcm con las variables a y b
    n = max(a, b) # buscamos la variable mayor para basarnos 
    while True: # mientras que sea verdadero
        if (n % a == 0) and (n % b == 0): # si al dividir n por a y b el residuo es 0 (con esta formula encontramos el mcm) entonces
            return n # Que nos devuelva 0
        n += 1 # a n le sumamos 1

if __name__ == "__main__": # ahora ejecutamos el programa con la funcion main
    a = int(input("Escribe el primer valor: ")) # Definimos la variable a
    b = int(input("Escribe el segundo valor: ")) # Definimos la variable b
    print("El mcm de " + str(a) + " y de " + str(b) + " es: " + str(mcm(a, b))) # Imprimimos el resultado del mcm