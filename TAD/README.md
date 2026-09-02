# Agenda — Tarea 3

`Agenda` es un TAD de contactos (nombre y teléfono) que se mantiene
siempre ordenado alfabéticamente por nombre y no admite nombres
repetidos. Está construido sobre dos listas paralelas de Python. La
búsqueda de un contacto usa una búsqueda binaria escrita a mano, lo que
permite `contiene()` y `telefono_de()` en O(log n), mientras que
`agregar()` y `eliminar()` son O(n) por tener que correr los elementos y
mantener el orden.

# Cómo correrlo

1. Poner `agenda.py`, `test_agenda.py` y `medicion.py` en la misma
   carpeta.
2. Instalar pytest una sola vez: `pip install pytest`.

# Cómo correr las pruebas

Desde esa carpeta:

```
python -m pytest -q
```

## Cómo correr la medición

```
python medicion.py
```

Imprime la tabla de tiempos para agendas de mil, diez mil y cien mil
contactos (la misma tabla de `resultados.md`) y los multiplicadores al
pasar de diez mil a cien mil.

## Extra

`interactivo.py` es un menú de consola opcional para probar la Agenda a
mano. no es uno de los seis archivos que pide la tarea.