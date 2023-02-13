import random
from time import sleep

urls = ['a.com', 'b.com', 'c.com', 'd.com']

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
  