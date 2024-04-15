comps = trocas = pssd = 0

def bubble_sort(lista):
    global comps, trocas, pssd
    comps = trocas = pssd = 0

    while True:
        pssd += 1

        trocou = False

        for pos in range(len(lista) - 1):

            comps += 1

            if lista[pos + 1] < lista[pos]:
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]
                trocas += 1
                trocou = True
        print(lista)

        if not trocou:
            break
#######################################################################

import sys, tracemalloc
sys.dont_write_bytecode = True 
from time import time

from emp10mil import empresas

tracemalloc.start() 
hora_ini = time()
bubble_sort(empresas)
hora_fim = time()
mem_atual, mem_pico = tracemalloc.get_traced_memory()
tracemalloc.stop() 

print(empresas)  
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
print(f"Passadas: {pssd}; Comparações: {comps}; Trocas: {trocas}")
print(f"Pico de memória: {mem_pico / 1024 / 1024}MB")