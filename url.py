import random
from time import sleep
from multiprocessing import Pool

urls = ['a.com', 'b.com', 'c.com', 'd.com']
urls2 = ["a.com", "b.com", "c.com", "d.com", "e.com"]

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

# El siguiente código trabaja con multiprocesos. Los 4 urls de nuestra lista se ejecutan a la vez.

if __name__ == '__main__':  # Para que no se genere un bucle guardamos el codigo en un archivo y lo ejecutamos directamente
  pool = Pool(processes = 4) # Contamos con 4 procesadores porque en nuestra lista de urls tenemos 4 elementos.
  # pool.map llama a la función scrape con cada url de urls y la salida la guarda en la variable data.
  data1 = pool.map(scrape, urls) # Aquí podemos observar   que los 4 elementos de la lista se ejecutan a la vez
  data2 = pool.map(scrape, urls2) # Aquí vemos como al sólo tener 4 procesadores, el quinto elemento de nuestra lista no se ejecuta hasta que uno de los otros cuatro deje un 'puesto' libre.
  pool.close()
  print()
  print('DATA 1')
  for row in data1:
    print(row)

  print('DATA 2')
  for row in data2:
    print(row)