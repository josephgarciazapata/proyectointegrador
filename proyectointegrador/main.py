from modelos.paciente import Paciente
from estructura.arreglodinamico import ArregloDinamico
pacientes = ArregloDinamico()

pacientes.agregar(Paciente(1, "Leimar", 2, "08:30", 45))
pacientes.agregar(Paciente(2, "Ana", 1, "08:45", 30))
pacientes.agregar(Paciente(3, "Tobias", 3, "09:00", 20))
pacientes.agregar(Paciente(4, "Laura", 2, "09:15", 15))
pacientes.agregar(Paciente(5, "Santiago", 1, "09:30", 10))
pacientes.agregar(Paciente(6, "Joseph", 3, "09:45", 5))

pacientes.mostrar()
