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