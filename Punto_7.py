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