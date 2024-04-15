divs = juncs = comps = 0

def merge_sort(lista):
    global divs, juncs, comps

    if len(lista) > 1:
        meio = len(lista) // 2
        sublista_esq = lista[:meio]
        sublista_dir = lista[meio:]

        divs += 1

        sublista_esq = merge_sort(sublista_esq)
        sublista_dir = merge_sort(sublista_dir)

        pos_esq = pos_dir = 0
        ordenada = [] 

        while pos_esq < len(sublista_esq) and pos_dir < len(sublista_dir):
            comps += 1
            if sublista_esq[pos_esq] <= sublista_dir[pos_dir]:
                ordenada.append(sublista_esq[pos_esq])
                pos_esq += 1
            else:
                ordenada.append(sublista_dir[pos_dir])
                pos_dir += 1

        if pos_esq < len(sublista_esq):
            sobra = sublista_esq[pos_esq:]
        else:
            sobra = sublista_dir[pos_dir:]

        juncs += 1

        return ordenada + sobra    
    else:
        return lista
#######################################################################

import sys, tracemalloc
sys.dont_write_bytecode = True
from time import time

from emp100mil import empresas

tracemalloc.start()
divs = juncs = comps = 0
hora_ini = time()
nomes_ord = merge_sort(empresas)
hora_fim = time()

mem_atual, mem_pico = tracemalloc.get_traced_memory()
tracemalloc.stop()   

print(empresas) 
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
print(f"Pico de memória: {mem_pico / 1024 / 1024}MB")