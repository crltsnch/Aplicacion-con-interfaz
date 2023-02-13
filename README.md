# Primera en paralelo
El link a nuestro repositorio es: [GitHub](https://github.com/crltsnch/Primera-en-paralelo)
https://github.com/crltsnch/Primera-en-paralelo

# Archivo `url.py`
```
import random
from time import sleep
from multiprocessing import Pool

def scrape(url):
  print('starting', url)
  duration = round(random.random(), 3)
  sleep(duration)
  print('finished', url, 'time taken: ', duration, 'seconds')
  return url, duration

def secuencial(urls):
  '''
  Esta función trabaja de manera secuencial. Hasta que no acaba A no empieza B y si hay muchos urls sería un problema porque tardaría mucho.
  '''
  output = []
  for url in urls:
    result = scrape(url)
    output.append(result)

def multiproceso(urls):
  '''
  Esta función trabaja con multiprocesos. Los 4 urls de nuestra lista se ejecutan a la vez.
  '''
  pool = Pool(processes = 4) # Contamos con 4 procesadores para que se puedan ejecutar hasta 4 procesos al mismo tiempo.
  data = pool.map(scrape, urls) # pool.map llama a la función scrape con cada url de urls y la salida la guarda en la variable data.
  pool.close()
  print()
  for row in data:
    print(row)
    
```
# Archivo `run.py`

```
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

```
# Conclusiones

Con este ejercicio hemos aprendido que trabajando con multiproceso es más rápido que trabajando de manera secuencial, es decir, es mucho más efectivo hacer varios procesos a la vez que esperar a que termine uno para hacer el siguiente. También hemos visto que si elegimos 4 procesadores y tenemos 5 procesos, se queda uno sin ejecutar porque los 4 procesadores están ocupados. Hasta que no acabe uno de los 4 procesadores el quinto proceso no empieza a ejecutarse.
