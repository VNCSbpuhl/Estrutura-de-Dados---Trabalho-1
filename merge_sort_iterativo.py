def merge_sort(lista):
    tam_part = 1
    n = len(lista)
    
    while tam_part < n:
        esq = 0
        while esq < n:
            dir = min(esq + (tam_part * 2 - 1), n - 1)
            meio = esq + (dir - esq) // 2

            if tam_part > n // 2:
                meio = dir - (n % tam_part)
            
            tam_esq = meio - esq + 1
            tam_dir = dir - meio
            lista_esq = lista[esq:meio+1] 
            lista_dir = lista[meio+1:dir+1] 

            pos_esq, pos_dir, i = 0, 0, esq
            while pos_esq < tam_esq and pos_dir < tam_dir:
                if lista_esq[pos_esq] <= lista_dir[pos_dir]:
                    lista[i] = lista_esq[pos_esq]
                    pos_esq += 1
                else:
                    lista[i] = lista_dir[pos_dir]
                    pos_dir += 1
                i += 1

            while pos_esq < tam_esq:
                lista[i] = lista_esq[pos_esq]
                pos_esq += 1
                i += 1

            while pos_dir < tam_dir:
                lista[i] = lista_dir[pos_dir]
                pos_dir += 1
                i += 1

            esq += tam_part * 2
        tam_part *= 2
    return lista
############################################################

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