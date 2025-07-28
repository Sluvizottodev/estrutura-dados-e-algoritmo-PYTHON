# Elemento por elemento

def buscaLinear (lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1

# Pior caso O(n)