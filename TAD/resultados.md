# Resultados de la medición

## Tabla de tiempos

| Contactos | contiene() — binaria (µs) | búsqueda uno por uno (µs) | agregar + eliminar al inicio (µs) |
|----------:|---------------------------:|----------------------------:|-------------------------------------:|
| 1.000     | 0,75                       | 10,46                       | 1,96                                 |
| 10.000    | 0,92                       | 106,83                      | 8,79                                 |
| 100.000   | 1,17                       | 1.098,25                    | 70,46                                |

Computador: MacBook Pro (macOS), Python 3. `random.seed(11)`. Cada valor
es el mejor de 7 repeticiones.

## Interpretación (de diez mil a cien mil contactos)

1. **contiene()** casi no cambió: pasó de 0,92 µs a 1,17 µs, un factor de
   apenas ~1,27. Era de esperar, porque la búsqueda binaria es O(log n): al
   multiplicar n por diez, log(n) solo crece en una constante pequeña
   (aproximadamente 3,3 comparaciones más), no en un factor de diez.

2. **La búsqueda uno por uno** se multiplicó por ~10,28 (de 106,83 µs a
   1.098,25 µs), prácticamente el factor de diez esperado para una
   operación O(n): con diez veces más nombres, hay que revisar diez
   veces más elementos en promedio antes de confirmar que el nombre no
   está.

3. **agregar+eliminar al principio** se multiplicó por ~8,01 (de 8,79 µs
   a 70,46 µs). Es una operación O(n) porque hay que correr todos los
   elementos para abrir (y luego cerrar) el hueco, así que lo esperable
   era un factor cercano a diez; el valor observado queda razonablemente
   cerca, con la diferencia explicada por el ruido normal de la máquina
   en mediciones de microsegundos.