comps = trocas = pssd = 0

def selection_sort(lista):
    global comps, trocas, pssd
    comps = trocas = pssd = 0

    for pos_sel in range(len(lista) - 1):
        pssd += 1
        pos_menor = pos_sel

        for pos in range(pos_sel + 1, len(lista)):
            comps += 1
            if lista[pos] < lista[pos_menor]:
                pos_menor = pos

        if pos_menor != pos_sel:
            lista[pos_sel], lista[pos_menor] = lista[pos_menor], lista[pos_sel]
            trocas += 1
#######################################################################

import sys, tracemalloc
sys.dont_write_bytecode = True
from time import time

from emp100mil import empresas

tracemalloc.start() 
hora_ini = time()
selection_sort(empresas)
hora_fim = time()
mem_atual, mem_pico = tracemalloc.get_traced_memory()
tracemalloc.stop() 

print(empresas) 
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
print(f"Passadas: {pssd}; Comparações: {comps}; Trocas: {trocas}") 
print(f"Pico de memória: {mem_pico / 1024 / 1024}MB")