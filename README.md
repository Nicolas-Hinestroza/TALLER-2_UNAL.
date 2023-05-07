# TALLER-2_UNAL.
Se debe elaborar un repo donde presente la solución a todos los problemas planteados. Para los puntos impares debe realizar un programa individual con extensión .py y para los pares debe elaborar un notebook .ipynb con las soluciones. El repo debe contener la explicación de la solución de cada punto. Todos los archivos se deben adjuntar al repo.

- **1. Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número.**

![image](https://user-images.githubusercontent.com/124611099/236645043-9e3a7c49-ec60-4275-8490-5ef8c8525045.png)

    Lista = [] # Creamos una lista vacia para almacenar los datos recolectados.
    def separados(a): # Definimos la funcion separados con la variable a
       while a > 0: # Mientras a sea mayor que a sea mayor que 0 haga
            Lista.insert(0, a % 10) # Con la formula se agregara la ultima cifra en la primera parte de la lista
            a = a // 10 # Con esta formula eliminamos la ultima cifra del numero
       print ("El numero que escribiste es " + str(n) + " y al separarlo queda " + str(Lista)) # Se imprime el resultado
    
    n = int(input("Escribe el valor que quieres separar: ")) # Definimos la variable n
    separados(n) # Corremos la funcion con la variable n


- **2. Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entrege los digitos tanto de la parte entera como de la decimal.**

![image](https://user-images.githubusercontent.com/124611099/236658695-8b1df391-c88e-4f70-a294-1d4ab5305dbd.png)

    n = float(input("Escribe el valor que quieres separar: ")) # Definimos la variable n
    n_entero = int # lo asignamos como entero.
    n_decimal = float # Lo asignamos como flotante.
    Lista1 = [] # Creamos la lista vacia para almacenar los datos recolectados.
    def separados1(a): # Definimos la funcion separados con la variable a
        while a > 0: # Mientras a sea mayor que a sea mayor que 0 haga
            Lista1.insert(0, a % 10) # Con la formula se agregara la ultima cifra en la primera parte de la lista
            a = a // 10 # Con esta formula eliminamos la ultima cifra del numero
    n_entero = int(n) # Asiganmos el numero flotante a entero
    n_decimal = n - n_entero  #Restamos el numero entero con el flotante por lo tanto n_decimal es la parte flotante 
    separados1(n_entero) # Corremos la funcion con la variable n
    print(" El valor que escribiste es " + str(n) + ", la parte entera es: " + str(n_entero) + " y la parte entera separada es " + str(Lista1) + ", la parte decimal es: " + str(n_decimal)) # Se imprime el resultado

- **3. Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos.**

![image](https://user-images.githubusercontent.com/124611099/236658680-0b4ead80-c4f0-443e-98c7-85003f0459d4.png)

    N = int(input("Escribe el primer numero (Dentro del rango 01-24): ")) # Definimos la variable N 
    n = int(input("Escribe el segundo numero (Dentro del rango 01-24): ")) # Definimos la variable n
    if N <= 24 and n <= 24:  # definimos las variables en el rando de 1 a 24 ya estas son todas aquellas que se repiten después de los dos puntos que marca tu reloj,
        if n == N: # si ambos valores son iguales
            print("Los numeros que escribiste son numeros espejos (" + str(N) + ":" + str(n) + ") ") # Imprimimos los resultados si son numero espejo
        else: # si no
            print("Los numeros que escribiste NO son numeros espejos (" + str(N) + ":" + str(n) + ") ") # Imprimimos los resultados si no son numeros espejo
    else: # si no
        print("Escibe un valor dentro del rango 01-24 ") # Imprimimos erros

- **4. Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Con cuántos valores de la serie, se tienen errores del 10%, 1%, 0.1% y 0.001%.**

![image](https://user-images.githubusercontent.com/124611099/236658739-37b7cc52-ec16-41dc-86ba-335ef3c8a7cb.png)

    import math
    def potencia(x, n): # Definimos la funcion separados con la variable a
        z = 0 # Definimos z 
        for c in range(0, n): # para i en un rango desde 0 hasta n
            a = (- 1) ** c # utilizamos la formula para cambiar el signo
            b = (x ** (2 * c)) / math.factorial(2 * c) # Utilizamos la formula para aproximarnos al coseno
            z += a * b # Utilizamos esta formula para carcular los datos
        return z # nos devuelven el resultado es decir z

    if __name__ == "__main__": # ahora ejecutamos el programa con la funcion main
        x = float(input("Escribe el valor al que le quieres sacar el coseno: ")) # definimos la variable x
        n = int(input("Escribe cuantos valores de las series ")) # Definimos la variable n
        coseno = math.cos(x) # definimos la variable 
        print("Resultado Serie MacLaurin: "+str (potencia(x, n))) # Imprime el resultado de la aproximacion
        print("Resultado Funcion Math: "+str(coseno)) # Imprime la funcion
        print("Diferencia = "+str(coseno - potencia(x, n))) # Imprimie la diferencia

- **5. Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde la perpectiva iterativa como recursiva.**

![image](https://user-images.githubusercontent.com/124611099/236658767-8deeaab3-0f52-41e9-9ac2-4acf76bf7b39.png)

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
    

- **6. Desarrollar un programa que determine si en una lista no existen elementos repetidos.**

![image](https://user-images.githubusercontent.com/124611099/236658786-4c2564f3-9355-4a5e-9aba-153ac4529bb1.png)

    n = int(input("Cuantos valores vas a digitar")) # vamos a definir esta variable para ver cuantos numeros van a digitar en la lista
    lista = [] # dejamos esta lista vacia para ir colocando los datos que se recolecten
    lista2 = [] # dejamos esta lista vacia para ir colocando los datos que se recolecten
    lista3= [] # dejamos esta lista vacia para ir colocando los datos que se recolecten
    for y in range(0,n): # usamos un ciclo for para seleccionar los datos segun la variable n
        v = int(input("Digita el valor: ")) # DFefinimos la variable v como los elementos recibidos
        lista.append(v) # Los valores que se van recibiendo se van almacenando en la lista
    print ("1. la lista que has creado es el siguiente:", lista) # Imprimimos la lista que se creo
    for z in lista:  # para z in lista  
        a = lista.count(z) # Vamos a verificar los valores que se repiten en lista
        if a >= 2: # si hay mas de dos valores que se repiten entonces
            lista2.append(z) # se agregan los valores que se repiten en la lista2
    c = len(lista2) # Vamos a ver cuantos valores hay en la lista2
    for e in lista2: # Para que la lista que se repite se vea mas lista entonces vamos a usar un for, para e en listas2
        if e not in lista3: # si e no esta en lista3
            lista3.append(e) #entonces vamos a agregar los valores en la lista3
    if c >= 2: # si c es mayor o igual que 2 entonces
        print("RTA: Si hay valores que se repiten en la lista y son: ", lista3) # imprimimos la lista de los numeros que se repiten
    if c <= 1: # si no
        print("RTA: En la lista que creaste no hay valores que se repiten.") # Imprimimos que no hay valores repetidos

- **7. Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.**

![image](https://user-images.githubusercontent.com/124611099/236658820-3a04bd4c-130f-4a66-8a85-21f64fdbed35.png)

    n = int(input("Cuantos valores vas a digitar")) # vamos a definir esta variable para ver cuantos numeros van a digitar en la lista
    Vocales = [65, 69, 73, 79, 85, 97, 101, 105, 111, 117] # Definimos la lista de las vocales
    lista = [] # dejamos esta lista vacia para ir colocando los datos que se recolecten
    Lista1 = [] # dejamos esta lista vacia para ir colocando los datos que se recolecten
    Lista2 = [] # dejamos esta lista vacia para ir colocando los datos que se recolecten
    for y in range(0,n): # usamos un ciclo for para seleccionar los datos segun la variable n
        v = int(input("Digita el valor: ")) # DFefinimos la variable v como los elementos recibidos
        lista.append(v) # Los valores que se van recibiendo se van almacenando en la lista
    print ("1. la lista que has creado es el siguiente:", lista) # Imprimimos la lista que se creo
    for z in lista: # Para z in listas haga:
        if z in Vocales: # Si z esta en vocales entonces
            Lista1.append(z) # Entonces vamos a agregar los valores en la Lista1
            Lista2.append(chr(z)) # Entonces vamos a agregar los valores (segun la tabla ascii) en La lista2
    c = len(Lista2) # Vamos a ver cuantos valores hay en la lista2
    if c >= 2: # si c es mayor o igual que 2 entonces
        print("En la lista se encuentra una cadena de caracteres con las siguientes vocales " + str(Lista2) + " en numeros la lista queda: "+ str(Lista1)) # imprimimos la lista de los numeros y las vocales
    elif c == 1: # si c es igual que 1 entonces
        print("En la lista NO EXISTE una cadena de caracteres con vocales aunque si hay una vocal y es: ", Lista2) # Solo imprimimos la vocal pero no hay una cadena
    else: # si no
        print("En la lista NO EXISTE una cadena de caracteres con vocales") # Imprimimos que no existe una cadena

- **8. Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista. Ejemplo:**

![image](https://user-images.githubusercontent.com/124611099/236658846-45a43051-0043-416c-a017-d22bed1e1b3e.png)

    n = int(input("Cuantos valores vas a digitar en la primera lista")) # vamos a definir esta variable para ver cuantos numeros van a digitar en la lista
    Lista1 = [] # dejamos esta lista vacia para ir colocando los datos que se recolecten
    Lista2 = [] # dejamos esta lista vacia para ir colocando los datos que se recolecten
    Lista3= [] # dejamos esta lista vacia para ir colocando los datos que se recolecten
    for y in range(0,n): # usamos un ciclo for para seleccionar los datos segun la variable n
        v = (input("Digita el valor: ")) # DFefinimos la variable v como los elementos recibidos
        Lista1.append(v) # Los valores que se van recibiendo se van almacenando en la lista
    print ("1. la primera lista que has creado es el siguiente:", Lista1) # Imprimimos la lista que se creo
    N = int(input("Cuantos valores vas a digitar en la segunda lista")) # vamos a definir esta variable para ver cuantos numeros van a digitar en la lista
    for Y in range(0,N): # usamos un ciclo for para seleccionar los datos segun la variable n
        v = (input("Digita el valor: ")) # DFefinimos la variable v como los elementos recibidos
        Lista2.append(v) # Los valores que se van recibiendo se van almacenando en la lista
    print ("2. la segunda lista que has creado es el siguiente:", Lista2) # Imprimimos la lista que se creo
    for z in Lista1: # Para z in lista1 haga:
        if z in Lista2: # Si z esta en Lista2 entonces
            Lista3.append(z) # Entonces vamos a agregar los valores en la Lista3
    c = len(Lista3) # Vamos a ver cuantos valores hay en la lista3
    if c >= 1: # si c es mayor o igual que 1 entonces
        print("RTA: Los valores de la primera lista que estan en la segunda lista son:", Lista3) # Imprimimos la lista de los valores de la primera lista que se encuentran en la segunda lista
    else: # Si no
        print("No hay valores en la primera lista que se repitan en la segunda lista ") # Imprimimos que no hay valores repetidos

- **9. Resolver el punto 7 del taller 1 usando operaciones con vectores.**

![image](https://user-images.githubusercontent.com/124611099/236658875-774cfc5b-bbd7-40bd-8e4b-e36ee4a0c58e.png)

    def promedio(Lista): # Definimos promedio segun la lista creada
        Pro = sum(Lista) / len(Lista) # pro va a ser el resultado de la suma de la lista dividido la cantidad de valores en la lista
        return Pro # Retornamos el resultado de la operacion 
    def media(Lista): # Definimos media segun la lista creada
        me = sube(Lista)[len(sube(Lista)) // 2] #sacamos la mediana a través de los números ordenados encontrando el de la mitad 
        return me # Retornamos el resultado de la operacion
    def promedio_multiplicativo(Lista): # Definimos promedio_multiplicativo segun la lista creada
        producto = 1 # Definimos producto como 1
        for num in Lista: # para num en lista haga
            producto *= num # Producto es igual a producto por el num
        return producto ** (1/len(Lista)) # Retornamos el resultado del for que seria producto y luego calculamos la raíz de la cantidad de operandos
    def sube(Lista): # Definimos sube segun la lista creada
        return sorted(Lista) # Con este comando ordenamos la lista de forma ascendente
    def baja(Lista): # Definimos baja segun la lista creada
        return sorted(Lista,reverse = True) # Con este comando ordenamos la lista de forma descendente
    def mayor_elevado_menor(Lista): # Definimos mayor_elevado_menor segun la lista creada
        return max(Lista) ** min(Lista) # Con esta formula el maximo valor de la lista lo elevamos al menor valor de la lista
    def raiz_cubica(Lista): # Definimos raiz_cubica segun la lista creada
        return min(Lista) ** (1/3) # Con esta formula el minimo valor de la lista le sacamos la raiz cubica

    if __name__ == "__main__":  # Ahora ejecutamos el programa con la funcion main
        Lista = [] # dejamos esta lista vacia para ir colocando los datos que se recolecten
        for y in range(0,5): # usamos un ciclo for para seleccionar los datos segun la variable n
            v = float(input("Digita el valor: ")) # DFefinimos la variable v como los elementos recibidos
            Lista.append(v) # Los valores que se van recibiendo se van almacenando en la lista
        print ("1. la lista que has creado es el siguiente:", Lista) # Imprimimos la lista que se creo
        print("El Promedio de la lista es: ", promedio(Lista)) # Imprimimos el promedio de la lista
        print("La mediana de la lista es: ", media(Lista))  # Imprimimos la media de la lista
        print("El promedio multiplicativo de la lista es: ", promedio_multiplicativo(Lista)) # Imprimimos el promedio multiplicativo de la lista
        print("La lista al ordenarla de foma ascendente queda: ", sube(Lista)) # Imprimimos la lista de forma ascendente
        print("La lista al ordenarla de foma decendente queda: ", baja(Lista)) # Imprimimos la lista de forma descendente
        print("El mayor número (" + str(max(Lista)) + ") elevado al menor número (" + str(min(Lista)) + ") da: ", mayor_elevado_menor(Lista)) #Imprimimos el maximo valor de la lista lo elevamos al menor valor de la lista
        print("La raíz cúbica del menor número (" + str(min(Lista)) + ") es: ", raiz_cubica(Lista)) # Imprimimos el minimo valor de la lista le sacamos la raiz cubica

- **10. Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.**




