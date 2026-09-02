"""interactivo.py

Menú de consola para probar la Agenda a mano. No es uno de los seis archivos que pide la Tarea 3 (ver README.md); es una herramienta extra para explorar la clase mientras se desarrolla.
"""

from agenda import Agenda

def mostrar_menu() -> None:
    print()
    print("-" * 40)
    print("  AGENDA - menú interactivo")
    print("-" * 40)
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto (contiene)")
    print("4. Ver teléfono de un contacto")
    print("5. Listar todos los contactos")
    print("6. Ver cuántos contactos hay")
    print("0. Salir")
    
def pedir_texto(mensaje: str) -> str:
    return input(mensaje).strip()

def accion_agregar(agenda: Agenda) -> None:
    nombre = pedir_texto("Nombre: ")
    telefono = pedir_texto("Teléfono: ")
    try:
        agenda.agregar(nombre, telefono)
        print(f"OK: '{nombre}' quedó guardado con teléfono '{telefono}'.")
    except ValueError as error:
        print(f"Error: {error}")
        
def accion_eliminar(agenda: Agenda) -> None:
    nombre = pedir_texto("Nombre a eliminar: ")
    try:
        agenda.eliminar(nombre)
        print(f"OK: '{nombre}' fue eliminado")
    except KeyError:
        print(f"Error: '{nombre}' no está en la agenda.")
        
def accion_buscar(agenda: Agenda) -> None:
    nombre = pedir_texto("Nombre a buscar: ")
    if agenda.contiene(nombre):
        print(f"Sí, '{nombre}' está en la agenda.")
    else:
        print(f"No, '{nombre}' no está en la agenda.")
        
def accion_telefono(agenda: Agenda) -> None:
    nombre = pedir_texto("Nombre: ")
    try:
        telefono = agenda.telefono_de(nombre)
        print(f"El teléfono de '{nombre}' es '{telefono}'.")
    except KeyError:
        print(f"Error: '{nombre}' no está en la agenda.")
        
def accion_listar(agenda: Agenda) -> None:
    nombres = agenda.nombres()
    if not nombres:
        print("La agenda está vacía.")
        return
    print(f"Contactos ({len(nombres)}), en orden alfabético:")
    for i, nombre in enumerate(nombres, start=1):
        print(f"  {i}. {nombre} - {agenda.telefono_de(nombre)}")
        
def accion_cantidad(agenda: Agenda) -> None:
    print(f"Hay {len(agenda)} contactos en la agenda.")
    
def main() -> None:
    agenda = Agenda()
    acciones = {
        "1": accion_agregar,
        "2": accion_eliminar,
        "3": accion_buscar,
        "4": accion_telefono,
        "5": accion_listar,
        "6": accion_cantidad,
    }
    
    while True:
        mostrar_menu()
        opcion = pedir_texto("Opción: ")
        if opcion == "0":
            print("Hasta luego.")
            break
        accion = acciones.get(opcion)
        if accion is None:
            print("Opción inválida, intenta de nuevo.")
            continue
        accion(agenda)
        
if __name__ == "__main__":
    main()