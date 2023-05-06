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

