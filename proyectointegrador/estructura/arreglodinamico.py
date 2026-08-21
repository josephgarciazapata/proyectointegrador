class ArregloDinamico:
    def __init__(self):
        self.datos = [None] * 5
        self.cantidad = 0

    def agregar(self, elemento):
        if self.cantidad == len(self.datos):
            nuevo = [None] * (len(self.datos) * 2)

            for i in range(self.cantidad):
                nuevo[i] = self.datos[i]

            self.datos = nuevo

        self.datos[self.cantidad] = elemento
        self.cantidad += 1

    def obtener(self, posicion):
        if posicion < 0 or posicion >= self.cantidad:
            return None

        return self.datos[posicion]

    def mostrar(self):
        for i in range(self.cantidad):
            self.datos[i].mostrar()

    def tamaño(self):
        return self.cantidad