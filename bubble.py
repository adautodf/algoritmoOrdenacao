import random

def bubble_sort(lista):
    n = len(lista)

    for j in range(n-1):
        for i in range(n-1-j): 
            if lista[i] > lista[i+1]:
                # Troca de elementos nas posições i e i+1
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista

any_numbers = random.sample(range(1, 50), 15)

lista = any_numbers
print("Lista default: ", lista)

bubble_sort(lista)
print("Lista ordenada: ", lista)
