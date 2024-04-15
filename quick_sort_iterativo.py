passd = comps = trocas = 0

def quick_sort(lista, ini=0, fim=None):
    global comps, trocas, passd

    if fim is None:
        fim = len(lista) - 1

    tamanho = fim - ini + 1
    aux = [None] * tamanho

    pos = -1

    pos += 1
    aux[pos] = ini
    pos += 1
    aux[pos] = fim

    while pos >= 0:

        fim = aux[pos]
        pos -= 1
        ini = aux[pos]
        pos -= 1

        i = ini - 1
        x = lista[fim]
    
        for j in range(ini, fim):
            comps += 1
            if lista[j] <= x:

                i += 1
                lista[i], lista[j] = lista[j], lista[i]
                trocas += 1
    
        lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
        pivot = i + 1
        trocas += 1

        if pivot - 1 > ini:
            pos += 1
            aux[pos] = ini
            pos += 1
            aux[pos] = pivot - 1
            passd += 1

        if pivot + 1 < fim:
            pos += 1
            aux[pos] = pivot + 1
            pos += 1
            aux[pos] = fim
            passd += 1

######################################################################################

import sys, tracemalloc
sys.dont_write_bytecode = True
from time import time

from emp10mil import empresas

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