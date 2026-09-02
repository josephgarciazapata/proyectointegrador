"""agenda.py

Clase Agenda: un TAD de contactos (nombre -> teléfono) que se mantiene siempre ordenado alfabéticamente por nombre y que no admite nombres repetidos.

Se construye sobre una lista de Python (list.insert, list.pop y list.append están permitidos: son el "correr los elementos" del arreglo, hecho en C). La búsqueda está escrita a mano: no se usa bisect, in ni .index() para localizar un contacto, y en ninguna parte de este archivo aparece sorted() ni .sort().
"""

from typing import List, Tuple

class Agenda:
    """TAD Agenda: contactos (nombre, teléfono) ordenados por nombre."""
    
    def __init__(self) -> None:
        """Crea una agenda vacía.
        
        Complejidad: 0(1)
        """
        self._nombres: List[str] = []
        self._telefonos: List[str] = []
        
    def __len__(self) -> int:
        """Devuelve cuantos contactos hay en la agenda.
        
        Complejidad: 0(1)
        """
        return len(self._nombres)
    
    def _buscar(self, nombre: str) -> Tuple[bool, int]:
        """Busca 'nombre' con búsqueda binaria escrita a mano.
        
        Devuelve una tupla (encontrado, indice). Si encontrado es True, indice es la posicion donde está ese contacto. Si es False, indice es la posición donde habría que insertarlo para que la agenda siga ordenada.
        
        Complejidad: 0(log n)
        """
        bajo = 0
        alto = len(self._nombres)
        while bajo < alto:
            medio = (bajo + alto) // 2
            actual = self._nombres[medio]
            if actual == nombre:
                return True, medio
            elif actual < nombre:
                bajo = medio + 1
            else:
                alto = medio
        return False, bajo
    
    def contiene(self, nombre: str) -> bool:
        """Inidca si ese nombre está en la agenda.
        
        Comoplejidad: 0(log n)
        """
        encontrado, _ = self._buscar(nombre)
        return encontrado
    
    def telefono_de(self, nombre: str) -> str:
        """Devuelve el teléfono de ese contacto.
        
        Lanza KeyError si el nombre no está en la agenda.
        
        Complejidad: 0(log n)
        """
        encontrado, indice = self._buscar(nombre)
        if not encontrado:
            raise KeyError(nombre)
        return self._telefonos[indice]
    
    def nombres(self) -> List[str]:
        """Develve todos los nombres, en orden alfabético, en una lista nueva.
        
        La lista devuelta es independiente de la agenda: quien la reciba puede modificarla sin que la agenda se entere.
        
        Complejidad: 0(n)
        """
        return list(self._nombres)
    
    def agregar(self, nombre: str, telefono: str) -> None:
        """Agrega el contacto (nombre, telefono).
        
        Si el nombre ya existe, actualiza el teléfono en vez de duplicarlo. Si el nombre está vacío, lanza ValueError. El teléfono se guarda siempre como texto (str).
        
        Complejidad: 0(n)
        """
        if nombre == "":
            raise ValueError("El nombre no puede estar vacío")
        telefono = str(telefono)
        encontrado, indice = self._buscar(nombre)
        if encontrado:
            self._telefonos[indice] = telefono
        else:
            self._nombres.insert(indice, nombre)
            self._telefonos.insert(indice, telefono)
            
    def eliminar(self, nombre: str) -> None:
        """Elimina ese contacto de la agenda.
        
        Lanza KeyError si el nombre no está.
        
        Complejidad: 0(n)
        """
        encontrado, indice = self._buscar(nombre)
        if not encontrado:
            raise KeyError(nombre)
        self._nombres.pop(indice)
        self._telefonos.pop(indice)