

def merge_sort(arreglo):
    if len(arreglo) <= 1:
        return
    _merge_sort(arreglo, 0, len(arreglo) - 1)

def _merge_sort(arreglo, inicio, fin):
    if inicio < fin:
        medio = (inicio + fin) // 2
        _merge_sort(arreglo, inicio, medio)
        _merge_sort(arreglo, medio + 1, fin)
        _merge(arreglo, inicio, medio, fin)

def _merge(arreglo, inicio, medio, fin):
    n1 = medio - inicio + 1
    n2 = fin - medio

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arreglo[inicio + i]
    for j in range(n2):
        R[j] = arreglo[medio + 1 + j]

    i = 0
    j = 0
    k = inicio

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arreglo[k] = L[i]
            i += 1
        else:
            arreglo[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arreglo[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arreglo[k] = R[j]
        j += 1
        k += 1