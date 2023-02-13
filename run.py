from url import *

urls1 = ["a.com", "b.com", "c.com", "d.com"]
urls2 = ["a.com", "b.com", "c.com", "d.com", "e.com"]

if __name__ == '__main__':
    print('-------------------------------------------------------------------------')
    print('Comenzamos ejecutando el código secuencial con 4 urls.\n')
    secuencial(urls1) # Aquí vemos que hasta que no termine un proceso no comienza el siguiente, realizando tan sólo un proceso a la vez.
    print('-------------------------------------------------------------------------')
    print('Comenzamos ejecutando el código de multiproceso con 4 urls y 4 procesadores.\n')
    multiproceso(urls1) # Aquí podemos observar que los 4 elementos de la lista se ejecutan a la vez.
    print('-------------------------------------------------------------------------')
    print('Comenzamos ejecutando el código de multiproceso con 5 urls y 4 procesadores.\n')
    multiproceso(urls2) # Aquí vemos como al sólo tener 4 procesadores, el quinto elemento de nuestra lista no se ejecuta hasta que uno de los otros cuatro deje un 'puesto' libre.
    # Comparando los tiempos de trabajo secuencial con el de multiproceso podemos afirmar que tarda menos con multiproceso.