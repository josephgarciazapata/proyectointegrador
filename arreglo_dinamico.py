import ctypes

class ArregloDinamico:
    def __init__(self):
        self.n = 0
        self.capacidad = 1
        self.A = self._crear_arreglo(self.capacidad)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            raise IndexError('Índice fuera de rango')
        return self.A[k]

    def __setitem__(self, k, valor):
        if not 0 <= k < self.n:
            raise IndexError('Índice fuera de rango')
        self.A[k] = valor

    def _crear_arreglo(self, capacidad):
        return (capacidad * ctypes.py_object)()

    def agregar(self, elemento):
        if self.n == self.capacidad:
            self._redimensionar(2 * self.capacidad)
        self.A[self.n] = elemento
        self.n += 1

    def _redimensionar(self, nueva_capacidad):
        B = self._crear_arreglo(nueva_capacidad)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacidad = nueva_capacidad