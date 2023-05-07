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