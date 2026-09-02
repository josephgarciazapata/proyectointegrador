import random
import string
import time

from agenda import Agenda

random.seed(11)

TAMANOS = [1_000, 10_000, 100_000]
REPETICIONES = 7


def nombre_aleatorio(longitud: int = 10) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=longitud))


def generar_nombres_unicos(cantidad: int) -> list:
    """cantidad nombres distintos de 10 letras minúsculas al azar."""
    vistos = set()
    while len(vistos) < cantidad:
        vistos.add(nombre_aleatorio())
    return list(vistos)


def construir_agenda(nombres: list) -> Agenda:
    agenda = Agenda()
    for nombre in nombres:
        agenda.agregar(nombre, "3000000000")
    return agenda


def nombre_ausente(agenda: Agenda) -> str:
    """Un nombre de 10 letras que garantizadamente NO está en la agenda."""
    while True:
        candidato = nombre_aleatorio()
        if not agenda.contiene(candidato):
            return candidato


def mejor_tiempo(funcion, repeticiones: int = REPETICIONES) -> float:
    """Corre `funcion` varias veces y devuelve el mejor tiempo, en segundos."""
    mejor = float("inf")
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        funcion()
        fin = time.perf_counter()
        mejor = min(mejor, fin - inicio)
    return mejor


def buscar_ingenuo(lista: list, objetivo: str) -> bool:
    """La versión "un contacto a la vez": bucle for + if, sin usar in."""
    for nombre in lista:
        if nombre == objetivo:
            return True
    return False


def medir_tamano(n: int) -> dict:
    nombres = generar_nombres_unicos(n)
    agenda = construir_agenda(nombres)
    ausente = nombre_ausente(agenda)

    t_binaria = mejor_tiempo(lambda: agenda.contiene(ausente))

    lista_nombres = agenda.nombres()
    t_ingenua = mejor_tiempo(lambda: buscar_ingenuo(lista_nombres, ausente))

    primero_del_alfabeto = "A" * 10

    def agregar_y_eliminar():
        agenda.agregar(primero_del_alfabeto, "3000000000")
        agenda.eliminar(primero_del_alfabeto)

    t_agregar = mejor_tiempo(agregar_y_eliminar)

    return {
        "n": n,
        "contiene_binaria_s": t_binaria,
        "busqueda_ingenua_s": t_ingenua,
        "agregar_peor_caso_s": t_agregar,
    }


def formatear_us(segundos: float) -> str:
    """segundos -> microsegundos, con punto de miles y coma decimal."""
    microsegundos = segundos * 1_000_000
    texto = f"{microsegundos:,.2f}"
    return texto.replace(",", "_").replace(".", ",").replace("_", ".")


def formatear_entero(numero: int) -> str:
    return f"{numero:,}".replace(",", ".")


def main():
    resultados = [medir_tamano(n) for n in TAMANOS]

    print(f"{'n':>12}  {'contiene (µs)':>15}  {'ingenua (µs)':>15}  {'agregar+eliminar (µs)':>22}")
    for r in resultados:
        print(
            f"{formatear_entero(r['n']):>12}  "
            f"{formatear_us(r['contiene_binaria_s']):>15}  "
            f"{formatear_us(r['busqueda_ingenua_s']):>15}  "
            f"{formatear_us(r['agregar_peor_caso_s']):>22}"
        )

    if len(resultados) >= 2:
        print("\nMultiplicadores al pasar de 10.000 a 100.000:")
        r10k = next(r for r in resultados if r["n"] == 10_000)
        r100k = next(r for r in resultados if r["n"] == 100_000)
        for clave, etiqueta in [
            ("contiene_binaria_s", "contiene (binaria)"),
            ("busqueda_ingenua_s", "búsqueda ingenua"),
            ("agregar_peor_caso_s", "agregar (peor caso)"),
        ]:
            multiplicador = r100k[clave] / r10k[clave]
            print(f"  {etiqueta:<22}: x{multiplicador:.2f}")


if __name__ == "__main__":
    main()
