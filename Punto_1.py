Lista = [] # Creamos una lista vacia para almacenar los datos recolectados.
def separados(a): # Definimos la funcion separados con la variable a
   while a > 0: # Mientras a sea mayor que a sea mayor que 0 haga
        Lista.insert(0, a % 10) # Con la formula se agregara la ultima cifra en la primera parte de la lista
        a = a // 10 # Con esta formula eliminamos la ultima cifra del numero
   print ("El numero que escribiste es " + str(n) + " y al separarlo queda " + str(Lista)) # Se imprime el resultado

n = int(input("Escribe el valor que quieres separar: ")) # Definimos la variable n
separados(n) # Corremos la funcion con la variable n