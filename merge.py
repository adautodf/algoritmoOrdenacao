import random

def merge(lista, inicio, meio, fim):
    esquerda = lista[inicio:meio]
    direita = lista[meio:fim]
    topo_esquerda, topo_direita = 0, 0
    for k in range(inicio, fim):
        if topo_esquerda >= len(esquerda):
            lista[k] = direita[topo_direita]
            topo_direita += 1
        elif topo_direita >= len(direita):
            lista[k] = esquerda[topo_esquerda]
            topo_esquerda += 1
        elif esquerda[topo_esquerda] < direita[topo_direita]:
            lista[k] = esquerda[topo_esquerda]
            topo_esquerda += 1
        else:
            lista[k] = direita[topo_direita]
            topo_direita += 1

 
def merge_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)

    if fim - inicio > 1:
        meio = (fim + inicio) // 2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)
        merge(lista, inicio, meio, fim)


any_numbers = random.sample(range(1, 50), 15)

lista = any_numbers
print("Lista default: ", lista)

merge_sort(lista)
print("Lista ordenada: ", lista)
