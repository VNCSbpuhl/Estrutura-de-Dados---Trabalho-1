passd = comps = trocas = 0

def quick_sort(lista, ini = 0, fim = None):
    global passd, comps, trocas

    if fim is None: fim = len(lista) - 1

    if fim <= ini: return

    pivot = fim
    div = ini - 1

    passd += 1

    for pos in range(ini, fim):

        comps += 1
        if lista[pos] < lista[pivot]:
            div += 1
            if(pos != div):
                lista[pos], lista[div] = lista[div], lista[pos]
                trocas += 1
    div += 1
    if(div != pivot):
        lista[div], lista[pivot] = lista[pivot], lista[div]
        trocas += 1
    quick_sort(lista, ini, div - 1)   
    quick_sort(lista, div + 1, fim)    

###############################################################

import sys, tracemalloc
sys.dont_write_bytecode = True 
from time import time

from emp100mil import empresas

passd = comps = trocas = 0

tracemalloc.start()  
hora_ini = time()
quick_sort(empresas)
hora_fim = time()

mem_atual, mem_pico = tracemalloc.get_traced_memory()
tracemalloc.stop()       

print(empresas)   
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
print(f"Passadas: {passd}; comparações: {comps}; trocas: {trocas}")
print(f"Pico de memória: { mem_pico / 1024 / 1024 }MB")