class Paciente:
    def __init__(self, documento, nombre, triage, hora_llegada, tiempo_espera):
        self.documento = documento
        self.nombre = nombre
        self.triage = triage
        self.hora_llegada = hora_llegada
        self.tiempo_espera = tiempo_espera

    def mostrar(self):
        print(
            f"Documento: {self.documento}"
            f" Nombre: {self.nombre}"
            f" Triage: {self.triage}"
            f" Hora llegada: {self.hora_llegada}"
            f" Tiempo de espera: {self.tiempo_espera} minutos"
        )