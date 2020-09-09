import threading

def worker(num_hilo, **secuencia):
    print('Hilo:',threading.current_thread().getName(),
          'con identificador:', threading.current_thread().ident)
    for valor in range(secuencia['comienzo'], secuencia['fin'], 1):
        print(valor)

HILOS = 5

for num_hilo in range(HILOS):

    comienzo = num_hilo * 10
    fin = 10 + num_hilo * 10
    hilo = threading.Thread(target=worker, args=(num_hilo,),
                           kwargs={'comienzo': comienzo, 'fin': fin})
    hilo.start()
    hilo.join()
